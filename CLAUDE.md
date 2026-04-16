# Project Context for Claude Code
> This file gives Claude Code full context about this project.
> It was generated from the project's Claude.ai chat session.

---

## Project Identity

- **Title:** A Data-Driven Predictive Control Framework for HVAC Cooling Optimisation in Commercial Office Buildings
- **Note on scope:** While the title retains "cooling optimisation", the framework naturally generalises to full HVAC control (heating + cooling). `ElectricityHVAC` captures total HVAC electricity across all seasons. The ML model is trained on this full signal with no seasonal filtering, and the MPC controller manages total HVAC output across both heating and cooling regimes. Chicago (5A) winter performance demonstrates this generalisability.
- **Student:** Cheuk Fung Donald Man
- **Programme:** MEng Civil Engineering, Imperial College London
- **Supervisor:** Dr. Po-Heng Lee
- **Module:** 4th Year Individual Research Project
- **Submission:** 13th March 2026 (interim report done; thesis in progress)

---

## Project Overview

A two-phase research project using the AlphaBuilding Synthetic Building Operation Dataset to:

- **Phase 1** — Train a supervised ML model to predict total HVAC electricity demand (`hvac_kwh`) from outdoor air temperature (OAT), occupancy, and time features. The model is trained on the full signal — no seasonal filtering — so it learns both heating-season and cooling-season behaviour across all three climate zones.
- **Phase 2** — Use the trained ML model as the internal predictive engine inside a Model Predictive Control (MPC) framework. The controller minimises indoor temperature deviation from setpoint (22°C) by managing total HVAC output across both heating and cooling regimes. The cost function penalises temperature variance and total HVAC energy consumption.

**Key design decision:** `ElectricityHVAC` in EnergyPlus captures all HVAC electricity including fans, pumps, chillers, and electric heating components. Rather than filtering to cooling-only periods, the full signal is used for both ML training and MPC control. This produces a more honest, generalisable framework and makes Chicago's heating-dominated winters a meaningful test case rather than noise to be excluded.

The sustainability framing is central: buildings account for ~40% of global energy use, HVAC is the largest single end-use, and cooling demand is rising with climate change. This project targets SDG 7 (Clean Energy) and SDG 13 (Climate Action), and aligns with the UK Net Zero Strategy.

**Reinforcement Learning** is an optional extension — implement and compare against MPC only if time allows after Phase 2 is complete.

---

## Dataset

**AlphaBuilding Synthetic Building Operation Dataset**
- Generated via EnergyPlus / OpenStudio simulations of a U.S. DOE reference MediumOfficeDetailed building
- Floor area: 4,982 m²  |  Standard: ASHRAE 90.1-2013
- Publicly accessible on AWS S3 — **no credentials needed:**
  ```
  s3://oedi-data-lake/building_synthetic_dataset/A_Synthetic_Building_Operation_Dataset.h5
  ```
- Format: HDF5 — access via `h5py` + `s3fs`
- Always use `s3fs.S3FileSystem(anon=True)` — public bucket

**Dimensions:**
| Dimension | Values |
|-----------|--------|
| Climate zones | 1A (Miami), 3C (San Francisco), 5A (Chicago) |
| Efficiency levels | Low, Standard, High |
| Weather years | 30 AMY years per climate (ranges differ) + TMY3 reference. 1A: 1976–2005 · 3C: 1988–2017 · 5A: 1980–2009. Overlapping years available in all 3 climates: **1988–2005**. |
| Occupancy runs | run_1 to run_5 (stochastic) |
| Time resolution | 10-minute intervals (52,560 rows per annual simulation) |

**Key HDF5 variables:**
| Variable name | Description |
|---------------|-------------|
| `ElectricityHVAC` | HVAC electricity (J) ← **primary target** |
| `ElectricityFacility` | Total site electricity (J) |
| `GasFacility` | Natural gas (J) |
| `CoolingElectricity` | Cooling-only electricity (J) |
| `HeatingElectricity` | Heating-only electricity (J) |
| `SiteOutdoorAirDrybulbTemperature` | Outdoor air dry-bulb temperature (°C) |
| `SiteOutdoorAirWetbulbTemperature` | Outdoor air wet-bulb temperature (°C) |
| `ZoneMeanAirTemperature` | Per-zone indoor air temperature (°C) |
| `ZonePeopleOccupantCount` | Per-zone occupancy counts |
| `InteriorLightsElectricity` | Lighting electricity (J) |
| `InteriorEquipmentElectricity` | Plug loads / MELs (J) |
| `ZoneThermostatCoolingSetpointTemperature` | Cooling setpoints per zone (°C) |
| `ZoneThermostatHeatingSetpointTemperature` | Heating setpoints per zone (°C) |

