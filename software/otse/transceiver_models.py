"""Flat Pydantic model for optical-transceiver datasheet extraction."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


from typing import Literal


PenaltyParameter = Literal[
    "chromatic_dispersion_ps_nm",
    "pmd_ps",
    "pdl_db",
    "rx_osnr_db",
    "rx_power_dbm",
    "rx_sensitivity_dbm",
]

PenaltyTargetParameter = Literal[
    "rx_osnr_db",
    "rx_sensitivity_dbm",
    "path_penalty_db",
    "dispersion_penalty_db",
]



class PenaltyCondition(BaseModel):
    parameter: PenaltyParameter = Field(
        ...,
        description="Condition parameter: e.g. 'chromatic_dispersion_ps_nm', 'pmd_ps', 'pdl_db', 'rx_power_dbm'."
    )
    value: float = Field(..., description="Condition numeric threshold/value (e.g., 13000 for CD, -14.0 for Rx power).")

class PenaltyPoint(BaseModel):
    target_parameter: PenaltyTargetParameter = Field(
        default="rx_osnr_db",
        description="The parameter degraded: 'rx_osnr_db', 'rx_sensitivity_dbm', or 'path_penalty_db'."
    )
    penalty_db: float = Field(..., description="Penalty magnitude in dB (e.g. 0.5, 1.0).")
    penalized_value: Optional[float] = Field(
        default=None,
        description="Degraded parameter value if stated (e.g. 24.2 for 24.2 dB OSNR @ 0.5 dB penalty)."
    )
    conditions: list[PenaltyCondition] = Field(
        min_length=1,
        description="List of operating conditions under which this penalty occurs."
    )
    source: Optional[str] = Field(
        default=None,
        description="Where it was found: table section and row key (e.g. 'OpenZR+ | Appl mode=4'). Used for mode linking."
    )


class TransceiverSpecs(BaseModel):
    """Extract only explicitly stated values; use None when data is absent."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    #Module identification — vendor and part number
    vendor: Optional[str] = Field(None, description="Manufacturer/brand explicitly identified by this datasheet. Never invent or infer.")
    model: Optional[list[str]] = Field(None, description="Product model or orderable part number.")
    form_factor: list[str] | None = Field(default=None, description="Form factor of the transceiver: QSFP28, QSFP-DD, QSFP+, OSFP, CFP2-DCO, Front Panel Plug RJ, Low Rider RJ, SFF")
    standards_claimed: list[str] | None  = Field(
        default=None, description="MSA Standards claimed in the datasheet."
    )
    emitter_type: list[str] | None = Field(
        default=None,
        description="Type of optical emitter: DFB, FP, VCSEL, etc.",
    )
    photodetector_type: list[str] | None = Field(
        default=None,
        description="Type of optical photodetector: PIN, APD, etc.",
    )

    #Frequency and wavelength parameters
    wavelength_min_nm: Optional[List[float]] = Field(
        None, description="Minimum supported of optical wavelengths ranges in nm."
    )
    wavelength_max_nm: Optional[List[float]] = Field(
        None, description="Maximum supported optical wavelengths of ranges in nm."
    )
    wavelength_center_nm: Optional[List[float]] = Field(
        None, description="Nominal or center optical wavelengths of ranges in nm."
    )
    wavelength_band: list[str] | None = Field(
        default=None,
        description="spectrum bands:C-band, L-band, O-band, CWDM, LAN-WDM, grey, Super/Extended variants.",
    )
    frequency_min_thz: Optional[List[float]] = Field(
        None, description="Minimum supported optical frequency in THz."
    )
    frequency_max_thz: Optional[List[float]] = Field(
        None, description="Maximum supported optical frequency in THz."
    )
    channel_spacing_ghz: Optional[List[float]] = Field(
        default_factory=list, description="Supported or minimum channel spacing in GHz."
    )
    channel_total: List[int] | int | None = Field(
    default=None, description="Total number of channels supported."
    )
    
    #Physical parameters

    mounting_type: list[str] | None = Field(
                default=None,
                description="Type of mounting for the transceiver module. Pluggable, Socket, screw, solder, etc. It is not a form factor or MSA code.",
            )








    connector_type: list[str] | None = Field(
            default=None,
            description="Optical connector: LC, SC, MPO, FC, ST. It is not a form factor or MSA code.",
        )
    fiber_type:  list[str] | None = Field(
            default=None,
            description="Transmission media/fiber: SM/SMF, MMF, G.652/G.655.",
        )
    temp_min_c: float | None = Field(
            default=None,
            description="Min normal operating temperature in Celsius.",
        )
    temp_max_c: float | None = Field(
            default=None,
            description="Max normal operating temperature in Celsius.",
        )
    power_consumption_w: Optional[List[float]] = Field(
        default_factory=list, 
            description="Electrical Power consumption in Watts.",
        )


    # interface details (e.g., 400GAUI-8)
    host_interface_name: list[str] | None = Field(
        default=None,
        description="Host MSA code names as per MSA standards or vendor datasheet.",
    )

    host_interface_id_hex: list[str] | None = Field(
            default=None,
            description="Host Electrical Interface IDs in hexadecimal. Not Media codes",
        )

    host_interface_id: list[int] | None = Field(
            default=None,
            description="Host Electrical Interface id in decimals",
        )

    media_interface_name: list[str] | None = Field(
        default=None,
        description="Media MSA code names as per MSA standards or vendor datasheet.",
    )

    media_interface_id_hex: list[str] | None = Field(
            default=None,
            description="Media Interface IDs in hexadecimal. Not Host codes",
        )

    media_interface_id: Optional[List[int]] = Field(
            default=None,
            description="Media Interface id in decimals.",
        )
    frame: list[str] | None = Field(
        default=None, description="Frames or combination and multiples of frames: i.e. 8x 100GAUI-1"
    )
    standards_code: list[str] | None = Field(
        default=None, description="application code or profile or format related to any MSA, specifications, standards or vendor: openzr, openroadm, or specific application code"
    )

    # Electrical and optical performance parameters
    baud_rate_gbaud: Optional[List[float]] = Field(
        None, description="symbol/Signaling rates in GBaud."
    )
    bit_rate_gbps: Optional[List[float]] = Field(
        default_factory=list, description="data rate/speed/payload bit rate in Gbps or G. do not confuse with GHz or grid"
    )
    roll_off_percent: Optional[List[float]] = Field(
        None, description="Spectral roll-off factor in percent."
    )
    modulation_format: Optional[List[str]] = Field(
        default_factory=list, description="Supported modulation formats: NRZ, PAM, QPSK, 8QAM, 16QAM, 64QAM, etc."
    )
    reach_km: Optional[List[float]] = Field(
        default_factory=list, description="Maximum stated transmission reach in km."
    )
    tx_power_min_dbm: Optional[List[float]] = Field(
        None, description="Minimum transmitter output power in dBm."
    )
    tx_power_max_dbm: Optional[List[float]] = Field(
        None, description="Maximum transmitter output power in dBm. sometimes given with TX shaping"
    )
    tx_in_band_osnr_db: Optional[List[float]] = Field(
        None, description="Transmitter-generated in band OSNR in dB."
    )
    tx_out_of_band_osnr_db: Optional[List[float]] = Field(
        None, description="Transmitter-generated out of band OSNR in dB."
    )


    #Module-level RX capability envelope — worst-case hardware limits

    rx_sensitivity_dbm: Optional[List[float]] = Field(
        None, description="Minimum receiver power in dBm at the stated BER."
    )
    rx_osnr_db: Optional[List[float]] = Field(
        None, description="Required receiver OSNR threshold in dB."
    )

    rx_osnr_tolerance_db_max: Optional[List[float]] = Field(
        default=None,
        description="Max required OSNR for target BER in dB/0.1nm.",
    )

    rx_overload_dbm: Optional[List[float]] = Field(
        None, description="Maximum receiver input power in dBm before overload."
    )
    cd_tolerance_ps_nm: Optional[List[float]] = Field(
        None, description="Chromatic-dispersion tolerance or CDC in ps/nm."
    )
    pdl_db: Optional[List[float]] = Field(
        None, description="Polarization-dependent-loss tolerance in dB."
    )
    pmd_tolerance_ps: Optional[List[float]] = Field(
        None, description="PMD or DGD tolerance in ps."
    )



    # FEC configuration fields
    fec_type: Optional[List[str]] = Field(
        default_factory=list, description="Supported FEC types as stated: oFEC, C-FEC, RS-FEC, KP4, KP1, KP2, KP3, RS(528)"
    )
    fec_overhead_percent: Optional[List[float]] = Field(
        default_factory=list, description="FEC overhead in percent."
    )
    pre_fec_ber_threshold: Optional[List[float]] = Field(
         default_factory=list, description="Maximum correctable pre-FEC bit-error ratio."
    )
    post_fec_ber_target: Optional[List[float]] = Field(
        None, description="Target post-FEC bit-error ratio."
    )

    # ── Direct-detect only ────────────────────────────────────────────────────
    # These three are listed in MODE_FIELDS, so a datasheet may state one value
    # per mode; a scalar type would reject the whole record in that case.
    extinction_ratio_db: Optional[List[float]] = Field(
        default=None,
        description="Extinction ratio in dB.",
    )
    los_assert_dbm: Optional[List[float]] = Field(
        default=None,
        description="LOS (loss of signal) assert threshold in dBm.",
    )
    los_deassert_dbm: Optional[List[float]] = Field(
        default=None,
        description="LOS deassert threshold in dBm.",
    )
    channel_insertion_loss_db: Optional[List[float]] = Field(
        default=None,
        description="Channel insertion loss in dB.",
    )
    receiver_reflectance_db: Optional[List[float]] = Field(
        default=None,
        description="Receiver reflectance in dB.",
    )
    transmitter_reflectance_db: Optional[List[float]] = Field(
        default=None,
        description="Transmitter reflectance in dB.",
    )
    optical_extinction_ratio_db: Optional[List[float]] = Field(
        default=None,
        description="Optical extinction ratio in dB.",
    )
    optical_return_loss_tolerance_db: Optional[List[float]] = Field(
        default=None,
        description="Optical return loss tolerance in dB.",
    )
    number_of_lanes: Optional[List[int]] = Field(
        default=None,
        description="Number of lanes.",
    )
    side_mode_suppression_ratio_db: Optional[List[float]] = Field(
        default=None,
        description="Side Mode Suppression Ratio (SMSR) in dB.",
    )
    los_deassert_dbm: Optional[List[float]] = Field(
        default=None,
        description="LOS deassert threshold in dBm.",
    )
    los_assert_dbm: Optional[List[float]] = Field(
        default=None,
        description="LOS assert threshold in dBm.",
    )
    los_hysteresis_db: Optional[List[float]] = Field(
        default=None,
        description="LOS hysteresis in dB.",
    )
    total_jitter_ps: Optional[List[float]] = Field(
        default=None,
        description="Total jitter in ps.",
    )
    
    penalties: list[PenaltyPoint] | None = Field(
        default=None,
        description=(
            "Optical penalties (OSNR, RX sensitivity, dispersion, path, PDL) for given values of other parameters like RX power. "        ),
    )

    notes: Optional[str] = Field(
        None, description="Conditions, qualifiers, ambiguities, values trade-off dependencies, or source wording about any parameter that can not be explained in the set schema."
    )
    provenance_datasheet_sections: str | list[str] | None = Field(
        None, description="Comma-separated list of section headings (from the Section Headings list above) that contained the extracted parameters."
    )
    suggestions: Optional[str] = Field(
        None, description="Any suggestions for improving the extraction or schema."
    )
    

