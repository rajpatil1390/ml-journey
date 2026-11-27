<!--
  Title: Conventional Commit style, e.g. "feat(02-regression): add polynomial regression model"
  Branch: <owner>/<module>-<short-desc>
  Request the partner as reviewer. Never merge your own PR.
-->

Closes #<!-- issue number -->

## What changed

<!-- What does this PR add or fix, and why? Bullet points are fine. -->

-

## How to test

<!-- Exact steps a reviewer can copy and paste. -->

```bash
pip install -r <module>/requirements.txt
streamlit run <module>/app.py
```

1.

## Live demo link

<!-- https://<subdomain>.streamlit.app, or "not deployed yet" with the reason. -->

## Screenshots

<!-- Drag and drop screenshots of the app or key plots here. Delete this section for non-UI changes. -->

## Reviewer checklist

<!-- The reviewer ticks these. -->

- [ ] Branch name is `<owner>/<module>-<short-desc>` and commits follow Conventional Commits
- [ ] Notebook runs top to bottom on a fresh kernel; outputs are trimmed
- [ ] Reusable code lives in `<module>/src/`, not duplicated across notebook and app
- [ ] `app.py` loads the saved model from `models/` via a path relative to the file, and runs locally
- [ ] `requirements.txt` is pinned (`==`) and lists only what this module imports
- [ ] Live demo works on Streamlit Community Cloud (or the reason it isn't deployed yet is given)
- [ ] README follows `docs/README_TEMPLATE.md`, with a real results table and a screenshot
- [ ] Our approach was compared with the ML-For-Beginners `/solution`; differences noted
- [ ] No secrets, no files over 25 MB, nothing copied from the reference repo
- [ ] CI is green
