# MLOPS_Pipeline

A simple end-to-end machine learning pipeline example in Python.

## Project Overview

This repository contains components for data ingestion, transformation, model training, and prediction organized under `src/`. It includes example notebooks, scripts, and artifact outputs.

- **Source code:** `src/` (components, pipeline, utils)
- **Notebooks:** `notebook/` (EDA and model training notebooks)
- **Artifacts:** `artifacts/` (train/test/data artifacts)
- **Logs:** `logs/`

## Requirements

Install dependencies into a virtual environment. The project includes a `requirements.txt` file and a `myenv/` virtual environment skeleton.

On Windows (PowerShell):

```powershell
# Activate existing venv
& myenv\Scripts\Activate.ps1
# Or create a new venv
python -m venv .venv
& .venv\Scripts\Activate.ps1
# Install requirements
pip install -r requirements.txt
```

## Quick Start

1. Prepare data
	- Place datasets under `artifacts/` or update the data ingestion config in `src/components/data_ingestion.py`.

2. Run training pipeline

```powershell
python src/pipeline/train_pipeline.py
```

3. Run prediction pipeline / app

```powershell
python src/pipeline/predict_pipeline.py
# or run the application entrypoint
python application.py
```

4. Notebooks

Open the notebooks for interactive exploration and experiments:
- `notebook/1 . EDA STUDENT PERFORMANCE .ipynb`
- `notebook/2. MODEL TRAINING.ipynb`

## Project Structure

- `src/components/` — data ingestion, transformation, model trainer
- `src/pipeline/` — training and prediction pipeline scripts
- `artifacts/` — input/output datasets and model artifacts
- `catboost_info/` — CatBoost training metadata

## Contributing

- Create an issue or pull request for changes.
- Follow the existing code style and add tests where appropriate.

## Notes

- This project was developed on Windows; adjust activation commands for other OSes.
- If `myenv/` is already present, activate it before installing dependencies.

## Model Evaluation Results

These R² scores were computed on `artifacts/test.csv` using the saved `artifacts/preprocessor.pkl` and `artifacts/model.pkl` in this repository.

- **Saved model:** LinearRegression — R² = 0.8804
- **LinearRegression (baseline):** R² = 0.8804
- **RandomForest (baseline):** R² = 0.8488
- **DecisionTree (baseline):** R² = 0.7473

To reproduce these numbers locally, run the evaluation script (example):

```powershell
python - <<'PY'
import os,pickle,pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

art='artifacts'
model=pickle.load(open(os.path.join(art,'model.pkl'),'rb'))
preproc=pickle.load(open(os.path.join(art,'preprocessor.pkl'),'rb'))
train=pd.read_csv(os.path.join(art,'train.csv'))
test=pd.read_csv(os.path.join(art,'test.csv'))
target='math_score'
features=[c for c in test.columns if c!=target]
X_train=preproc.transform(train[features])
X_test=preproc.transform(test[features])
print('Saved R2',r2_score(test[target],model.predict(X_test)))
LR=LinearRegression().fit(X_train,train[target])
RF=RandomForestRegressor(n_estimators=100,random_state=42).fit(X_train,train[target])
DT=DecisionTreeRegressor(random_state=42).fit(X_train,train[target])
print('LR',r2_score(test[target],LR.predict(X_test)))
print('RF',r2_score(test[target],RF.predict(X_test)))
print('DT',r2_score(test[target],DT.predict(X_test)))
PY
```

## Web UI (Flask)

A minimal Flask app can serve a prediction form and a `/metrics` endpoint that returns the same evaluation scores. See `app.py` (example) in the repo for a suggested implementation — run with:

```powershell
python app.py
```

