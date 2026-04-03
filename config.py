# config.py
# ─────────────────────────────────────────────────────────────────
# Central configuration for the HVAC Cooling Optimisation Project
# Edit this file to change dataset paths, constants, or parameters
# ─────────────────────────────────────────────────────────────────

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

# ── Temporal settings ─────────────────────────────────────────────
TIMESTEP_MIN   = 10        # minutes per interval
HOURS_PER_DAY  = 24
STEPS_PER_DAY  = int(HOURS_PER_DAY * 60 / TIMESTEP_MIN)   # 144

# Operating hours: weekdays 07:00–20:00
OPS_HOUR_START = 7
OPS_HOUR_END   = 20

# ── Thermal comfort settings (Phase 2 MPC) ───────────────────────
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
