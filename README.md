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
├── data_loader.py          ← All data extraction from HDF5/S3
├── requirements.txt        ← Python dependencies
│
├── notebooks/
│   ├── 01_load_data.ipynb  ← Environment check, S3 connection, data loading
│   ├── 02_eda.ipynb        ← Exploratory data analysis & visualisations
│   ├── 03_features.ipynb   ← Feature engineering
│   ├── 04_ml_model.ipynb   ← ML model training & evaluation (RF, XGBoost, LSTM)
│   └── 05_mpc.ipynb        ← Model Predictive Control framework
│
├── data/
│   └── processed/          ← Locally saved Parquet files (gitignored)
│
└── figures/                ← Saved plots for the thesis
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

### 3. Open notebooks in VS Code

Install the **Jupyter** extension in VS Code, then open any `.ipynb` file.  
Select your `venv` as the kernel.

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
| `hvac_kwh` | HVAC electricity consumption ← **target variable** | kWh |
| `total_kwh` | Total site electricity | kWh |
| `gas_kwh` | Natural gas consumption | kWh |
| `oat_c` | Outdoor air dry-bulb temperature | °C |
| `occupancy` | Total building occupant count | persons |
| `lighting_kwh` | Interior lighting electricity | kWh |
| `plugloads_kwh` | Plug loads / MELs electricity | kWh |
| `hour` | Hour of day (0–23) | — |
| `is_weekday` | 1 if Monday–Friday | — |
| `is_occupied` | 1 if weekday 07:00–20:00 | — |
| `oat_roll1h` | 1-hour rolling mean OAT | °C |
| `oat_roll3h` | 3-hour rolling mean OAT | °C |
| `climate` | "1A", "3C", or "5A" | — |
| `efficiency` | "Low", "Standard", or "High" | — |
