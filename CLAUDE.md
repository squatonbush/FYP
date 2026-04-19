# Project Context for Claude Code
> This file gives Claude Code full context about this project.
> It was generated from the project's Claude.ai chat session.

---

## Project Identity

- **Title:** A Data-Driven Predictive Control Framework for HVAC Cooling Optimisation in Commercial Office Buildings
- **Note on scope (pivoted 2026-04-18):** The thesis title was set at proposal stage referencing cooling-control optimisation. During execution the scope pivoted from control-framework design to a **three-lever climate-and-carbon emissions analysis**: (i) climate-change contribution to HVAC demand via 18-year AMY data, (ii) retrofit marginal-abatement-cost curve across ASHRAE efficiency levels, (iii) grid-aware carbon-optimal scheduling using thermal-mass flexibility overlaid with NREL Cambium hourly grid carbon. The MPC exploration is retained as archived material at `notebooks/05_mpc_archive.ipynb` and is referenced in the Chapter 8 Limitations section; the research contribution is the three-lever analysis. Literature gap justification: Péan et al (2019) *J. Process Control* identify carbon-signal objectives as under-served in HVAC control — see `[Pean2019]` in `docs/references.md`.
- **Student:** Cheuk Fung Donald Man
- **Programme:** MEng Civil Engineering, Imperial College London
- **Supervisor:** Dr. Po-Heng Lee
- **Module:** 4th Year Individual Research Project
- **Submission:** 13th March 2026 (interim report done; thesis in progress)

---

## Project Overview

A two-phase research project using the AlphaBuilding Synthetic Building Operation Dataset.

**Phase 1 — ML demand predictor (unchanged, complete).** Train a supervised ML model to predict total HVAC electricity demand (`hvac_kwh`) from outdoor air temperature (OAT), occupancy, and time features. The model is trained on the full signal — no seasonal filtering — so it learns both heating-season and cooling-season behaviour across all three climate zones. Delivered in notebooks 01–04; `model_xgb_v2.pkl` (R² = 0.9973 on 81-simulation multi-year dataset) is the scenario-exploration engine for Phase 2.

**Phase 2 — Three-lever climate-and-carbon analysis (pivoted 2026-04-18).** Use the ML predictor as a counterfactual engine over the AMY + efficiency-level design space, and overlay public hourly grid carbon intensity to quantify and compare three complementary decarbonisation pathways across Miami 1A, San Francisco 3C and Chicago 5A:

- **(a) Climate-change contribution** — 18-year AMY longitudinal analysis (1988–2005 overlapping window, 6 years × 3 climates × 3 efficiency levels) to quantify CDD/HDD sensitivity and warming-attributable demand. Delivered in `notebooks/05_climate_trends.ipynb`.
- **(b) Regional grid carbon overlay** — EPA eGRID 2022 annual subregion factors + NREL Cambium 2023 hourly long-run marginal emissions rate (LRMER). Climate → subregion: 1A→FRCC, 3C→CAMX, 5A→RFCW (historical) / p20 (modern ReEDS). Delivered in `notebooks/06_grid_carbon.ipynb`.
- **(c) Carbon-optimal operational scheduling** — thermal-mass flexibility envelope (RC model salvaged from archived nb 05) overlaid with hourly LRMER; rule-based shift of load from high-carbon to low-carbon windows without comfort violation. Delivered in `notebooks/07_carbon_optimisation.ipynb`.
- **(d) Retrofit MACC under UK carbon pricing** — marginal abatement cost curve for Low→Standard→High upgrades per climate under UK ETS (£49.41/tCO₂e, 2026), HMT Green Book (£248/tCO₂e, 2022; £378/tCO₂e, 2050) and Rennert SCC ($185/tCO₂). Delivered in `notebooks/07_carbon_optimisation.ipynb` Sections 5–7.

**Literature-gap justification.** Péan, Salom & Costa-Castelló (2019) *J. Process Control* review of HVAC control strategies finds that CO₂-signal objectives are rare in the control literature, which is dominated by economic/price objectives. This pivot targets that under-served gap. The MPC exploration is archived at `notebooks/05_mpc_archive.ipynb` and retained only as Chapter 8 Limitations material — closed-loop validation on synthetic data cannot produce a research claim that generalises to real buildings, because the dominant real-world failure modes (forecast error, model-plant mismatch, actuator drift, occupant divergence) are eliminated by construction.

**Framing statistics (all cited in `docs/references.md`).** Buildings = 31% of global final energy + 21% of GHG emissions, cooling grew ~75% 1990–2019 (`[IPCC_AR6_Ch9]`); global cooling demand triples by 2050 (`[IEA2018_FoC]`); climate change alone lifts energy demand 25–58% by 2050 (`[VanRuijven2019]`); US per +1 °C warming lifts CDD₁₈ ~20%, cuts HDD₁₈ ~10% (`[Petri2015]`); commercial pre-cooling can shift up to 51% of daily cooling load off-peak (`[Braun1990]`); US Grid-Interactive Efficient Buildings can deliver ~80 Mt CO₂/yr by 2030, ~6% of US power-sector emissions (`[Satchwell2021]`).

The sustainability framing is central: buildings and HVAC dominate operational emissions, and the interaction between climate-driven demand, retrofit, and grid-aware operation is the quantitative question the thesis answers. Project targets SDG 7 (Clean Energy) and SDG 13 (Climate Action), and aligns with UK Net Zero and the IEA *Net Zero by 2050* retrofit trajectory.

**Reinforcement Learning** is no longer part of the scope. If mentioned in the thesis, it appears only in Chapter 9 Future Work.

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