**Unit conversion:** `J_TO_KWH = 1 / 3_600_000`

---

## Research Aims & Objectives

**Aim:** Develop a data-driven MPC framework for HVAC energy optimisation, using ML to predict total HVAC electricity demand and minimise indoor temperature fluctuation across all seasons and climate zones.

**Objectives:**
- O1. EDA to identify key drivers of total HVAC electricity (OAT, occupancy, time, season, efficiency level) across all 3 climate zones — including analysis of heating vs cooling season behaviour
- O2. Train & compare ML models (Random Forest, XGBoost, LSTM) on the full-year `hvac_kwh` signal with no seasonal filtering — metrics: RMSE, MAE, R²
- O3. Design MPC using the trained ML model as the predictive engine, minimising indoor temperature deviation from 22°C setpoint across both heating and cooling regimes
- O4. Evaluate MPC vs on/off baseline across all 3 climate zones and 3 efficiency levels, including heating-dominated (Chicago winter) and cooling-dominated (Miami summer) conditions
- O5. Quantify the trade-off between thermal comfort (temperature stability) and total HVAC energy consumption under the MPC framework
- O6. *(Optional — if time allows)* Implement a Reinforcement Learning control agent and compare its performance against the MPC framework using the same dataset, evaluation metrics, and climate zones

---

## Project Structure

```
hvac_project/
│
├── CLAUDE.md                        ← YOU ARE HERE — project context for Claude Code
├── config.py                        ← Central config (S3 path, constants, colours)
├── requirements.txt                 ← Python dependencies
├── README.md                        ← Setup instructions
│
├── notebooks/
│   ├── A_Synthetic_Operation_Dataset.ipynb  ← Original AlphaBuilding demo notebook
│   ├── AlphaBuilding_README.md              ← Original dataset README
│   ├── 01_load_data.ipynb           ← Environment check, S3 connection, data loading ✓ (incl. 81-sim multi-year loader)
│   ├── 02_eda.ipynb                 ← Exploratory data analysis ✓
│   ├── 03_features.ipynb            ← Feature engineering ✓ (v1 + v2 outputs)
│   ├── 04_ml_model.ipynb            ← ML model training & evaluation ✓ (v1 + v2 sections)
│   ├── 05_mpc.ipynb                 ← MPC framework (TO BUILD)
│   └── 06_rl.ipynb                  ← RL agent & MPC comparison — OPTIONAL (TO BUILD)
│
├── data/
│   └── processed/                   ← Locally cached Parquet files (gitignored)
│
└── figures/                         ← Saved plots for the thesis
```

---

## Workflow

- **Claude Code** — all code writing, editing, debugging, building new notebooks, analysis
- **VS Code** — running notebooks, viewing plots, browsing files
- Claude Code has full autonomy to read, create, and edit files in this project
- Always update `CLAUDE.md` when significant decisions, findings, or status changes occur

### config.py
Import at the top of any notebook that needs shared constants:
```python
import sys; sys.path.append('..')
from config import *
```
Contains: `S3_PATH`, `J_TO_KWH`, `CLIMATE_ZONES`, `EFFICIENCY_LEVELS`, `CLIMATE_COLOURS`, `EFFICIENCY_COLOURS`, `TEMP_SETPOINT_C` (22°C), `TEMP_COMFORT_LOW` (20°C), `TEMP_COMFORT_HIGH` (22°C)

### Notebooks are self-contained
Each notebook defines its own `load_simulation()` function and constants inline.
`data_loader.py` has been removed — do not reference it.

The standard DataFrame columns produced by `load_simulation()` are:
`hvac_kwh, total_kwh, gas_kwh, lighting_kwh, plugloads_kwh, cooling_kwh, heating_kwh, oat_c, wetbulb_c, indoor_temp_c, occupancy, hour, minute, dayofweek, month, is_weekday, is_occupied, oat_roll1h, oat_roll3h, climate, efficiency, year, run`

