"""Pydantic model for optical-transceiver datasheet extraction.

Printed numeric fields use ``PrintedNumber``. ``otse.pipeline.units`` fills
``canonical_value`` after extraction and leaves it null when the printed unit
cannot be converted safely, including a dB value that would otherwise be placed
in a dBm field. Canonical fields are omitted from the extraction prompt.

Canonical units for printed fields:

- reach: km
- bit_rate: Gbps
- baud_rate: GBaud
- frequency_min, frequency_max, frequency_center: THz
- channel_spacing: GHz
- power_consumption: W
- supply_voltage: V
- supply_current: mA
- cable_length: m

Old extraction names map as follows:

- reach_km -> reach
- bit_rate_gbps -> bit_rate
- baud_rate_gbaud -> baud_rate
- frequency_min_thz -> frequency_min
- frequency_max_thz -> frequency_max
- channel_spacing_ghz -> channel_spacing
- power_consumption_w -> power_consumption
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

PenaltyParameter = Literal[
    "chromatic_dispersion_ps_nm",
    "pmd_ps",
    "pdl_db",
    "rx_osnr_db",
    "rx_power_dbm",
    "rx_sensitivity_dbm",
    "bit_rate",
    "tecq_db",
    "tdecq_db",
]

PenaltyTargetParameter = Literal[
    "rx_osnr_db",
    "rx_sensitivity_dbm",
    "path_penalty_db",
    "dispersion_penalty_db",
]

Comparator = Literal["eq", "lt", "le", "gt", "ge"]
Statistic = Literal["min", "typ", "max"]

CANONICAL_UNITS: dict[str, str] = {
    "reach": "km",
    "bit_rate": "Gbps",
    "baud_rate": "GBaud",
    "frequency_min": "THz",
    "frequency_max": "THz",
    "frequency_center": "THz",
    "channel_spacing": "GHz",
    "power_consumption": "W",
    "supply_voltage": "V",
    "supply_current": "mA",
    "cable_length": "m",
}

DERIVED_FIELDS: frozenset[str] = frozenset({"canonical_value", "canonical_unit"})


class PrintedNumber(BaseModel):
    """One numeric token copied from the datasheet, with its printed unit."""

    model_config = ConfigDict(extra="forbid")

    value: float = Field(description="Number exactly as printed. Do not convert or round.")
    unit: str = Field(
        description=(
            "Unit exactly as printed, such as m, km, Mbps, Gbps, MBd, GBaud, "
            "MHz, GHz, THz, nm, dB, dBm, V, mA, or W."
        )
    )
    comparator: Comparator = Field(
        "eq",
        description="eq for a plain number; lt for '<'; le for '<='; gt for '>'; ge for '>='.",
    )
    statistic: Statistic | None = Field(
        None,
        description="min, typ, or max when the datasheet labels the value. Null otherwise.",
    )
    canonical_value: float | None = Field(
        None,
        description="Pipeline-derived value in the canonical unit. Leave null during extraction.",
        json_schema_extra={"filled_by": "pipeline"},
    )
    canonical_unit: str | None = Field(
        None,
        description="Pipeline-derived unit. Leave null during extraction.",
        json_schema_extra={"filled_by": "pipeline"},
    )


class PenaltyCondition(BaseModel):
    """One printed condition attached to a penalty."""

    model_config = ConfigDict(extra="forbid")

    parameter: PenaltyParameter = Field(description="Condition parameter named by the datasheet.")
    value: float = Field(description="Condition number exactly as printed.")
    unit: str | None = Field(
        None,
        description=(
            "Printed unit when the parameter name does not fix it, such as Mbps on bit_rate. "
            "Null for dBm, dB, ps/nm, and ps parameters."
        ),
    )


class PenaltyPoint(BaseModel):
    """A printed penalty magnitude, with a degraded value or condition only when printed."""

    model_config = ConfigDict(extra="forbid")

    target_parameter: PenaltyTargetParameter = Field(
        description=(
            "Degraded parameter: rx_osnr_db, rx_sensitivity_dbm, path_penalty_db, "
            "or dispersion_penalty_db."
        )
    )
    penalty_db: float = Field(description="Penalty magnitude in dB exactly as printed.")
    penalized_value: float | None = Field(
        None,
        description=(
            "Degraded measurement if printed, such as 24.2 for 24.2 dB OSNR. Null if absent."
        ),
    )
    conditions: list[PenaltyCondition] = Field(
        default_factory=list,
        description="Printed operating conditions. Use an empty list when none is printed.",
    )
    source: str | None = Field(
        None,
        description="Section and row where it was found, such as 'Optical | Dispersion penalty'.",
    )


class OrderableVariant(BaseModel):
    """One ordering-table row or one temperature-grade part number."""

    model_config = ConfigDict(extra="forbid")

    model: str | None = Field(None, description="Orderable part number printed on this row.")
    temp_grade: str | None = Field(
        None,
        description="Printed grade or SKU marker, such as C, E, I, commercial, or industrial.",
    )
    temp_min_c: float | None = Field(
        None, description="Minimum operating temperature in °C printed for this variant."
    )
    temp_max_c: float | None = Field(
        None, description="Maximum operating temperature in °C printed for this variant."
    )
    reach: list[PrintedNumber] | None = Field(
        None, description="Reach printed on this row. Do not convert meters to kilometers."
    )
    bit_rate: list[PrintedNumber] | None = Field(
        None, description="Data rate printed on this row, with its printed unit."
    )
    wavelength_tx_center_nm: list[float] | None = Field(
        None, description="Transmit center wavelength in nm when this row states one."
    )
    wavelength_rx_center_nm: list[float] | None = Field(
        None, description="Receive center wavelength in nm when this row states one."
    )
    frequency_center: list[PrintedNumber] | None = Field(
        None, description="Optical frequency printed on this row, with its printed unit."
    )
    cable_length: list[PrintedNumber] | None = Field(
        None, description="Cable length printed on this row for a copper, DAC, or AOC part."
    )
    cable_category: list[str] | None = Field(
        None, description="Printed cable category for this row, such as Cat5e or Cat6."
    )


class TransceiverSpecs(BaseModel):
    """Values explicitly printed on one datasheet. Use null when a value is absent."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    vendor: str | None = Field(
        None,
        description=(
            "Manufacturer explicitly named for this product. "
            "Do not use a footer, logo, distributor, or website."
        ),
    )
    model: list[str] | None = Field(
        None, description="Product model or orderable part numbers printed for this datasheet."
    )
    form_factor: list[str] | None = Field(
        None,
        description=(
            "Printed form factor. Examples are not a closed list: SFP, SFP+, SFP28, "
            "SFP-DD, DSFP, QSFP+, QSFP28, QSFP-DD, OSFP, CFP, CFP2, CFP2-DCO, XFP."
        ),
    )
    standards_claimed: list[str] | None = Field(
        None, description="Standards or MSA names the datasheet claims, as printed."
    )
    emitter_type: list[str] | None = Field(
        None, description="Optical emitter type printed for this module, such as DFB, FP, or VCSEL."
    )
    photodetector_type: list[str] | None = Field(
        None, description="Photodetector type printed for this module, such as PIN or APD."
    )

    wavelength_min_nm: list[float] | None = Field(
        None,
        description=(
            "Minimum of an unscoped wavelength range in nm. "
            "Use the tx/rx fields when transmit and receive differ."
        ),
    )
    wavelength_max_nm: list[float] | None = Field(
        None, description="Maximum of an unscoped wavelength range in nm."
    )
    wavelength_center_nm: list[float] | None = Field(
        None, description="Unscoped center wavelength in nm."
    )
    wavelength_tx_min_nm: list[float] | None = Field(
        None, description="Minimum transmit wavelength in nm."
    )
    wavelength_tx_max_nm: list[float] | None = Field(
        None, description="Maximum transmit wavelength in nm."
    )
    wavelength_tx_center_nm: list[float] | None = Field(
        None, description="Transmit center wavelength in nm."
    )
    wavelength_rx_min_nm: list[float] | None = Field(
        None, description="Minimum receive wavelength in nm."
    )
    wavelength_rx_max_nm: list[float] | None = Field(
        None, description="Maximum receive wavelength in nm."
    )
    wavelength_rx_center_nm: list[float] | None = Field(
        None, description="Receive center wavelength in nm."
    )
    wavelength_band: list[str] | None = Field(
        None,
        description=(
            "Printed spectral band, such as C-band, L-band, O-band, CWDM, or LAN-WDM. "
            "Examples are not a closed list."
        ),
    )
    frequency_min: list[PrintedNumber] | None = Field(
        None, description="Minimum optical frequency with its printed unit."
    )
    frequency_max: list[PrintedNumber] | None = Field(
        None, description="Maximum optical frequency with its printed unit."
    )
    frequency_center: list[PrintedNumber] | None = Field(
        None, description="Center optical frequency with its printed unit."
    )
    channel_spacing: list[PrintedNumber] | None = Field(
        None,
        description="Printed channel spacing with its unit, including nm when the grid is in nm.",
    )
    channel_total: list[int] | None = Field(None, description="Number of channels printed.")

    mounting_type: list[str] | None = Field(
        None,
        description="Printed mounting type, such as pluggable or solder. Not a form factor.",
    )
    connector_type: list[str] | None = Field(
        None,
        description=(
            "Printed connector. Examples are not a closed list: LC, SC, MPO, MTP, "
            "CS, SN, MDC, FC, ST, RJ-45."
        ),
    )
    fiber_type: list[str] | None = Field(
        None,
        description=(
            "Printed transmission media. Examples are not a closed list: SMF, MMF, "
            "OM3, OM4, OM5, G.652, G.655, G.657, copper, DAC, AOC."
        ),
    )
    cable_category: list[str] | None = Field(
        None, description="Printed copper cable category, such as Cat5e or Cat6."
    )
    cable_length: list[PrintedNumber] | None = Field(
        None, description="Printed cable length for a copper, DAC, or AOC assembly."
    )
    temp_min_c: float | None = Field(
        None,
        description=(
            "Minimum operating temperature in °C when one range applies to every part. "
            "Use variants when grades differ."
        ),
    )
    temp_max_c: float | None = Field(
        None,
        description=(
            "Maximum operating temperature in °C when one range applies to every part. "
            "Use variants when grades differ."
        ),
    )
    power_consumption: list[PrintedNumber] | None = Field(
        None, description="Printed electrical consumption with its unit, such as W or mW."
    )
    supply_voltage: list[PrintedNumber] | None = Field(
        None, description="Printed supply voltage with its unit."
    )
    supply_current: list[PrintedNumber] | None = Field(
        None, description="Printed supply current with its unit, such as mA."
    )

    host_interface_name: list[str] | None = Field(
        None, description="Host interface name printed on the datasheet. Do not recall MSA names."
    )
    host_interface_id_hex: list[str] | None = Field(
        None, description="Host interface ID printed in hexadecimal. Do not derive it."
    )
    host_interface_id: list[int] | None = Field(
        None, description="Host interface ID printed in decimal. Do not derive it."
    )
    media_interface_name: list[str] | None = Field(
        None, description="Media interface name printed on the datasheet. Do not recall MSA names."
    )
    media_interface_id_hex: list[str] | None = Field(
        None, description="Media interface ID printed in hexadecimal. Do not derive it."
    )
    media_interface_id: list[int] | None = Field(
        None, description="Media interface ID printed in decimal. Do not derive it."
    )
    frame: list[str] | None = Field(
        None, description="Printed host frame or lane combination, such as 8x 100GAUI-1."
    )
    standards_code: list[str] | None = Field(
        None,
        description=(
            "Printed application code, profile, or protocol label, such as an OpenZR+ mode, "
            "Fibre Channel code, Ethernet rate name, or OTN label."
        ),
    )

    baud_rate: list[PrintedNumber] | None = Field(
        None, description="Printed symbol rate with its unit."
    )
    bit_rate: list[PrintedNumber] | None = Field(
        None, description="Printed data rate with its unit. Do not convert Mbps to Gbps."
    )
    roll_off_percent: list[float] | None = Field(None, description="Spectral roll-off in percent.")
    modulation_format: list[str] | None = Field(
        None,
        description=(
            "Printed modulation format. Examples are not a closed list: NRZ, PAM4, "
            "QPSK, 8QAM, 16QAM, 64QAM."
        ),
    )
    reach: list[PrintedNumber] | None = Field(
        None,
        description=(
            "Printed transmission reach with its unit. "
            "Do not convert a meter value into kilometers."
        ),
    )
    tx_power_min_dbm: list[float] | None = Field(
        None,
        description=(
            "Minimum average transmitter output power in dBm. "
            "Leave null when the printed unit is not dBm."
        ),
    )
    tx_power_max_dbm: list[float] | None = Field(
        None,
        description=(
            "Maximum average transmitter output power in dBm. "
            "Leave null when the printed unit is not dBm."
        ),
    )
    tx_oma_min_dbm: list[float] | None = Field(
        None, description="Minimum transmitter OMA in dBm. Do not store this as average power."
    )
    tx_oma_max_dbm: list[float] | None = Field(
        None, description="Maximum transmitter OMA in dBm. Do not store this as average power."
    )
    tx_in_band_osnr_db: list[float] | None = Field(
        None, description="Transmitter in-band OSNR in dB."
    )
    tx_out_of_band_osnr_db: list[float] | None = Field(
        None, description="Transmitter out-of-band OSNR in dB."
    )

    rx_sensitivity_dbm: list[float] | None = Field(
        None,
        description=(
            "Receiver sensitivity as average power in dBm. "
            "OMA sensitivity goes in rx_sensitivity_oma_dbm."
        ),
    )
    rx_sensitivity_oma_dbm: list[float] | None = Field(
        None, description="Receiver sensitivity specified as OMA in dBm."
    )
    rx_osnr_db: list[float] | None = Field(None, description="Required receiver OSNR in dB.")
    rx_osnr_tolerance_db_max: list[float] | None = Field(
        None, description="Maximum required OSNR in dB for the stated BER and reference bandwidth."
    )
    rx_overload_dbm: list[float] | None = Field(
        None,
        description=(
            "Unqualified maximum receiver input power in dBm. Leave null when the sheet "
            "separates per-channel and total limits."
        ),
    )
    rx_overload_per_channel_dbm: list[float] | None = Field(
        None, description="Maximum per-channel receiver input power in dBm."
    )
    rx_overload_total_dbm: list[float] | None = Field(
        None, description="Maximum total receiver input power in dBm."
    )
    damage_threshold_dbm: list[float] | None = Field(
        None, description="Receiver optical damage threshold in dBm."
    )
    cd_tolerance_ps_nm: list[float] | None = Field(
        None, description="Chromatic-dispersion tolerance in ps/nm."
    )
    pdl_db: list[float] | None = Field(None, description="PDL tolerance in dB.")
    pmd_tolerance_ps: list[float] | None = Field(None, description="PMD or DGD tolerance in ps.")
    power_budget_min_db: list[float] | None = Field(
        None,
        description="Minimum optical power budget in dB. Not insertion loss or transmitter power.",
    )
    power_budget_max_db: list[float] | None = Field(
        None,
        description="Maximum optical power budget in dB. Not insertion loss or transmitter power.",
    )
    tdecq_db: list[float] | None = Field(None, description="TDECQ in dB as printed.")
    tecq_db: list[float] | None = Field(None, description="TECQ in dB as printed.")
    tdp_db: list[float] | None = Field(
        None, description="Transmitter and dispersion penalty (TDP) in dB as printed."
    )
    spectral_width_nm: list[float] | None = Field(
        None,
        description=(
            "Spectral width in nm. Put the printed definition, such as RMS or -20 dB, in notes."
        ),
    )
    rin_db_hz: list[float] | None = Field(None, description="Relative intensity noise in dB/Hz.")

    fec_type: list[str] | None = Field(
        None,
        description="FEC name printed on the datasheet. Do not name a FEC that is only required.",
    )
    fec_overhead_percent: list[float] | None = Field(None, description="FEC overhead in percent.")
    pre_fec_ber_threshold: list[float] | None = Field(
        None, description="Printed pre-FEC BER threshold."
    )
    post_fec_ber_target: list[float] | None = Field(
        None, description="Printed post-FEC BER target."
    )

    extinction_ratio_db: list[float] | None = Field(None, description="Extinction ratio in dB.")
    los_assert_dbm: list[float] | None = Field(None, description="LOS assert threshold in dBm.")
    los_deassert_dbm: list[float] | None = Field(
        None, description="LOS deassert threshold in dBm."
    )
    los_hysteresis_db: list[float] | None = Field(None, description="LOS hysteresis in dB.")
    channel_insertion_loss_db: list[float] | None = Field(
        None,
        description="Channel insertion loss in dB. Do not store an optical power budget here.",
    )
    receiver_reflectance_db: list[float] | None = Field(
        None, description="Receiver reflectance in dB."
    )
    transmitter_reflectance_db: list[float] | None = Field(
        None, description="Transmitter reflectance in dB."
    )
    optical_return_loss_tolerance_db: list[float] | None = Field(
        None, description="Optical return loss tolerance in dB."
    )
    number_of_lanes: list[int] | None = Field(None, description="Number of lanes printed.")
    side_mode_suppression_ratio_db: list[float] | None = Field(
        None, description="Side-mode suppression ratio in dB."
    )
    total_jitter_ps: list[float] | None = Field(None, description="Total jitter in ps.")

    penalties: list[PenaltyPoint] | None = Field(
        None,
        description=(
            "Printed OSNR, sensitivity, dispersion, and path penalties. "
            "A magnitude alone is valid."
        ),
    )
    variants: list[OrderableVariant] | None = Field(
        None,
        description=(
            "One entry per ordering-table row or temperature grade. "
            "Bind only values printed on that row."
        ),
    )
    notes: str | None = Field(
        None,
        description=(
            "Ambiguity, brand conflict, formula, inequality context, or condition that "
            "qualifies a stored value. Do not list parameters the datasheet omits."
        ),
    )
    provenance_datasheet_sections: str | list[str] | None = Field(
        None,
        description=(
            "Section headings that supplied extracted values, including ordering information."
        ),
    )
    suggestions: str | None = Field(
        None,
        description=(
            "A printed value that cannot be stored without changing its meaning. "
            "Do not list absent parameters or propose general schema ideas."
        ),
    )


