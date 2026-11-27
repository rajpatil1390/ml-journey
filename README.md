# ML Journey

> Two developers, 10 days, 9 deployed machine-learning apps. We are working through Microsoft's
> [ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) curriculum and shipping every
> module as a live Streamlit app with a write-up.

[![CI](https://github.com/rajpatil1390/ml-journey/actions/workflows/ci.yml/badge.svg)](https://github.com/rajpatil1390/ml-journey/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.67-FF4B4B?logo=streamlit&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Each module is a self-contained mini-project: a notebook that trains a model, reusable code in
`src/`, a saved model, a Streamlit app deployed to Streamlit Community Cloud, and a README
covering the problem, data, approach and results.

## Modules

| Module | Topic | Owner | Live Demo | Status |
|---|---|---|---|---|
| [01-intro](01-intro/) | Introduction to ML: workflow, history, fairness | Raj & Bhavesh (shared) | Coming soon | 📋 Planned |
| [02-regression](02-regression/) | Regression: pumpkin price prediction | [Raj](https://github.com/rajpatil1390) | Coming soon | 📋 Planned |
| [03-web-app](03-web-app/) | Web App: UFO sighting country predictor | [Bhavesh](https://github.com/bhaveshvinodpatil20) | Coming soon | 📋 Planned |
| [04-classification](04-classification/) | Classification: cuisine classifier | [Raj](https://github.com/rajpatil1390) | Coming soon | 📋 Planned |
| [05-clustering](05-clustering/) | Clustering: Nigerian music clusters | [Bhavesh](https://github.com/bhaveshvinodpatil20) | Coming soon | 📋 Planned |
| [06-nlp](06-nlp/) | NLP: hotel review sentiment | [Raj](https://github.com/rajpatil1390) | Coming soon | 📋 Planned |
| [07-timeseries](07-timeseries/) | Time Series: energy load forecasting | [Bhavesh](https://github.com/bhaveshvinodpatil20) | Coming soon | 📋 Planned |
| [08-reinforcement](08-reinforcement/) | Reinforcement Learning: Q-learning agent | [Raj](https://github.com/rajpatil1390) | Coming soon | 📋 Planned |
| [09-real-world](09-real-world/) | ML in the Real World: model debugging | Raj & Bhavesh (shared) | Coming soon | 📋 Planned |

Status key: 📋 Planned · 🚧 In progress · 👀 In review · ✅ Deployed

## Collaboration workflow

We work like a small product team: nothing reaches `main` without a review from the partner.

1. **Pick up the module issue.** Every module has an issue assigned to its owner.
2. **Branch from `main`** as `<owner>/<module>-<short-desc>`:
   ```bash
   git switch main && git pull
   git switch -c raj/02-regression-pumpkin-model
   ```
3. **Build it:** notebook in `notebooks/`, reusable code in `src/`, trained model saved to `models/`,
   app in `app.py`, README from [`docs/README_TEMPLATE.md`](docs/README_TEMPLATE.md).
4. **Commit using [Conventional Commits](https://www.conventionalcommits.org/):** `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`.
5. **Open a pull request.** Fill in the template and request the partner as reviewer.
6. **CI runs on every PR.** It installs the changed module's requirements, parses and smoke-runs its
   `app.py`, and runs ruff.
7. **The partner reviews and merges.** One approval is required and authors never merge their own PRs.
   `main` is protected, so direct pushes are blocked.
8. **Deploy** the module on Streamlit Community Cloud (below), then update the table above.

The full rules, which Claude Code sessions in this repo also follow, are in [`CLAUDE.md`](CLAUDE.md).

### Deploying a module to Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) → **Create app** → *Deploy a public app from GitHub*.
2. Repository `rajpatil1390/ml-journey`, branch `main`, main file path `<module>/app.py`
   (e.g. `02-regression/app.py`).
3. **Advanced settings** → Python **3.12**.
4. Pick a custom subdomain such as `ml-journey-regression`, then deploy. Cloud installs the
   `requirements.txt` that sits next to `app.py`, so each module deploys with only its own dependencies.

## Repository structure

```text
ml-journey/
├── 01-intro/ … 09-real-world/   # one mini-project per curriculum module
│   ├── app.py                   #   Streamlit app (loads models/)
│   ├── requirements.txt         #   pinned, module-only dependencies
│   ├── README.md                #   project write-up (from the template)
│   ├── notebooks/  data/  src/  models/
├── docs/README_TEMPLATE.md      # template every module README follows
├── .github/                     # CI workflow, PR and issue templates
├── CLAUDE.md                    # working rules for humans and Claude Code
├── requirements-dev.txt         # dev tools: ruff, jupyterlab
└── ruff.toml                    # lint config (CI uses it)
```

## Tech stack

| Area | Tools |
|---|---|
| Language | Python 3.12 |
| Data | pandas, NumPy |
| Machine learning | scikit-learn, imbalanced-learn, statsmodels, NLTK, Gymnasium |
| Visualisation | Matplotlib, Seaborn |
| Apps and hosting | Streamlit, Streamlit Community Cloud |
| Notebooks | JupyterLab |
| Quality and CI | Ruff, GitHub Actions, branch protection with required reviews |
| AI pair programming | Claude Code (rules in `CLAUDE.md`) |

Built with assistance from Claude Code.

## Running locally

```bash
git clone https://github.com/rajpatil1390/ml-journey.git
cd ml-journey
python -m venv .venv
.venv\Scripts\activate            # Windows
# source .venv/bin/activate       # macOS / Linux
pip install -r 02-regression/requirements.txt
streamlit run 02-regression/app.py
```

For notebook work and linting: `pip install -r requirements-dev.txt`, then `ruff check .`.

## Authors

- **Raj**: [@rajpatil1390](https://github.com/rajpatil1390)
- **Bhavesh**: [@bhaveshvinodpatil20](https://github.com/bhaveshvinodpatil20)

## Acknowledgements

The curriculum, lessons and datasets come from [Microsoft ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners)
(MIT License). The code here is our own. Each module README credits its dataset's original source.

## License

[MIT](LICENSE)