Note: `season` is derived in notebooks via `month` mapping (Dec/Jan/Feb → Winter, etc.) and is not produced by `load_simulation()` directly.

---

## Python Stack

| Library | Purpose |
|---------|---------|
| `pandas`, `numpy` | Data manipulation |
| `h5py`, `s3fs` | HDF5 / S3 access |
| `scikit-learn`, `xgboost` | ML models (Phase 1) |
| `tensorflow` / `keras` | LSTM (Phase 1) |
| `scipy` | MPC optimisation (Phase 2) |
| `matplotlib`, `seaborn` | Visualisation |
| `tqdm` | Progress bars |
| `pyarrow` | Parquet file support |

Python version: 3.9 | Virtual environment: `venv/` in project root

---

## Thesis Chapter Plan

| Chapter | Title |
|---------|-------|
| 1 | Introduction |
| 2 | Literature Review |
| 3 | Dataset and Exploratory Data Analysis |
| 4 | ML Model for Total HVAC Demand Prediction |
| 5 | Model Predictive Control Framework |
| 6 | Results and Evaluation |
| 7 | *(Optional)* Reinforcement Learning Agent & Comparison with MPC |
| 8 | Discussion |
| 9 | Conclusions and Future Work |

---

## Current Status

- [x] Interim report submitted (13 March 2026)
- [x] Project structure built
- [x] `01_load_data.ipynb` — complete. 3 Parquet files saved:
  - `TMY3_1A_Standard_run_1.parquet`
  - `TMY3_3C_Standard_run_1.parquet`
  - `TMY3_5A_Standard_run_1.parquet`
- [x] `02_eda.ipynb` — complete. 15 figures saved to `figures/`
- [x] `03_features.ipynb` — complete. Single-year (v1) + 81-sim expanded (v2) feature matrices saved
- [x] `04_ml_model.ipynb` — complete. v1 (TMY3) + v2 (81-sim) models trained and saved
- [ ] `05_mpc.ipynb` — **current step**
- [ ] `06_rl.ipynb` — optional, if time allows
- [ ] Thesis write-up

---

## Key Decisions & Findings So Far

### ElectricityHVAC is a mixed signal
`hvac_kwh` captures total HVAC electricity — heating + cooling + fans + pumps. It is NOT cooling-only. Chicago (5A) shows large spikes in January/February due to heating load — this is expected and valid, not an error.

### Decision: train on full signal, no seasonal filtering
Both the ML model (Phase 1) and MPC controller (Phase 2) use the full `hvac_kwh` signal across all seasons. No OAT filtering is applied. This makes the framework more general and makes Chicago's winter a meaningful test case rather than noise to exclude.

### MPC controls full HVAC — heating and cooling
The MPC cost function minimises deviation from the 22°C setpoint regardless of season. In summer it reduces cooling; in winter it manages heating. The controller works in both regimes.

### Parquet files saved (Standard efficiency, TMY3, run_1)
- `TMY3_1A_Standard_run_1.parquet` — Miami
- `TMY3_3C_Standard_run_1.parquet` — San Francisco
- `TMY3_5A_Standard_run_1.parquet` — Chicago

Each file contains all columns including the newer `indoor_temp_c`, `cooling_kwh`, `heating_kwh`. Load efficiency comparison data separately if needed (Low/High efficiency not yet saved).

### EDA key findings (notebook 02)
- **OAT is the strongest predictor** of `hvac_kwh` across all 3 climate zones
- **Miami (1A)** has the highest annual HVAC load — cooling-dominated year-round
- **Chicago (5A)** has dual peaks: summer cooling + winter heating — confirms mixed signal
- **San Francisco (3C)** has the lowest and flattest HVAC demand — mild marine climate
- **Occupancy has a moderate positive correlation** with HVAC demand during occupied hours
- **Indoor temperature** tracks close to 22°C setpoint in most conditions; largest drift occurs in Chicago winters
- Comfort band updated to **23–24°C** (setpoint 23.5°C midpoint); prior 20–22°C band retired

### Feature engineering outputs (notebook 03)