TransceiverDatasheet = TransceiverSpecs

FIELD_BUNDLES: dict[str, list[str]] = {
    "identification": ["vendor", "model", "form_factor", "standards_claimed"],
    "interfaces": [
        "host_interface_name",
        "host_interface_id_hex",
        "media_interface_name",
        "media_interface_id_hex",
    ],
    "wavelength": [
        "wavelength_min_nm",
        "wavelength_max_nm",
        "wavelength_center_nm",
        "wavelength_tx_center_nm",
        "wavelength_rx_center_nm",
        "wavelength_band",
        "channel_spacing",
    ],
    "physical": [
        "connector_type",
        "fiber_type",
        "cable_category",
        "temp_min_c",
        "temp_max_c",
    ],
    "electrical": ["baud_rate", "bit_rate", "modulation_format"],
    "power": [
        "tx_power_min_dbm",
        "tx_power_max_dbm",
        "tx_oma_min_dbm",
        "tx_oma_max_dbm",
        "power_budget_min_db",
        "power_budget_max_db",
    ],
    "fec": [
        "fec_type",
        "fec_overhead_percent",
        "pre_fec_ber_threshold",
        "post_fec_ber_target",
    ],
}

# Values that can co-occur in one selectable operating mode.
MODE_FIELDS: list[str] = [
    "channel_spacing",
    "form_factor",
    "frequency_min",
    "frequency_max",
    "frequency_center",
    "wavelength_band",
    "wavelength_min_nm",
    "wavelength_max_nm",
    "wavelength_center_nm",
    "wavelength_tx_min_nm",
    "wavelength_tx_max_nm",
    "wavelength_tx_center_nm",
    "wavelength_rx_min_nm",
    "wavelength_rx_max_nm",
    "wavelength_rx_center_nm",
    "channel_total",
    "model",
    "number_of_lanes",
    "baud_rate",
    "bit_rate",
    "roll_off_percent",
    "modulation_format",
    "reach",
    "tx_power_min_dbm",
    "tx_power_max_dbm",
    "tx_oma_min_dbm",
    "tx_oma_max_dbm",
    "tx_in_band_osnr_db",
    "tx_out_of_band_osnr_db",
    "rx_sensitivity_dbm",
    "rx_sensitivity_oma_dbm",
    "rx_osnr_db",
    "rx_osnr_tolerance_db_max",
    "rx_overload_dbm",
    "rx_overload_per_channel_dbm",
    "rx_overload_total_dbm",
    "damage_threshold_dbm",
    "cd_tolerance_ps_nm",
    "pdl_db",
    "pmd_tolerance_ps",
    "power_budget_min_db",
    "power_budget_max_db",
    "tdecq_db",
    "tecq_db",
    "tdp_db",
    "fec_type",
    "fec_overhead_percent",
    "pre_fec_ber_threshold",
    "post_fec_ber_target",
    "extinction_ratio_db",
    "los_assert_dbm",
    "los_deassert_dbm",
    "host_interface_name",
    "host_interface_id_hex",
    "host_interface_id",
    "media_interface_name",
    "media_interface_id_hex",
    "media_interface_id",
    "power_consumption",
    "supply_voltage",
    "supply_current",
    "standards_code",
    "frame",
    "penalties",
]

MODE_FIELDS_OPT: list[str] = [
    "fec_type",
    "fec_overhead_percent",
]

STANDARDS_IDENTITY_FIELDS: list[str] = [
    "host_interface_name",
    "host_interface_id_hex",
    "host_interface_id",
    "media_interface_name",
    "media_interface_id_hex",
    "media_interface_id",
    "standards_code",
    "frame",
]

STANDARDS_IMPLIED_FIELDS: list[str] = [
    "channel_spacing",
    "baud_rate",
    "bit_rate",
    "modulation_format",
    "reach",
]

__all__ = [
    "CANONICAL_UNITS",
    "DERIVED_FIELDS",
    "MODE_FIELDS",
    "OrderableVariant",
    "PenaltyPoint",
    "PrintedNumber",
    "TransceiverDatasheet",
    "TransceiverSpecs",
]