**Aim (pivoted 2026-04-18):** Quantify and compare three complementary decarbonisation pathways for commercial office HVAC — building retrofit, climate-resilient design, and grid-aware operational scheduling — across three US climate zones, using a machine-learning demand predictor as a counterfactual-scenario engine and real regional grid carbon data.

**Objectives:**
- **O1** — EDA of HVAC drivers across climates and efficiency levels (delivered in `notebooks/02_eda.ipynb`; minor CDD/HDD extension for nb 05).
- **O2** — Train an ML model that generalises HVAC demand prediction across climate × efficiency × weather year (delivered in `notebooks/04_ml_model.ipynb`; XGBoost v2 retained as the scenario engine — test R² = 0.9973 on 81-simulation panel).
- **O3** — Quantify the climate-change contribution to HVAC demand using 6 AMY years across the overlapping 1988–2005 window; compute climate sensitivity (β_CDD, β_HDD per climate × efficiency) and warming-attributable demand (counterfactual: 2005 weather applied to same building as 1988 weather). Delivered in `notebooks/05_climate_trends.ipynb`.
- **O4** — Ingest public regional grid carbon intensity profiles (EPA eGRID 2022 annual, NREL Cambium 2023 hourly LRMER); compute hourly building CO₂e emissions per archetype (3 climates × 3 efficiency levels) for 2004; diagnose peak-coincidence between HVAC demand and grid carbon. Delivered in `notebooks/06_grid_carbon.ipynb`.
- **O5** — Derive a thermal-mass flexibility envelope per climate using the RC model salvaged from archived nb 05; quantify carbon-optimal load-shift potential without comfort violation via a rule-based scheduling heuristic overlaid on Cambium hourly LRMER. Delivered in `notebooks/07_carbon_optimisation.ipynb` Sections 2–4.
- **O6** — Build a retrofit MACC across Low→Standard→High efficiency rungs per climate under UK carbon-pricing scenarios (ETS 2026 £49.41, Green Book £248–378, Rennert SCC $185); compare retrofit-only vs schedule-only vs combined scenarios; carbon-price sensitivity sweep. Delivered in `notebooks/07_carbon_optimisation.ipynb` Sections 5–7.

The MPC Objectives O3–O5 and the optional RL O6 from the pre-pivot framing are archived together with `notebooks/05_mpc_archive.ipynb` and referenced in thesis Chapter 8 Limitations. RL is not in the current scope.

---

## Project Structure