**v1 — single year (TMY3, Standard, run_1, 3 climates):**
- `features_train.parquet` (110,073 rows), `features_val.parquet` (23,586), `features_test.parquet` (23,589)
- `scaler_X.pkl` — StandardScaler for 20 continuous X features (fit on train only)
- `scaler_y.pkl` — StandardScaler for `hvac_kwh`; mean=3.72 kWh, scale=3.91 kWh
- `feature_sets.json` — FULL_FEATURES (31 cols), MPC_FEATURES (29 cols), metadata
- Split: 70/15/15 temporal per climate; train 2006-01-02→09-13, val →11-07, test →12-31

**v2 — 81-simulation expanded dataset:**
- `multi_year_raw.parquet` — 4,257,960 rows, 24 columns (raw combined)
- `features_train_v2.parquet`, `features_val_v2.parquet`, `features_test_v2.parquet`
- `scaler_X_v2.pkl`, `scaler_y_v2.pkl`
- `feature_sets_v2.json` — FULL_FEATURES_V2 (34 cols), MPC_FEATURES_V2 (32 cols)
- Split: year-level (train=1990+1997, val=2004 Jan–Jun, test=2004 Jul–Dec)

**Feature sets:**
- `FULL_FEATURES` (31) / `FULL_FEATURES_V2` (34): includes `lighting_kwh`, `plugloads_kwh`, `wetbulb_c`, `wetbulb_dev` + efficiency OHE (v2 only)
- `MPC_FEATURES` (29) / `MPC_FEATURES_V2` (32): excludes plug loads & lighting — forecastable inputs only

**Engineered features:** `hour_sin/cos`, `month_sin/cos`, `dow_sin/cos`, `hvac_lag1/6/144`, `hvac_roll1h/24h`, `oat_dev`, `wetbulb_dev`, `indoor_dev`, `oat_sq`, `climate_1A/3C/5A`, `efficiency_High/Low/Standard` (v2 only)

**Key results from running notebook 03:**
- OAT ranges confirmed: 1A [5.0, 35.6]°C · 3C [2.2, 32.8]°C · 5A [-22.8, 35.0]°C
- `oat_dev` range [-44.8, +13.6]°C — Chicago winter (-22.8°C) is 44.8° below setpoint; Miami peaks only 13.6° above
- `wetbulb_dev` range [-45.2, +4.9]°C — wetbulb never far above setpoint (expected: wetbulb ≤ drybulb always)
- `indoor_dev` range [-6.4, +4.4]°C — largest undershoot in Chicago winters (heating struggles to reach 22°C)
- Top features by |Pearson r| with `hvac_kwh`: hvac_roll1h (0.951) > hvac_lag1 (0.930) > hvac_lag6 (0.833) > hvac_lag144 (0.778) > plugloads_kwh (0.596, full only) > lighting_kwh (0.580, full only) > hour_cos (0.575) > is_occupied (0.541) > occupancy (0.531) > oat_sq (0.485)
- Autoregressive features dominate — strong HVAC thermal inertia confirmed
- `oat_sq` ranking at 0.485 confirms U-shaped HVAC-OAT relationship across climates

### ML model results — v1: single year (notebook 04, Part 1)
Saved to `data/processed/`: `model_rf.pkl`, `model_xgb.pkl`, `model_lstm.keras`, `model_results.json`
Dataset: TMY3 × Standard efficiency × run_1 × 3 climates. Split: 70/15/15 temporal.

| Model | Val RMSE | Val R² | Test RMSE | Test R² |
|-------|----------|--------|-----------|---------|
| Persistence baseline | 1.365 kWh | 0.843 | 1.357 kWh | 0.868 |
| Random Forest (500 trees) | 0.225 kWh | 0.9957 | 0.345 kWh | 0.9915 |
| **XGBoost** | **0.230 kWh** | **0.9956** | **0.340 kWh** | **0.9917** |
| LSTM | 0.290 kWh | 0.9929 | 1.532 kWh | 0.832 |

**Best model v1: XGBoost** (test RMSE = 0.340 kWh, R² = 0.9917) — ~75% RMSE reduction over baseline.
- LSTM val→test collapse: overfits to seasonal training distribution; tree models more robust to temporal shift.
- LOOKBACK = 24 steps (4h) for LSTM sequences, created per climate to avoid zone bleed.
- v1 outputs preserved for thesis documentation (LSTM comparison rationale).