TransceiverDatasheet = TransceiverSpecs

__all__ = ["TransceiverSpecs", "TransceiverDatasheet"]

PENALTY_PARAMETERS: list[str] = [
    "cd_tolerance_ps_nm",
    "pmd_tolerance_ps",
    "pdl_db",
    "rx_osnr_db",
    "rx_sensitivity_dbm",
]

PENALTY_CONDITION_PARAMETERS: list[str] = [
    "rx_power_dbm",
    "rx_osnr_db",
]

FIELD_BUNDLES = {
    "identification": ["vendor", "model", "form_factor", "standards_claimed"],
    "interfaces": ["host_interface_name", "host_interface_id_hex", "media_interface_name", "media_interface_id_hex"],
    "wavelength": ["wavelength_min_nm", "wavelength_max_nm", "wavelength_center_nm", "wavelength_band", "channel_spacing_ghz"],
    "physical": ["connector_type", "fiber_type", "temp_min_c", "temp_max_c"],
    "electrical": ["baud_rate_gbaud", "bit_rate_gbps", "modulation_format"],
    "fec": ["fec_type", "fec_overhead_percent", "pre_fec_ber_threshold", "post_fec_ber_target"],
}

# Fields that participate in per-mode configuration (can have multiple correlated values)
MODE_FIELDS: list[str] = [
    "channel_spacing_ghz",
    "form_factor",
    "frequency_max_thz",
    "frequency_min_thz",
    "wavelength_band",
    "wavelength_center_nm",
    "wavelength_max_nm",
    "wavelength_min_nm",
    "channel_total",
    "model",
    "number_of_lanes",
    "baud_rate_gbaud",
    "bit_rate_gbps",
    "roll_off_percent",
    "modulation_format",
    "reach_km",
    "tx_power_min_dbm",
    "tx_power_max_dbm",
    "tx_in_band_osnr_db",
    "tx_out_of_band_osnr_db",
    "rx_sensitivity_dbm",
    "rx_osnr_db",
    "rx_osnr_tolerance_db_max",
    "rx_overload_dbm",
    "cd_tolerance_ps_nm",
    "pdl_db",
    "pmd_tolerance_ps",
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
    "power_consumption_w",
    "standards_code",
    "frame",
    "penalties",  # <-- Include penalties in MODE_FIELDS
]

MODE_FIELDS_OPT: list[str] = [
    "fec_type",
    "fec_overhead_percent",
]


# Fields that participate in per-mode configuration (can have multiple correlated values)
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


# Fields that participate in per-mode configuration (can have multiple correlated values)
STANDARDS_IMPLIED_FIELDS: list[str] = [
    "channel_spacing_ghz",
    "baud_rate_gbaud",
    "bit_rate_gbps",
    "modulation_format",
    "reach_km"
]