```
hvac_project/
│
├── CLAUDE.md                        ← YOU ARE HERE — project context for Claude Code
├── config.py                        ← Central config (paths, grid regions, carbon prices, colours)
├── requirements.txt                 ← Python dependencies
├── README.md                        ← Setup instructions
│
├── notebooks/
│   ├── A_Synthetic_Operation_Dataset.ipynb  ← Original AlphaBuilding demo notebook
│   ├── AlphaBuilding_README.md              ← Original dataset README
│   ├── 01_load_data.ipynb           ← S3 connection, data loading ✓ (to extend for 1988, 1996, 2005 AMY)
│   ├── 02_eda.ipynb                 ← Exploratory data analysis ✓
│   ├── 03_features.ipynb            ← Feature engineering ✓ (v1 + v2 outputs)
│   ├── 04_ml_model.ipynb            ← ML model training & evaluation ✓ (v1 + v2 sections)
│   ├── 05_climate_trends.ipynb      ← Climate-change contribution to HVAC demand (NEW — O3)
│   ├── 06_grid_carbon.ipynb         ← Grid carbon overlay + baseline emissions (NEW — O4)
│   ├── 07_carbon_optimisation.ipynb ← Flexibility envelope + retrofit MACC + scenarios (NEW — O5, O6)
│   └── 05_mpc_archive.ipynb         ← ARCHIVED (renamed from 05_mpc.ipynb on pivot; Ch.8 Limitations only)
│
├── data/
│   ├── processed/                   ← Locally cached Parquet, JSON, pickles (gitignored)
│   │                                   — multi_year_raw.parquet, features_*_v2.parquet, model_xgb_v2.pkl,
│   │                                     ml_dynamics_{1A,3C,5A}.pkl (archived), mpc_results.json (archived),
│   │                                     + NEW: multi_year_{1988,1996,2005}_*.parquet,
│   │                                            emissions_baseline.parquet, grid_profiles.parquet,
│   │                                            flexibility_envelope.json, macc_table.csv,
│   │                                            scenario_comparison.json, scheduling_results.parquet
│   └── external/                    ← Public third-party data (NEW)
│       ├── egrid/                   ← EPA eGRID 2022 CSV dumps
│       └── cambium/                 ← NREL Cambium 2023 hourly LRMER CSVs per region
│
├── docs/
│   └── references.md                ← Canonical thesis bibliography (40 refs, 3 pillars) — NEW
│
└── figures/                         ← Saved plots for the thesis
    (05_*.png archived MPC figures retained on disk, un-linked from new narrative.
     New: 05_cdd_hdd_trends.png, 05_climate_sensitivity.png, 05_warming_counterfactual.png,
          06_hourly_carbon_profiles.png, 06_emissions_matrix.png, 06_peak_coincidence.png,
          07_flexibility_envelope.png, 07_shift_per_climate.png, 07_macc_per_climate.png,
          07_scenario_comparison.png, 07_carbon_price_sensitivity.png.)
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
Contains:
- **Paths:** `PROJECT_ROOT`, `DATA_RAW`, `DATA_PROCESSED`, `DATA_EXTERNAL`, `DATA_EGRID`, `DATA_CAMBIUM`, `DOCS_DIR`, `FIG_OUT`
- **Core constants:** `S3_PATH`, `J_TO_KWH`, `AREA_M2` (4982.22 m²), `CLIMATE_ZONES`, `EFFICIENCY_LEVELS`
- **AMY panel:** `AMY_YEARS_PIVOT` = `["1988","1990","1996","1997","2004","2005"]`
- **Grid mapping:** `GRID_REGIONS` (historical eGRID — 1A→FRCC, 3C→CAMX, 5A→RFCW), `GRID_REGIONS_CAMBIUM` (modern ReEDS — 5A→p20)
- **Carbon pricing (£/tCO₂e, 2024 GBP):** `CARBON_PRICE_ETS_2026` (49.41), `CARBON_PRICE_GB_2022` (248.0), `CARBON_PRICE_GB_2050` (378.0), `CARBON_PRICE_SCC_USD` (185.0), `GBP_PER_USD` (0.79)
- **MACC annualisation:** `ASSET_LIFE_YEARS` (25), `DISCOUNT_RATE` (0.035 UK HMT social discount rate)
- **Temporal:** `TIMESTEP_MIN` (10), `HOURS_PER_DAY`, `STEPS_PER_DAY` (144), `OPS_HOUR_START` (7), `OPS_HOUR_END` (20)
- **Comfort (archived MPC legacy + nb 07 upper-bound check):** `TEMP_SETPOINT_C` (22°C), `TEMP_COMFORT_LOW` (20°C), `TEMP_COMFORT_HIGH` (22°C)
- **Plot style:** `CLIMATE_COLOURS`, `EFFICIENCY_COLOURS`

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
| `h5py`, `s3fs` | HDF5 / S3 access to AlphaBuilding |
| `scikit-learn`, `xgboost` | ML models (Phase 1) |
| `tensorflow` / `keras` | LSTM (Phase 1, v1 only) |
| `scipy` | Linear regression, optimisation (nb 05 sensitivity regression, nb 07 MACC; archived MPC optimiser) |
| `statsmodels` | Time-series trend detection (nb 05) |
| `matplotlib`, `seaborn` | Visualisation |
| `tqdm` | Progress bars |
| `pyarrow` | Parquet file support |

Python version: 3.9 | Virtual environment: `venv/` in project root

---

## External Data Sources (Phase 2)

All public, free, no credentials required. See `docs/references.md` for full citations.

| Source | Format | Use | Short-key | Local path |
|--------|--------|-----|-----------|------------|
| EPA eGRID 2022 | CSV (annual by subregion) | Annual-average grid CO₂e factors for baseline emissions accounting | `[eGRID2022]` | `data/external/egrid/` |
| NREL Cambium 2023 | CSV (8760 hourly per region × scenario) | Hourly long-run marginal emissions rate (LRMER) for time-of-use carbon optimisation | `[Cambium2023]`, `[LRMER2023]` | `data/external/cambium/` |
| UK HMT Green Book 2023 update | PDF reference | Social cost of carbon (£248/tCO₂e 2022 → £378/tCO₂e 2050) | `[HMT2023-GreenBook]` | referenced in `config.py` constants |
| UK ETS 2026 civil-penalty price | Web reference | Market carbon price (£49.41/tCO₂e) | `[UKGov2026-ETS]` | referenced in `config.py` constants |
| Rennert 2022 SCC | Nature article | US$185/tCO₂ central SCC — benchmark for cost-effectiveness thresholds | `[Rennert2022-SCC]` | referenced in `config.py` constants |
| EPA 2023 SC-GHG | Report | US$190/tCO₂ (2020) central SCC — regulatory-grade | `[EPA2023-SCGHG]` | — |
| PNNL 90.1-2013 cost-effectiveness | Tech report | Primary retrofit-cost source for MACC x-axis | `[Hart2015-PNNL]` | literature-only |
| ASHRAE service-life database | Web | Asset-life assumption (25 yr conservative) for CAPEX annualisation | `[ASHRAE2019-ServiceLife]` | literature-only |

**Climate → grid-subregion mapping:**
- 1A Miami → **FRCC** (Florida Reliability Coordinating Council, gas-dominated, flat diurnal profile expected)
- 3C San Francisco → **CAMX** (California WECC subregion, solar-heavy — pronounced midday trough + evening ramp)
- 5A Chicago → **RFCW** (historical eGRID — Reliability First Corporation West, retired post-2020) / **p20** (modern Cambium ReEDS region — PJMW analogue, coal transitioning)

Raw CSV files are committed under `data/external/` (< 50 MB total) with pinned download dates. The archival commit also records the eGRID 2022 schema and Cambium 2023 scenario choice (mid-case baseline; high-renewables + low-renewables retained for future-projection extension).

---

## Literature / Reference Library Workflow

The canonical thesis bibliography lives at `docs/references.md` — 40 curated references across three pillars (climate impact on buildings, grid carbon intensity and demand response, retrofit MACC and carbon pricing).

**Rules:**
1. Every numeric claim in a notebook markdown cell or thesis chapter cites a short-key from `docs/references.md` — e.g. `[IPCC_AR6_Ch9]`, `[Pean2019]`, `[Braun1990]`.
2. When a new source is introduced during implementation, add it to `docs/references.md` **in the same commit** as the code/chapter that uses it.
3. Short-key format: `[FirstAuthorLastNameYYYY]` or `[Org-YYYY-Topic]` (e.g. `[UKGov2026-ETS]`).
4. Every entry must contain: full citation (authors, year, title, venue), stable URL/DOI, the exact quantitative finding being cited, and the notebook/chapter where it is used.
5. Entries tagged `[needs verification]` must be re-checked against the primary source before quoting in the final thesis. Current flags: `[Petri2015]` exact %, `[Braun1990]` 40%/51% (primary ASHRAE Transactions PDF paywalled), `[IPCC_AR6_Ch9]` cooling-growth figure, `[Huang2016]` page range, `[Neukomm2019]` flexibility-MW figures.

**Reference-to-notebook mapping** (see `docs/references.md` for the full table): nb 05 pulls from Pillar A (Isaac2009, VanRuijven2019, Dirks2015, EPA2021_CDD, Petri2015, Sailor2003, DayGD2017, Biardeau2020, Santamouris2014); nb 06 pulls from Pillar B core (eGRID2022, Cambium2023, LRMER2023, SilerEvans2012, Ryan2016, Hawkes2010); nb 07 pulls from Pillar B flexibility (Braun1990, Reynders2017, Pean2019, Arteconi2012, Neukomm2019, Satchwell2021, Radovanovic2021) and Pillar C (Hart2015-PNNL, McKinsey2009-MACC, Kesicki2012, Huang2016, PradaHernandez2015, HMT2023-GreenBook, UKGov2026-ETS, Rennert2022-SCC, EPA2023-SCGHG, Ma2012-RetrofitReview, Chidiac2011, Rockefeller2012, Wilson2022-ComStock, ASHRAE2019-ServiceLife).

---

## Thesis Chapter Plan

| Ch | Title | Source | Role in narrative |
|----|-------|--------|-------------------|
| 1 | Introduction | rewrite | Buildings 31% energy + 21% GHG → HVAC largest end-use → three levers (climate adaptation, retrofit, grid-aware operation) → research question |
| 2 | Literature Review | rewrite | Building decarbonisation, climate-impact-on-buildings, grid carbon dynamics, demand-side flexibility, MACC methodology — integrated treatment is the gap |
| 3 | Dataset and Exploratory Data Analysis | existing nb 02 | AlphaBuilding overview; climate × efficiency × AMY coverage; key HVAC drivers |
| 4 | HVAC Demand Prediction Model | existing nb 04 | XGBoost v2 (test R² = 0.9973) — justified as scenario engine for counterfactuals |
| 5 | **Climate-Change Impact on HVAC Demand** | **new nb 05** | 6-AMY-year CDD/HDD regression, warming counterfactual, trend detection |
| 6 | **Grid Carbon Context and Baseline Emissions** | **new nb 06** | eGRID + Cambium ingestion, hourly LRMER profiles, annual CO₂e per archetype, peak-coincidence |
| 7 | **Carbon-Optimal Operation and Retrofit Pathways** | **new nb 07** | Flexibility envelope → carbon-optimal schedule → retrofit MACC → combined scenarios → carbon-price sensitivity |
| 8 | Discussion | new | Three-lever synthesis; policy implications; limitations — including archived MPC framework |
| 9 | Conclusions and Future Work | new | Key findings; extensions (real-grid APIs, occupant comfort surveys, MPC with forecast error, RL) |

Pre-pivot chapter plan (MPC framework + RL) is superseded. All reference numbers, stats, and methodology choices in each chapter must cite a short-key from `docs/references.md`.

---

## Current Status

- [x] Interim report submitted (13 March 2026)
- [x] Project structure built
- [x] `01_load_data.ipynb` — complete (3 TMY3 Parquet files + 81-sim multi-year loader). **Extended 2026-04-18** with Section 12 (markdown intro + loop-based loader + combiner) to pull 3 new AMY years (1988, 1996, 2005) × 3 climates × 3 efficiency × run_1 = 27 new simulations. Combined with existing run_1 subsets from `multi_year_raw.parquet`, produces `multi_year_pivot_raw.parquet` — the 54-simulation panel consumed by `05_climate_trends.ipynb`. Cells added but not yet executed; execute in VS Code when ready.
- [x] `02_eda.ipynb` — complete. 15 figures saved to `figures/`.
- [x] `03_features.ipynb` — complete. Single-year (v1) + 81-sim expanded (v2) feature matrices saved.
- [x] `04_ml_model.ipynb` — complete. v1 (TMY3) + v2 (81-sim) models trained and saved. `model_xgb_v2.pkl` retained as scenario engine for Phase 2.
- [x] **Research pivot (2026-04-18)** — scope pivoted from MPC framework to three-lever climate-and-carbon emissions analysis. Pivot rationale and literature gap documented below; approved plan at `/Users/cfd/.claude/plans/streamed-gliding-mango.md`.
- [x] **`05_mpc.ipynb` archived** → `notebooks/05_mpc_archive.ipynb` (git mv, archive preamble cell inserted). Artifacts retained on disk: `ml_dynamics_{1A,3C,5A}.pkl`, `mpc_results.json`, `figures/05_*.png`.
- [x] `docs/references.md` created — 40-reference thesis bibliography across 3 pillars (climate impact, grid carbon, retrofit MACC).
- [x] `config.py` extended with `DATA_EXTERNAL`, `DATA_EGRID`, `DATA_CAMBIUM`, `DOCS_DIR`, `AMY_YEARS_PIVOT`, `GRID_REGIONS`, `GRID_REGIONS_CAMBIUM`, `CARBON_PRICE_ETS_2026`, `CARBON_PRICE_GB_2022`, `CARBON_PRICE_GB_2050`, `CARBON_PRICE_SCC_USD`, `GBP_PER_USD`, `ASSET_LIFE_YEARS`, `DISCOUNT_RATE`.
- [x] **Execute Section 12 cells in `01_load_data.ipynb`** — `multi_year_pivot_raw.parquet` confirmed present (2,838,240 rows: 6 AMY years × 3 climates × 3 efficiency × run_1).
- [x] `05_climate_trends.ipynb` — **WRITTEN (2026-04-19)**. All 6 sections implemented and smoke-tested. Ready to execute in VS Code. Key design decisions:
  - Sections 1–3: CDD₁₈/HDD₁₅ from 10-min OAT; OLS sensitivity β_CDD per (climate, efficiency); scatter + trend plots.
  - Section 4: Observed 1988 vs 2005 counterfactual (actual HVAC Δ); XGBoost re-prediction using `scaler_X_v2` + `scaler_y_v2` (3–7% annual error vs actuals — validated).
  - Section 5: Linear trend regression of annual HVAC on year; early indication of weak trends (high p-values) — climate variability dominates over monotonic trend in 6-AMY-year window.
  - Section 6: Saves `data/processed/climate_sensitivity.json`; figures `05_cdd_hdd_trends.png`, `05_climate_sensitivity.png`, `05_warming_counterfactual.png`, `05_annual_hvac_trajectory.png`.
  - **Note:** `statsmodels` not in original `requirements.txt` — install via `pip install statsmodels` (done in venv).
- [ ] `06_grid_carbon.ipynb` — new notebook (O4): eGRID + Cambium ingestion, climate-to-grid mapping, hourly profile visualisation, annual emissions matrix, peak coincidence. **Next step.**
- [ ] `07_carbon_optimisation.ipynb` — new notebook (O5, O6): flexibility envelope (from salvaged RC model), carbon-optimal scheduling, retrofit MACC, scenario comparison, carbon-price sensitivity.
- [ ] Thesis write-up.

**Timeline.** ~6 weeks to thesis (current date 2026-04-19; target late May / early June 2026). Week 1 done: config + CLAUDE.md + nb 01 AMY extension + nb 05 written. Week 2: execute nb 05 + nb 06 grid carbon. Week 3–4: nb 06 complete + nb 07 start. Week 5–6: nb 07 carbon optimisation.

---

## Key Decisions & Findings So Far

### Pivot rationale (2026-04-18)

**What changed.** The thesis scope pivoted from building a Model Predictive Control (MPC) framework to a three-lever climate-and-carbon emissions analysis. Notebooks 01–04 carry forward unchanged; notebook 05 (MPC) is archived; three new notebooks (05 climate trends, 06 grid carbon, 07 carbon optimisation) deliver the new contribution.

**Why the MPC framework was archived.** The closed-loop MPC simulation on the AlphaBuilding synthetic dataset produced internally consistent results (22–46% energy savings on 8 of 9 windows, comfort compliance under ASHRAE 55 Class A) but hit a fundamental research-contribution ceiling. A simulated controller evaluated on a simulated building with zero model-plant mismatch and perfect forecasts cannot produce a claim that generalises to real buildings: the dominant real-world failure modes (forecast error, sensor noise, actuator drift, occupant divergence) are eliminated by construction. The numerical savings are defensible as an upper bound under ideal conditions, not as a publishable claim about deployable performance. In the 4th-year individual-project context this is a scientifically thin contribution.

**Why the three-lever framing addresses a real gap.** Péan, Salom & Costa-Castelló (2019) *J. Process Control* 74:35–49 review HVAC control strategies and find that CO₂-signal objectives are rare in the literature — economic/price objectives dominate (`[Pean2019]` in `docs/references.md`). Quantifying emissions-reduction potential under real regional grid carbon data, across three climates and three efficiency levels, and comparing it against retrofit and climate-adaptation pathways, addresses that under-served question directly. All three levers reuse the existing dataset + ML model, so the new notebooks extend the prior work rather than replacing it.

**What carries forward from archived nb 05.** Four components are explicitly salvaged and referenced in the new notebooks:
- **RC thermal model fitting** (per-climate α_persist, α_env, β_cool, β_heat, γ_occ) — reused in nb 07 for the flexibility envelope.
- **HVAC-mode-gated comfort band derivation** (per climate × season) — reused in nb 07 for shift-validity constraints.
- **HVAC_CAP per-climate saturation** (observed peak kWh/10-min) — reused in nb 07 for pre-cool / pre-heat magnitude bounds.
- **Occupancy-gated evaluation pattern** — reused in nb 06 for occupied-hour emissions accounting.

**Referenced in thesis as:** Chapter 8 Limitations section — "a control framework was explored as `notebooks/05_mpc_archive.ipynb`; closed-loop validation on synthetic data limits the research contribution, motivating the pivot to emissions analysis under real regional grid carbon data."

### ElectricityHVAC is a mixed signal
`hvac_kwh` captures total HVAC electricity — heating + cooling + fans + pumps. It is NOT cooling-only. Chicago (5A) shows large spikes in January/February due to heating load — this is expected and valid, not an error. This carries forward unchanged into the new narrative: nb 05 climate-trend CDD/HDD regression treats heating and cooling sensitivities separately; nb 06 emissions accounting uses the full signal.

### Decision: train on full signal, no seasonal filtering
The ML model (notebooks 01–04) was trained on full-year `hvac_kwh` across all seasons with no OAT filtering. This makes the predictor climate-agnostic at inference time — essential for the nb 05 warming counterfactual (apply 2005 weather to 1988 building) and the nb 06 emissions simulation (predict hourly HVAC under shifted schedules). The Chicago winter test case remains a meaningful generalisation benchmark in all three new notebooks.

### External data sources + reference library — see top-level sections
Phase-2 external data (eGRID, Cambium, UK ETS, Green Book, Rennert SCC, PNNL 90.1, ASHRAE service-life) and the reference-library workflow are documented as standalone sections near the top of this file: **§ External Data Sources (Phase 2)** and **§ Literature / Reference Library Workflow**. The short-key → notebook mapping table lives at the end of `docs/references.md`.

---

### Archived — MPC design decisions (notebook 05_mpc_archive)

> The decisions below document the final state of the archived MPC framework. They are preserved for thesis Chapter 8 Limitations and for reuse of the RC model / comfort bands / HVAC_CAP in nb 07. They are no longer active design decisions for the current narrative.

**MPC controlled full HVAC — heating and cooling.** The MPC cost function minimised deviation from a climate- and season-specific setpoint. In summer it reduced cooling; in winter it managed heating.

### Decision: RC perturbation-form plant model (Δ-tracking) — archived

**History:** Three iterations of the MPC plant model have been attempted:
1. **First attempt — absolute-form RC.** Open-loop 2016-step simulations drifted (especially Miami) because coefficient error compounded step-by-step.
2. **Second attempt — ML dynamics (XGBoost).** Achieved R² > 0.99 on one-step validation but catastrophically failed inside MPC: optimiser pinned `u` at lower bound for 100% of timesteps across 3 of 4 windows; Chicago winter temp deviation *worsened* (1.45°C → 1.90°C). Root cause: ML was trained on thermostat-controlled data where T ≈ setpoint regardless of HVAC level, so it predicted weak HVAC→T coupling. The optimiser exploited this "free lunch" and the comfort barrier never activated.
3. **Third attempt — absolute-form RC with corrected structure.** Fixed 3 of 4 windows (SF, Chicago summer, Chicago winter all improved substantially — Chicago summer violations 19.8% → 1.4%) but Miami baseline drifted 4.14°C open-loop (95% violations at u=1 — unphysical).
4. **Fourth attempt (current) — RC in perturbation form.** Track δ = T_mpc − T_ref, where T_ref is the AlphaBuilding reference trajectory.

**Perturbation-form equation:**
```
δ(t+1) = (α_persist − α_env)·δ(t)
       + β_cool·(u−1)·hvac_cool_ref(t)
       + β_heat·(u−1)·hvac_heat_ref(t)
