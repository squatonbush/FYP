# HVAC Cooling Optimisation — MEng Final Year Project
**A Data-Driven Predictive Control Framework for HVAC Cooling Optimisation in Commercial Office Buildings**

Cheuk Fung Donald Man | Imperial College London | MEng Civil Engineering
Supervised by Dr. Po-Heng Lee

---

## Project Structure

```
hvac_project/
│
├── config.py               ← Central config (S3 path, constants, colours)
├── requirements.txt        ← Python dependencies
│
├── notebooks/
│   ├── 01_load_data.ipynb  ← Environment check, S3 connection, data loading ✓
│   ├── 02_eda.ipynb        ← Exploratory data analysis & visualisations ✓
│   ├── 03_features.ipynb   ← Feature engineering (in progress)
│   ├── 04_ml_model.ipynb   ← ML model training & evaluation (RF, XGBoost, LSTM)
│   └── 05_mpc.ipynb        ← Model Predictive Control framework
│
├── data/
│   └── processed/          ← Locally saved Parquet files (gitignored — regenerate by running 01)
│
└── figures/                ← Saved plots for the thesis (gitignored — regenerate by running 02)
```

---

## Setup (do this once)

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Register the venv as a Jupyter kernel

```bash
python -m ipykernel install --user --name=hvac_venv --display-name "Python (hvac venv)"
```

### 4. Open notebooks in VS Code

Install the **Jupyter** extension in VS Code, then open any `.ipynb` file.
Select **"Python (hvac venv)"** as the kernel — do not use the system Python kernel.

---

## Running Order

Run notebooks in order. Each one depends on outputs from the previous:

1. **`01_load_data.ipynb`** — connects to S3, loads 3 climate zone simulations, saves parquets to `data/processed/`
2. **`02_eda.ipynb`** — loads parquets, generates 15 EDA figures saved to `figures/`
3. **`03_features.ipynb`** — feature engineering for ML model input
4. **`04_ml_model.ipynb`** — trains and evaluates Random Forest, XGBoost, LSTM
5. **`05_mpc.ipynb`** — MPC framework using trained ML model as predictive engine

---

## Dataset

**AlphaBuilding Synthetic Building Operation Dataset**
- Source: [OEDI / LBNL](https://data.openei.org/submissions/2977)
- Access: Public AWS S3 bucket (`s3://oedi-data-lake/...`) — **no credentials needed**
- Format: HDF5 (streamed via `s3fs` + `h5py`, no local download required)

---

## Key Variables

| Column | Description | Unit |
|--------|-------------|------|
| `hvac_kwh` | Total HVAC electricity ← **ML target** | kWh |
| `cooling_kwh` | Cooling-only electricity | kWh |
| `heating_kwh` | Heating-only electricity | kWh |
| `total_kwh` | Total site electricity | kWh |
| `gas_kwh` | Natural gas consumption | kWh |
| `oat_c` | Outdoor air dry-bulb temperature | °C |
| `indoor_temp_c` | Mean indoor air temperature (all zones) | °C |
| `occupancy` | Total building occupant count | persons |
| `lighting_kwh` | Interior lighting electricity | kWh |
| `plugloads_kwh` | Plug loads / MELs electricity | kWh |
| `hour` | Hour of day (0–23) | — |
| `month` | Month (1–12) | — |
| `is_weekday` | 1 if Monday–Friday | — |
| `is_occupied` | 1 if weekday 07:00–20:00 | — |
| `oat_roll1h` | 1-hour rolling mean OAT | °C |
| `oat_roll3h` | 3-hour rolling mean OAT | °C |
| `climate` | Climate zone: "1A", "3C", or "5A" | — |
| `efficiency` | Efficiency level: "Low", "Standard", or "High" | — |
