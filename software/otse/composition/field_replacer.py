"""Config-driven replacement of schema field values in OTSE run JSON."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from otse.paths import LEXICON_PATH

DEFAULT_CONFIG_PATH = LEXICON_PATH

# OTSE stores mode-linking output as JSON inside raw_llm_modes_response.content
_LLM_JSON_FENCE_RE = re.compile(r"```json\s*\n?(.*?)\n?```", re.DOTALL | re.IGNORECASE)


@dataclass(frozen=True)
class FieldRule:
    field: str
    to: str
    from_values: tuple[str, ...]
    case_insensitive: bool = True
    dedupe_lists: bool = True

    def match_key(self, raw: str) -> str | None:
        if self.case_insensitive:
            probe = raw.casefold()
            for candidate in self.from_values:
                if candidate.casefold() == probe:
                    return candidate
            return None
        if raw in self.from_values:
            return raw
        return None


@dataclass
class ReplacementConfig:
    version: int
    run_artifacts: tuple[str, ...]
    rules: tuple[FieldRule, ...]
    rules_by_field: dict[str, tuple[FieldRule, ...]] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> ReplacementConfig:
        rules: list[FieldRule] = []
        for item in raw.get("rules", []):
            rules.append(
                FieldRule(
                    field=str(item["field"]),
                    to=str(item["to"]),
                    from_values=tuple(str(x) for x in item.get("from", [])),
                    case_insensitive=bool(item.get("case_insensitive", True)),
                    dedupe_lists=bool(item.get("dedupe_lists", True)),
                )
            )
        cfg = cls(
            version=int(raw.get("version", 1)),
            run_artifacts=tuple(str(x) for x in raw.get("run_artifacts", ())),
            rules=tuple(rules),
        )
        by_field: dict[str, list[FieldRule]] = {}
        for r in cfg.rules:
            by_field.setdefault(r.field, []).append(r)
        cfg.rules_by_field = {k: tuple(v) for k, v in by_field.items()}
        return cfg

    @classmethod
    def load(cls, path: Path | None = None) -> ReplacementConfig:
        config_path = path or DEFAULT_CONFIG_PATH
        raw = json.loads(config_path.read_text(encoding="utf-8"))
        return cls.from_dict(raw)

    def to_dict(self, *, description: str | None = None) -> dict[str, Any]:
        doc: dict[str, Any] = {
            "version": self.version,
            "run_artifacts": list(self.run_artifacts),
            "rules": [
                {
                    "field": r.field,
                    "to": r.to,
                    "from": list(r.from_values),
                    "case_insensitive": r.case_insensitive,
                    "dedupe_lists": r.dedupe_lists,
                }
                for r in self.rules
            ],
        }
        if description is not None:
            doc["description"] = description
        return doc

    def has_field(self, field_name: str) -> bool:
        return field_name in self.rules_by_field


def load_config_document(path: Path | None = None) -> dict[str, Any]:
    config_path = path or DEFAULT_CONFIG_PATH
    return json.loads(config_path.read_text(encoding="utf-8"))


def save_config_document(doc: dict[str, Any], path: Path | None = None) -> Path:
    config_path = path or DEFAULT_CONFIG_PATH
    config_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    reload_config(config_path)
    return config_path


_config_cache: ReplacementConfig | None = None


def default_config() -> ReplacementConfig:
    global _config_cache
    if _config_cache is None:
        _config_cache = ReplacementConfig.load()
    return _config_cache


def reload_config(path: Path | None = None) -> ReplacementConfig:
    global _config_cache
    _config_cache = ReplacementConfig.load(path)
    return _config_cache


def replace_scalar(field_name: str, value: str, config: ReplacementConfig) -> str:
    for rule in config.rules_by_field.get(field_name, ()):
        if rule.match_key(value) is not None:
            return rule.to
    return value


def replace_field_value(field_name: str, value: Any, config: ReplacementConfig) -> Any:
    """Replace a single field's JSON value (scalar or list of scalars)."""
    rules = config.rules_by_field.get(field_name)
    if not rules:
        return value
    rule = rules[0]
    if value is None:
        return value
    if isinstance(value, str):
        return replace_scalar(field_name, value, config)
    if isinstance(value, list):
        out: list[Any] = []
        seen: set[str] = set()
        for item in value:
            if isinstance(item, str):
                replaced = replace_scalar(field_name, item, config)
                if rule.dedupe_lists:
                    key = replaced.casefold() if rule.case_insensitive else replaced
                    if key in seen:
                        continue
                    seen.add(key)
                out.append(replaced)
            else:
                out.append(item)
        return out
    return value


@dataclass
class TransformStats:
    files_touched: int = 0
    fields_updated: int = 0
    values_replaced: int = 0


def _count_replacement(rule: FieldRule, before: Any, after: Any) -> int:
    if before == after:
        return 0
    if isinstance(before, list) and isinstance(after, list):
        return max(0, len(before) - len(after)) + sum(
            1 for a, b in zip(before, after) if a != b
        )
    return 1