T_mpc(t+1) = T_ref(t+1) + δ(t+1)
```

**Derivation:** Subtract the RC equation evaluated at T_mpc and T_ref. All shared terms (OAT, occupancy, diurnal, intercept) cancel — only the response to Δhvac = (u−1)·hvac_ref remains.

**Why this works:**
- At u=1: δ stays at 0 by construction. Baseline ≡ the AlphaBuilding data exactly — zero drift possible.
- At u≠1: δ captures only the *incremental* effect of control deviations. RC is used only for its sensitivity (β_cool, β_heat), not its absolute trajectory.
- (α_p − α_env) is typically ~0.97 < 1, so δ decays back toward 0 when u returns to 1 — stable.
- Isolates exactly the HVAC→T coupling we want; nuisance terms that caused drift are eliminated.

**Baseline is now trivial:** `run_baseline()` returns the AlphaBuilding window directly (indoor_temp_c, hvac_kwh columns). No simulation needed — u=1 means "apply what the thermostat already applied". This is the correct reference.

**RC coefficients retained per climate:** `rc_models = {'1A': {...}, '3C': {...}, '5A': {...}}` — fitted in Section 4 on 1990+1997 multi-year training data. Same coefficients as absolute-form; only the propagation mechanism changed.

**ML dynamics files (`ml_dynamics_*.pkl`) are retained** in `data/processed/` for thesis comparison but not used by the MPC loop.

### MPC architecture (notebook 05_mpc_archive — archived)
- **HVAC predictor:** `model_xgb_v2.pkl` (32 features → `hvac_kwh`) — predicts horizon HVAC demand (*framework component; perfect forecasts used for simulation*)
- **Dynamics model (plant):** RC **perturbation-form** per climate — δ-tracking, zero-drift baseline
- **Reference trajectory:** AlphaBuilding data (`indoor_temp_c`, `hvac_kwh`) — represents u=1 thermostat control
- **Optimiser:** `scipy.minimize` L-BFGS-B, horizon H=12 (120 min), warm-start enabled (previous solution shifted); δ state carried across MPC steps
- **Control variable:** u ∈ [0.5, 1.5] multiplying AlphaBuilding baseline HVAC
- **Comfort bands:** empirically derived in Section 3b using **HVAC-mode-gated P50** (cooling_sp = P50 of indoor_temp_c when cooling_kwh > 0; heating_sp = P50 when heating_kwh > 0). Band = `[heating_sp − 1, cooling_sp + 1]` spans the observed control dead-band plus ASHRAE 55-2020 PMV ±1°C margin. All 9 (climate × season) combinations; embedded dynamically in `SIM_WINDOWS` via `get_comfort_band()`.
- **HVAC capacity cap:** `HVAC_CAP[clim] = max(sim_data[clim]['hvac_kwh'])` — each climate's observed peak kWh/10-min. Applied in both `mpc_cost` (δ propagation uses effective u after cap) and `run_mpc` (hvac_applied = min(u·hvac_ref, cap)). Prevents u=1.5 from exceeding the actual equipment's delivered-capacity peak.
- **Occupancy-gated comfort evaluation:** comfort violations and the W_TEMP / W_VIOL terms in the cost function activate **only during occupied hours**. HVAC setback during unoccupied periods (cooling setback ≈ 26.7°C, heating ≈ 15.6°C) is a deliberate energy-saving strategy built into the AlphaBuilding reference — counting it as discomfort was inflating baseline violations (e.g., SF winter 55.7% → 30.2% occupied-only; Chicago winter 68.0% → 6.5% occupied-only). Both metrics reported: `comfort_violation_pct` (occupied, primary) and `comfort_violation_pct_all` (all-hour, reference).
- **Simulation windows:** 9 windows — 3 climates × 3 seasons each (2004 data, Standard, run_1):
  - Miami: July (summer), April (shoulder), January (winter)
  - San Francisco: July (summer), October (shoulder), January (winter)
  - Chicago: July (summer), April (shoulder), January (winter)
  - Each window: 14 days = 2016 steps. Season months: summer=[6,7,8], winter=[12,1,2], shoulder=[3,4,5,9,10,11].

**Cost function — 4 terms with occupancy gating on comfort:**
```
cost = occ(τ)·W_TEMP·(T − sp)² + occ(τ)·W_VIOL·max(0, out-of-band)²
     + W_ENERGY·hvac_delivered(τ) + W_SMOOTH·(Δu)²
