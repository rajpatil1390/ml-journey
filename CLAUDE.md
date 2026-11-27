# CLAUDE.md: rules for every Claude Code session in ml-journey

This repo is a monorepo built by two developers working through Microsoft's
ML-For-Beginners curriculum in 10 days. Every module becomes a deployed mini-project.

| Person  | GitHub                                                         | Branch prefix |
|---------|----------------------------------------------------------------|---------------|
| Raj     | [rajpatil1390](https://github.com/rajpatil1390)                | `raj/`        |
| Bhavesh | [bhaveshvinodpatil20](https://github.com/bhaveshvinodpatil20)  | `bhavesh/`    |

Module owners: Raj owns 02, 04, 06, 08. Bhavesh owns 03, 05, 07. Modules 01 (intro) and
09 (real-world) are shared by both. The partner who did not write a change reviews it.

These rules are not optional. If a request conflicts with them, stop and ask the user.

## 1. Git and branches

- **Never commit to `main`.** `main` is protected; the setup commit is the only direct commit it will ever get.
- Before any change, create a branch from an up-to-date `main`:
  `git switch main && git pull && git switch -c <owner>/<module>-<short-desc>`
  - `<owner>` is `raj` or `bhavesh`: whoever is doing the work.
  - `<module>` is the module folder, e.g. `02-regression`. Use `repo` for changes outside module folders.
  - `<short-desc>` is 2–4 lowercase words joined by hyphens.
  - Examples: `raj/02-regression-pumpkin-model`, `bhavesh/05-clustering-kmeans-app`, `raj/repo-ci-cache`.
- Never force-push to a shared branch, never rewrite `main` history, never skip hooks (`--no-verify`).

## 2. Pull requests and review

- **Every change goes through a pull request** into `main`, using `.github/pull_request_template.md`.
- The **partner reviews**: Raj reviews Bhavesh's PRs and the other way round. Request the partner as reviewer.
- **Never self-merge.** The author never merges their own PR, and Claude never merges any PR.
  After approval, the reviewer merges (squash merge).
- Link the module's issue in the PR body (`Closes #<n>`).

## 3. Commits

Use Conventional Commits, imperative mood, at most 72 characters in the subject:

| Prefix      | Use for                                        | Example                                          |
|-------------|------------------------------------------------|--------------------------------------------------|
| `feat:`     | new functionality (notebook, model, app)       | `feat(02-regression): add polynomial regression model` |
| `fix:`      | bug fixes                                      | `fix(03-web-app): load model relative to app.py` |
| `docs:`     | README and documentation                       | `docs(04-classification): add results table`     |
| `refactor:` | restructure without behaviour change           | `refactor(05-clustering): move plotting into src` |
| `chore:`    | tooling, CI, dependencies, config              | `chore: bump streamlit to 1.68.0`                |

The scope in parentheses is the module folder. Leave it out for repo-wide changes.

- **Attribution:** Commits must contain no co-author trailers; author must be the human running the session.

## 4. Using the reference curriculum

- The reference repo is cloned read-only at `../ML-For-Beginners` (sparse checkout without translations).
  **Never modify, commit to, or copy files wholesale from it.**
- Read the lesson first, then **write our own code**. Do not paste solution code.
- After our version works, **compare it with the lesson's `/solution`** folder and note real
  differences (approach, metrics) in the module README.
- Data files may be copied from the reference into the module's `data/` folder (credit the source in the README).

## 5. Module layout and code quality

Every module folder (`01-intro` … `09-real-world`) has exactly this shape:

```text
<module>/
├── app.py             # Streamlit app, loads the model from models/
├── requirements.txt   # pinned (==), only what THIS module imports
├── README.md          # follows docs/README_TEMPLATE.md
├── notebooks/         # exploration and training
├── data/              # small data; data/raw/ is git-ignored for big downloads
├── src/               # reusable code (a package: src/__init__.py)
└── models/            # saved model(s), committed so the deployed app can load them
```

- **Reusable code goes in the module's `src/`.** Do not copy the same function between a
  notebook and `app.py`. Import it instead: `from src.features import build_features`.
  In notebooks, run `sys.path.append("..")` first.
- **Notebooks must run top to bottom** on a fresh kernel (Restart and Run All, or
  `jupyter nbconvert --to notebook --execute --inplace <nb>.ipynb`) before every commit.
- **Trim notebook outputs** before committing: show `.head()` and not whole DataFrames, no long training
  logs, no widget state, no huge images. Keep key plots and metric outputs small.
- No file over 25 MB in git. Large downloads go in `<module>/data/raw/` (git-ignored), with
  download steps in the module README.
- Never commit secrets: `.env` and `.streamlit/secrets.toml` are git-ignored.
- Code must pass `ruff check .` (config: `ruff.toml`). Run it before pushing.

## 6. Streamlit app and deployment

- **Every module must have a working `app.py`** that:
  - loads its saved model from `models/` using a path relative to the file:
    `Path(__file__).resolve().parent / "models" / "model.joblib"`. Streamlit Cloud runs from
    the repo root, so a bare `"models/model.joblib"` path breaks in production.
  - caches the model with `@st.cache_resource`.
  - runs with `streamlit run <module>/app.py` from the repo root.
- It must deploy on **Streamlit Community Cloud** using **that module's own `requirements.txt`**
  (Cloud reads the requirements file next to the entrypoint). Settings: repo `rajpatil1390/ml-journey`,
  branch `main`, main file `<module>/app.py`, Python 3.12.
- `requirements.txt` holds pinned versions (`pkg==x.y.z`) of only the packages the module imports.
  Dev tools (jupyter, ruff) go in the root `requirements-dev.txt`, never in a module.
- The scikit-learn version used to train must equal the pinned one, or the pickled model may
  not load. Retrain after bumping scikit-learn.
- CI (`.github/workflows/ci.yml`) installs each changed module's requirements, parses and
  smoke-runs `app.py`, and runs ruff. It must be green before merge.

## 7. Documentation

- **Every module README follows `docs/README_TEMPLATE.md`**: same sections, same order, all
  `{{TOKENS}}` and _TODO_ markers replaced, real numbers in the Results table.
- When a module is deployed, update its row in the root `README.md` table (Live Demo link, Status).

## 8. Useful commands

```bash
python -m venv .venv && .venv\Scripts\activate          # Windows (source .venv/bin/activate on macOS/Linux)
pip install -r requirements-dev.txt                       # ruff, jupyterlab
pip install -r 02-regression/requirements.txt             # one module's runtime deps
streamlit run 02-regression/app.py                        # run an app from the repo root
ruff check .                                              # lint everything (notebooks too)
python -c "import ast; ast.parse(open('02-regression/app.py', encoding='utf-8').read())"   # the CI syntax check
```

## 9. End of every task: SUMMARY REPORT

Finish every task by printing a report in this format:

```text
SUMMARY REPORT
- Branch:          <branch name>
- Files created:   <paths>
- Files changed:   <paths>
- Commands run:    <commands that changed state or verified work>
- Test/run results: <ruff, app smoke run, notebook execution: pass/fail, with numbers>
- PR:              <link, or "not opened" and why>
- Failed / unsure: <anything that failed, was skipped, or you were unsure about; "none" only if truly none>
```