def transform_tree(
    obj: Any,
    config: ReplacementConfig,
    stats: TransformStats | None = None,
) -> Any:
    if isinstance(obj, dict):
        out: dict[str, Any] = {}
        for key, val in obj.items():
            if key in config.rules_by_field:
                new_val = replace_field_value(key, val, config)
                if stats is not None and new_val != val:
                    stats.fields_updated += 1
                    field_rules = config.rules_by_field[key]
                    stats.values_replaced += _count_replacement(field_rules[0], val, new_val)
                out[key] = transform_tree(new_val, config, stats)
            else:
                out[key] = transform_tree(val, config, stats)
        return out
    if isinstance(obj, list):
        return [transform_tree(item, config, stats) for item in obj]
    return obj


def transform_llm_embedded_content(content: str, config: ReplacementConfig) -> str:
    """Rewrite JSON embedded in LLM ``content`` (fenced or bare object)."""

    def rewrite_json_blob(blob: str) -> str:
        try:
            parsed = json.loads(blob)
        except json.JSONDecodeError:
            return blob
        transformed = transform_tree(parsed, config)
        if transformed == parsed:
            return blob
        return json.dumps(transformed, indent=2, ensure_ascii=False)

    def fence_sub(match: re.Match[str]) -> str:
        inner = match.group(1)
        return f"```json\n{rewrite_json_blob(inner)}\n```"

    updated = _LLM_JSON_FENCE_RE.sub(fence_sub, content)
    if updated != content:
        return updated

    stripped = content.strip()
    if stripped.startswith("{") or stripped.startswith("["):
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            return content
        transformed = transform_tree(parsed, config)
        if transformed == parsed:
            return content
        return json.dumps(transformed, indent=2, ensure_ascii=False)

    return content


def transform_document(
    data: Any,
    filename: str,
    config: ReplacementConfig,
    stats: TransformStats | None = None,
) -> Any:
    data = transform_tree(data, config, stats)
    if filename == "raw_llm_modes_response.json" and isinstance(data, dict):
        content = data.get("content")
        if isinstance(content, str):
            new_content = transform_llm_embedded_content(content, config)
            if new_content != content:
                data = dict(data)
                data["content"] = new_content
                if stats is not None:
                    stats.fields_updated += 1
    return data


def iter_run_artifact_paths(
    runs_dir: Path,
    artifacts: Iterable[str],
    run_ids: Iterable[str] | None = None,
) -> Iterable[tuple[Path, str]]:
    allowed = set(run_ids) if run_ids else None
    for run_dir in sorted(runs_dir.iterdir()):
        if not run_dir.is_dir():
            continue
        if allowed is not None and run_dir.name not in allowed:
            continue
        if not (run_dir / "meta.json").is_file():
            continue
        for name in artifacts:
            path = run_dir / name
            if path.is_file():
                yield path, name


def apply_to_run_file(
    path: Path,
    filename: str,
    config: ReplacementConfig,
    *,
    dry_run: bool = False,
) -> TransformStats:
    stats = TransformStats()
    try:
        original_text = path.read_text(encoding="utf-8")
        data = json.loads(original_text)
    except (OSError, json.JSONDecodeError):
        return stats

    new_data = transform_document(data, filename, config, stats)
    if new_data == data:
        return stats

    stats.files_touched = 1
    if dry_run:
        return stats

    path.write_text(
        json.dumps(new_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return stats


@dataclass
class FileChangePreview:
    run_id: str
    artifact: str
    path: Path
    fields_updated: int
    values_replaced: int


def preview_run_changes(
    runs_dir: Path,
    config: ReplacementConfig,
    *,
    run_ids: Iterable[str] | None = None,
) -> list[FileChangePreview]:
    previews: list[FileChangePreview] = []
    artifacts = config.run_artifacts
    for path, name in iter_run_artifact_paths(runs_dir, artifacts, run_ids):
        stats = apply_to_run_file(path, name, config, dry_run=True)
        if stats.files_touched:
            previews.append(
                FileChangePreview(
                    run_id=path.parent.name,
                    artifact=name,
                    path=path,
                    fields_updated=stats.fields_updated,
                    values_replaced=stats.values_replaced,
                )
            )
    return previews


def apply_to_runs(
    runs_dir: Path,
    config: ReplacementConfig | None = None,
    *,
    dry_run: bool = False,
    run_ids: Iterable[str] | None = None,
) -> TransformStats:
    cfg = config or default_config()
    total = TransformStats()
    artifacts = cfg.run_artifacts or (
        "specs.json",
        "raw_llm.json",
        "mode_atoms.json",
        "modes.json",
        "raw_llm_modes.json",
        "raw_llm_modes_response.json",
    )
    for path, name in iter_run_artifact_paths(runs_dir, artifacts, run_ids):
        file_stats = apply_to_run_file(path, name, cfg, dry_run=dry_run)
        total.files_touched += file_stats.files_touched
        total.fields_updated += file_stats.fields_updated
        total.values_replaced += file_stats.values_replaced
    return total