### ML model results — v2: 81-simulation expanded dataset (notebook 04, Part 2)
Saved to `data/processed/`: `model_rf_v2.pkl`, `model_xgb_v2.pkl`, `model_results_v2.json`
Dataset: 3 AMY years (1990, 1997, 2004) × 3 runs × 3 efficiency levels × 3 climates = 81 simulations (~4.25M rows).
Split: year-level — train on 1990+1997, val on 2004 Jan–Jun, test on 2004 Jul–Dec.
Features: FULL_FEATURES_V2 = 34 (adds efficiency_High, efficiency_Low, efficiency_Standard OHE).
LSTM excluded — 4M sequences × (24, 34) float32 ≈ 13 GB RAM; infeasible on MacBook.

| Model | Val RMSE | Val R² | Test RMSE | Test R² |
|-------|----------|--------|-----------|---------|
| Random Forest (300 trees) | 0.2738 kWh | 0.9957 | 0.1859 kWh | 0.9979 |
| XGBoost (1000 rounds, lr=0.05) | 0.3049 kWh | 0.9947 | 0.2441 kWh | 0.9964 |
| **XGBoost (3000 rounds, lr=0.05)** | **0.2744 kWh** | **0.9957** | **0.2114 kWh** | **0.9973** |

**Selected for MPC: XGBoost (3000 rounds)**
- RF has lower test RMSE (0.1859 vs 0.2114) but is dominated by autoregressive lag features — produces flat optimisation landscape in MPC.
- XGBoost distributes importance across OAT, occupancy, time features — physically meaningful, gives MPC controller actionable gradients.
- XGBoost did not converge within 3000 rounds (best_iteration=2999) — val RMSE (0.2744) now matches RF (0.2738); remaining test gap is a tuning issue not a model limitation.
- Both models achieve R² > 0.997 — highly accurate HVAC demand prediction across all climates and efficiency levels.

**Per-climate test RMSE (Random Forest v2):**
| Climate | RMSE | MAE | R² |
|---------|------|-----|----|
| 1A Miami | 0.2181 kWh | 0.0748 kWh | 0.9979 |
| 3C San Francisco | 0.1336 kWh | 0.0559 kWh | 0.9966 |
| 5A Chicago | 0.1955 kWh | 0.0767 kWh | 0.9977 |

**Per-efficiency test RMSE (Random Forest v2):**
| Efficiency | RMSE | MAE | R² |
|------------|------|-----|----|
| Low | 0.2574 kWh | 0.0939 kWh | 0.9971 |
| Standard | 0.1518 kWh | 0.0636 kWh | 0.9984 |
| High | 0.1198 kWh | 0.0500 kWh | 0.9984 |

**Key v2 design decisions:**
- Efficiency OHE added as explicit feature — model learns Low/Standard/High differences directly
- Lag/rolling features computed per (climate, efficiency, run, year) group — prevents cross-simulation bleed
- RF reduced to 300 trees (from 500) to keep training time feasible on 2.8M rows
- XGBoost: same hyperparameters, early stopping on val set; hit 999/1000 rounds — no early stop triggered
- `get_efficiency()` helper reconstructs efficiency label from OHE for per-efficiency breakdown
- **MPC (notebook 05) will use**: `model_xgb_v2.pkl` + `MPC_FEATURES_V2` (32 features) — XGBoost selected for MPC due to more physically distributed feature importance

- Always use `anon=True` in `s3fs.S3FileSystem()` — the S3 bucket is public
- Never hardcode the S3 path — use `S3_PATH` from `config.py`
- Raw HDF5 energy variables are in **Joules** — always convert with `J_TO_KWH`
- Target variable for ML is `hvac_kwh` — this is **total HVAC electricity** (heating + cooling combined), not cooling only. Never filter to cooling-season only for ML training.
- `hvac_kwh` spikes in Chicago (5A) during winter are expected and valid — they reflect heating-season HVAC load, not errors
- MPC controls total HVAC output across all seasons — cost function minimises temperature deviation from **22°C setpoint** and total HVAC energy
- Thermal comfort band is **23–24°C** (setpoint 23.5°C) — applies year-round for both heating and cooling
- Use `CLIMATE_COLOURS` and `EFFICIENCY_COLOURS` from `config.py` for all plots
- Save all figures to `figures/` with descriptive names (e.g. `02_correlation_heatmap.png`)
- Save processed data as **Parquet** to `data/processed/` — never commit raw HDF5 to git
- Add `data/processed/` to `.gitignore`
