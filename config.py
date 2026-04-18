# config.py
# ─────────────────────────────────────────────────────────────────
# Central configuration for the HVAC Climate-and-Carbon Project
# (project pivoted 2026-04-18 from MPC framework → climate-and-
#  carbon emissions analysis; MPC config retained for nb 05_mpc_archive)
# Edit this file to change dataset paths, constants, or parameters
# ─────────────────────────────────────────────────────────────────
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────
PROJECT_ROOT  = Path(__file__).parent
DATA_RAW      = PROJECT_ROOT / "data"  / "raw"           # (unused; HDF5 fetched from S3)
DATA_PROCESSED= PROJECT_ROOT / "data"  / "processed"     # Local Parquet cache
DATA_EXTERNAL = PROJECT_ROOT / "data"  / "external"      # Grid carbon CSVs, retrofit cost refs
DATA_EGRID    = DATA_EXTERNAL / "egrid"                  # EPA eGRID 2022 CSV dumps
DATA_CAMBIUM  = DATA_EXTERNAL / "cambium"                # NREL Cambium 2023 hourly region CSVs
DOCS_DIR      = PROJECT_ROOT / "docs"                    # references.md and thesis aides
FIG_OUT       = PROJECT_ROOT / "figures"                 # Saved plots for the thesis

# ── Dataset location ──────────────────────────────────────────────
S3_PATH = "s3://oedi-data-lake/building_synthetic_dataset/A_Synthetic_Building_Operation_Dataset.h5"

# ── Unit conversion constants ─────────────────────────────────────
J_TO_KWH     = 1 / 3_600_000   # Joules → kilowatt-hours
AREA_M2      = 4_982.22        # Building floor area (m²)

# ── Dataset dimensions ────────────────────────────────────────────
CLIMATE_ZONES = {
    "1A": "Miami, FL (Hot/Humid)",
    "3C": "San Francisco, CA (Marine/Mild)",
    "5A": "Chicago, IL (Cold/Continental)",
}

EFFICIENCY_LEVELS = ["Low", "Standard", "High"]

# ── AMY years for climate-trend analysis (nb 05_climate_trends) ──
# Overlapping range across all 3 climates is 1988–2005 (see CLAUDE.md §Dataset).
# Six years spaced across the window give a 17-year temporal baseline.
AMY_YEARS_PIVOT = ["1988", "1990", "1996", "1997", "2004", "2005"]

# ── Grid-region mapping (climate zone → eGRID / Cambium subregion) ─
# Rationale documented in docs/references.md → [eGRID2022], [Cambium2023].
# Miami 1A → FRCC (Florida Reliability Coordinating Council).
# San Francisco 3C → CAMX (California WECC subregion).
# Chicago 5A → RFCW (Reliability First Corporation West — historical eGRID
#   subregion; modern Cambium ReEDS analogue is region P20 / PJMW).
GRID_REGIONS = {
    "1A": "FRCC",
    "3C": "CAMX",
    "5A": "RFCW",
}

# Modern Cambium ReEDS region fallback for Chicago (RFCW retired post-2020)
GRID_REGIONS_CAMBIUM = {
    "1A": "FRCC",
    "3C": "CAMX",
    "5A": "p20",   # PJMW equivalent in Cambium 2023 ReEDS
}

# ── Carbon pricing scenarios (£/tCO₂e, 2024 GBP) ──────────────────
# For MACC carbon-price sensitivity analysis (nb 07 §7).
# See docs/references.md → [UKGov2026-ETS], [HMT2023-GreenBook], [Rennert2022-SCC].
CARBON_PRICE_ETS_2026 = 49.41   # UK ETS civil-penalty price 2026     [UKGov2026-ETS]
CARBON_PRICE_GB_2022  = 248.0   # HMT Green Book central value 2022   [HMT2023-GreenBook]
CARBON_PRICE_GB_2050  = 378.0   # HMT Green Book central value 2050   [HMT2023-GreenBook]
CARBON_PRICE_SCC_USD  = 185.0   # Rennert 2022 Nature — 2020 USD/tCO₂ [Rennert2022-SCC]
GBP_PER_USD           = 0.79    # Illustrative FX (2024 avg). Update when needed.

# ── Retrofit asset life for MACC CAPEX annualisation ─────────────
# Conservative 25-year envelope of ASHRAE service-life database [ASHRAE2019-ServiceLife].
# Reciprocating chillers 20 yr, centrifugal 23 yr, boilers 25–30 yr, insulation 30+ yr.
ASSET_LIFE_YEARS = 25
DISCOUNT_RATE    = 0.035        # UK HMT Green Book social discount rate (real)

# ── Temporal settings ─────────────────────────────────────────────
TIMESTEP_MIN   = 10        # minutes per interval
HOURS_PER_DAY  = 24
STEPS_PER_DAY  = int(HOURS_PER_DAY * 60 / TIMESTEP_MIN)   # 144

# Operating hours: weekdays 07:00–20:00
OPS_HOUR_START = 7
OPS_HOUR_END   = 20

# ── Thermal comfort settings ─────────────────────────────────────
# Referenced by: nb 05_mpc_archive (legacy MPC), nb 07 (flexibility envelope
#                upper-bound check on comfort-preserving load-shift).
# Empirical HVAC-mode-gated comfort bands per (climate, season) are derived
# dynamically in nb 05_mpc_archive Section 3b and propagated into nb 07.
TEMP_SETPOINT_C    = 22.0  # Target indoor temperature (°C)
TEMP_COMFORT_LOW   = 20.0  # Lower comfort band (°C)
TEMP_COMFORT_HIGH  = 22.0  # Upper comfort band (°C)

# ── Plot style ────────────────────────────────────────────────────
CLIMATE_COLOURS = {
    "1A": "#E24B4A",   # Red  → Miami (hot)
    "3C": "#2E75B6",   # Blue → San Francisco (mild)
    "5A": "#639922",   # Green → Chicago (cold)
}

EFFICIENCY_COLOURS = {
    "Low":      "#E24B4A",
    "Standard": "#BA7517",
    "High":     "#639922",
}