```
where `hvac_delivered = min(u·hvac_ref, HVAC_CAP[clim])` and `occ(τ) ∈ {0,1}` is the occupancy mask over the horizon.

| Weight | Value | Role |
|--------|-------|------|
| W_TEMP | 30 | Quadratic pull toward setpoint within comfort band (occupied hours only) |
| W_VIOL | 500 | Hard barrier — heavy penalty if T exits comfort band (occupied hours only) |
| W_ENERGY | 1 | Reward for HVAC reduction (always active) |
| W_SMOOTH | 5 | Penalise rapid changes in u — prevents bang-bang behaviour (always active) |

**Weight calibration rationale:** With the RC plant model, reducing `u` now produces a real temperature response, so the comfort term and barrier can do their job without heavy over-weighting. `W_VIOL` is high (500) to make band violations decisively costly; `W_ENERGY` is kept at 1 since the RC coupling itself limits how far the optimiser can push `u` down. Gating comfort terms on occupancy lets MPC exploit the setback window for energy savings while maintaining comfort during occupied hours — matching how real buildings are operated.

### MPC simulation — what is and isn't realistic (archived; informs Chapter 8 Limitations)

**What is realistic:**
- Receding-horizon MPC architecture with physics-grounded plant model — industry standard approach
- 12-step / 120-min horizon — appropriate for building thermal mass
- Climate-zone comparison across 3 zones — meaningful for policy generalisation
- Hybrid architecture: data-driven HVAC demand predictor (XGBoost) + physics RC plant model — matches practice where control engineers use simple interpretable thermal models

**What is NOT realistic (known limitations — state explicitly in thesis):**
- **Perfect forecasts** — OAT, occupancy, and time are known exactly over the horizon. Real systems use weather forecasts (±1–2°C error) and occupancy predictions (±20–30%). This is the "certainty equivalence" assumption, standard in academic MPC.
- **No model-plant mismatch** — the MPC's internal RC coefficients are fitted on the same AlphaBuilding data used to define the baseline reference trajectory. Real deployments suffer from mismatch between learned model and actual building response — the primary source of real-world underperformance.
- **Perturbation-form assumes valid reference** — the plant is linearised around the AlphaBuilding u=1 trajectory. For large excursions (u near 0.5 or 1.5 sustained over many steps), the RC linearisation degrades. Conservative δ growth limits this in practice, but extrapolation beyond the data is untested.
- **Single u multiplier** — real HVAC control acts on supply air temperature, chilled water setpoints, fan speeds, VAV dampers — not a single scalar. Mapping from actuators to `hvac_kwh` is nonlinear with delays.
- **Limited actuator constraints** — equipment capacity cap is applied (hvac_delivered ≤ observed peak), but no minimum on/off times, ramp rate limits, or chiller staging logic. A simple Δu smoothness penalty (W_SMOOTH) approximates ramp control in aggregate.
- **Single aggregated zone** — multiple thermal zones treated as one indoor temperature.

**Thesis framing (archived rationale):** MPC results represented an **upper bound on achievable performance under ideal conditions**. The simulation-in-the-loop framework eliminated model-plant mismatch by design, which is precisely why this cannot support a deployable-performance claim. This limitation is the pivot motivation recorded in the "Pivot rationale" subsection above; the ML predictor (`model_xgb_v2.pkl`), RC coefficients, comfort bands, and HVAC_CAP are reused by the new nb 07 flexibility envelope and emissions analysis.

---

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
- Comfort bands are **derived empirically from data** (2004 Standard run_1 occupied-hour indoor temperatures) using an **HVAC-mode-gated P50** method:
  - **Method:** For each (climate, season), separate occupied-hour samples into cooling-active (cooling_kwh > 0) and heating-active (heating_kwh > 0) subsets. Take P50 of indoor_temp_c in each → `cooling_sp` and `heating_sp`. Band = `[heating_sp − 0.5, cooling_sp + 0.5]`. If only one mode is active, use `[sp − 0.5, sp + 0.5]`.
  - **Why HVAC-mode gating:** The AlphaBuilding thermostat uses separate cooling and heating setpoints. A simple P50 of all occupied temps gives a band around whichever mode dominates (e.g., SF winter heating → narrow band missing the cooling regime that does activate). Mode gating reads the thermostat setpoints directly from observed equipment activation states.
  - **Why ±0.5°C margin (ASHRAE 55-2020 Class A):** AlphaBuilding's thermostat holds occupied-hour T within ≈ ±0.15°C of design setpoint — the natural operating envelope spans < 0.3°C per window. With the earlier ±1°C margin (ASHRAE Class B), the comfort band was 4× wider than the observed envelope and produced trivially 0% baseline violations in 7 of 9 windows, making the metric useless for discriminating controller performance. ASHRAE 55-2020 **Class A** (premium indoor environment) uses PMV ±0.2 ≈ ±0.5°C operative temperature — the physically motivated tight comfort standard for office work. This gives a band (1.0-1.4°C wide) that meaningfully discriminates baseline from MPC.
  - **Comfort bands used in MPC (HVAC-mode-gated, ±0.5°C Class A):**
    | Climate/Season | Band (°C) | Baseline viol% (occ) |
    |---|---|---|
    | Miami summer    | [23.6, 24.6] | 0.0 (genuine perfect regulation) |
    | Miami shoulder  | [23.2, 24.6] | ~0.7 |
    | Miami winter    | [23.2, 24.4] | ~1.5 |
    | SF summer       | [23.4, 24.5] | ~1.1 |
    | SF shoulder     | [23.2, 24.4] | ~1.9 |
    | SF winter       | [22.7, 23.7] | ~60.5 (real comfort gap during heating ramp-up) |
    | Chicago summer  | [23.4, 24.5] | 0.0 (tight cooling control) |
    | Chicago shoulder| [22.6, 23.8] | ~17.6 |
    | Chicago winter  | [21.4, 22.5] | ~16.6 |
  - **Occupancy gating:** Comfort violations are counted ONLY during occupied hours. Unoccupied setback (cooling ≈ 26.7°C, heating ≈ 15.6°C) is a deliberate energy-saving strategy — counting it as discomfort inflated baseline metrics (e.g., SF winter 55.7% → 30.2% occupied; Chicago winter 68.0% → 6.5% occupied).
  - These are **computed live in Section 3b of notebook 05** — COMFORT_BANDS, SETPOINTS, and HVAC_CAP dicts start empty and are populated by the analysis cell

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

**Selected as Phase 2 scenario engine: XGBoost (3000 rounds)**
- RF has lower test RMSE (0.1859 vs 0.2114) but is dominated by autoregressive lag features — produces a flatter response surface, less useful when exposing feature-level sensitivities to OAT, CDD/HDD and time-of-day (needed for nb 05 warming counterfactual and nb 07 scheduling).
- XGBoost distributes importance across OAT, occupancy, time features — physically meaningful, gives the new notebooks actionable gradients for counterfactuals (e.g. "what is HVAC demand under 2005 weather on a Standard building from 1988?").
- XGBoost did not converge within 3000 rounds (best_iteration=2999) — val RMSE (0.2744) now matches RF (0.2738); remaining test gap is a tuning issue not a model limitation.
- Both models achieve R² > 0.997 — highly accurate HVAC demand prediction across all climates and efficiency levels. Precision is well above what is needed for annual-emissions accounting.
- The archived MPC notebook also used this model as its horizon HVAC-demand predictor (not the dynamics plant); this reuse is historical and does not affect Phase 2.

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
- **Phase 2 new notebooks use**: `model_xgb_v2.pkl` + `MPC_FEATURES_V2` (32 features) as the counterfactual-scenario engine — XGBoost selected due to physically distributed feature importance. Specifically: nb 05 for warming-counterfactual demand projections; nb 07 for retrofit-scenario and load-shift demand predictions.

## Coding conventions and operational rules

**Data access:**
- Always use `anon=True` in `s3fs.S3FileSystem()` — the AlphaBuilding S3 bucket is public.
- Never hardcode the S3 path — use `S3_PATH` from `config.py`.
- Raw HDF5 energy variables are in **Joules** — always convert with `J_TO_KWH`.
- Target variable for ML is `hvac_kwh` — total HVAC electricity (heating + cooling combined), not cooling only. Never filter to cooling-season only for ML training.
- `hvac_kwh` spikes in Chicago (5A) during winter are expected and valid — they reflect heating-season HVAC load, not errors.

**Phase 2 (climate-carbon analysis):**
- Use `GRID_REGIONS` (historical eGRID) from `config.py` for annual CO₂e factor lookups; use `GRID_REGIONS_CAMBIUM` (with `5A → p20`) for hourly LRMER lookups.
- Use `CARBON_PRICE_ETS_2026`, `CARBON_PRICE_GB_2022`, `CARBON_PRICE_GB_2050`, `CARBON_PRICE_SCC_USD` for carbon-pricing scenarios — not literal numbers scattered through notebooks.
- Use `ASSET_LIFE_YEARS = 25` and `DISCOUNT_RATE = 0.035` for MACC CAPEX annualisation.
- Use `AMY_YEARS_PIVOT` for the 6-year climate-trend panel (1988, 1990, 1996, 1997, 2004, 2005).
- Store Phase 2 external inputs in `data/external/egrid/` and `data/external/cambium/`; store derived outputs in `data/processed/`.
- Every numeric claim in a Phase 2 markdown cell cites a short-key from `docs/references.md` (e.g. `[eGRID2022]`, `[Hart2015-PNNL]`).

**Plotting and saving:**
- Use `CLIMATE_COLOURS` and `EFFICIENCY_COLOURS` from `config.py` for all plots.
- Save all figures to `figures/` with notebook-prefixed names (e.g. `05_cdd_hdd_trends.png`, `06_peak_coincidence.png`, `07_macc_per_climate.png`).
- Save processed data as **Parquet** to `data/processed/` — never commit raw HDF5 to git.
- `data/processed/` is gitignored; the small `data/external/*.csv` inputs for eGRID/Cambium are committed (< 50 MB total) for reproducibility.

**Archived MPC (no longer active, but retained on disk):**
- `notebooks/05_mpc_archive.ipynb` — renamed from `05_mpc.ipynb` on 2026-04-18.
- Archived comfort bands and HVAC_CAP still live in Section 3b of that notebook; they are the source-of-truth for the nb 07 flexibility envelope derivation.
- Archived RC coefficients (`α_persist`, `α_env`, `β_cool`, `β_heat`, `γ_occ` per climate) live in Section 4 of the archived notebook and are salvaged by nb 07.
- Do not add new MPC work to the archived notebook. Bug-fixes to salvaged components belong in the new notebook that consumes them (typically nb 07).
