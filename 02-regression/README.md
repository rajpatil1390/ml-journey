# Pumpkin Price Predictor

> Predict US pumpkin prices from variety, city and month with linear, polynomial and logistic regression.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.67-FF4B4B?logo=streamlit&logoColor=white)
[![Live Demo](https://img.shields.io/badge/Live_Demo-coming_soon-lightgrey?logo=streamlit&logoColor=white)](#live-demo)

**Module 02: Regression**, part of [ML Journey](../README.md), our 10-day run through Microsoft's ML-For-Beginners where every module ships as a deployed app.

## Live Demo

_Not deployed yet. The link goes here after the first deploy to Streamlit Community Cloud._

<!-- Save a screenshot of the running app as screenshot.png in this folder, then uncomment: -->
<!-- ![Screenshot of the Pumpkin Price Predictor app](screenshot.png) -->
_Screenshot: TODO, add after the first deploy._

## Problem

_TODO: 2–4 sentences. What question does this answer? Who would use it? Why is it a Regression problem?_

## Dataset

| | |
|---|---|
| **Dataset** | [US pumpkin prices](https://www.kaggle.com/usda/a-year-of-pumpkin-prices) (`US-pumpkins.csv`) |
| **Origin** | USDA Specialty Crops Terminal Markets Standard Reports (public domain) |
| **Provided by** | Microsoft [ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression) (MIT License) |
| **Size** | _TODO: rows × columns after cleaning_ |
| **Target** | _TODO: the column we predict, or "none (unsupervised)"_ |

Dataset and lesson material credited to the [ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) curriculum by Microsoft.

## Approach

1. **Explore and clean:** _TODO: missing values, filtering, notable findings._
2. **Features:** _TODO: what goes into the model and why._
3. **Models:** _TODO: baseline first, then what we tried._
4. **Evaluate:** _TODO: metric(s) and validation strategy (train/test split, CV)._
5. **Ship:** final model saved to `models/` with joblib, served by `app.py` on Streamlit Community Cloud.

## Results

| Model | Metric | Score | Notes |
|---|---|---|---|
| _Baseline_ | _TODO_ | _TODO_ | _TODO_ |
| _Final model_ | _TODO_ | _TODO_ | _TODO_ |

_TODO: one or two sentences on what the numbers mean, and how they compare with the ML-For-Beginners `/solution`._

## How to run locally

Requires Python 3.12.

```bash
git clone https://github.com/rajpatil1390/ml-journey.git
cd ml-journey
python -m venv .venv
.venv\Scripts\activate            # Windows
# source .venv/bin/activate       # macOS / Linux
pip install -r 02-regression/requirements.txt
streamlit run 02-regression/app.py
```

To retrain the model, also run `pip install -r requirements-dev.txt`, then run the notebook in `02-regression/notebooks/` top to bottom. It writes the model to `02-regression/models/`.

## Project structure

```text
02-regression/
├── app.py             # Streamlit app; loads the saved model from models/
├── requirements.txt   # pinned dependencies for this module only (used by Streamlit Cloud)
├── notebooks/         # exploration and training; runs top to bottom
├── data/              # small datasets (large or raw files are git-ignored)
├── src/               # reusable code shared by the notebooks and app.py
└── models/            # trained model(s) loaded by app.py
```

## What I learned

- _TODO: a concept that finally clicked_
- _TODO: something that surprised us in the data_
- _TODO: a mistake, and how it was fixed_

## Author

[Raj](https://github.com/rajpatil1390)

## Reviewer

Reviewed by [Bhavesh](https://github.com/bhaveshvinodpatil20). Every change to this repo goes through a pull request approved by the partner.

## Acknowledgements

Curriculum, lesson structure and dataset: [Microsoft ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) (MIT License). The code in this module is our own; we compared it with the lesson's `/solution` afterwards.
