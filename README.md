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

