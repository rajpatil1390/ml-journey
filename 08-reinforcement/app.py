"""Q-Learning Agent: Streamlit app for module 08 (Reinforcement Learning).

Placeholder until the model is trained. Train it in notebooks/, save it to
models/model.joblib, then replace the TODO section with the real UI.

Run from the repo root, the same way Streamlit Community Cloud does:

    streamlit run 08-reinforcement/app.py
"""

from pathlib import Path

import joblib
import streamlit as st

MODULE_DIR = Path(__file__).resolve().parent
MODEL_PATH = MODULE_DIR / "models" / "model.joblib"


@st.cache_resource
def load_model(path: Path):
    """Load the trained model once per server process."""
    return joblib.load(path)


st.set_page_config(page_title="Q-Learning Agent", page_icon="🐺", layout="centered")
st.title("🐺 Q-Learning Agent")
st.caption("ML Journey · Module 08: Reinforcement Learning")

if not MODEL_PATH.exists():
    st.info(
        "Work in progress: no trained model yet. Run the notebook in `notebooks/` "
        f"to create `models/{MODEL_PATH.name}`."
    )
    st.stop()

model = load_model(MODEL_PATH)

# TODO: add input widgets and show the model's prediction.
st.success("Model loaded.")
