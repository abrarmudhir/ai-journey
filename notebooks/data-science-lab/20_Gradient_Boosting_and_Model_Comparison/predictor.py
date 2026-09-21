
from __future__ import annotations

import pickle
from pathlib import Path

import pandas as pd

from data import wrangle

def predict_bankruptcy_prob(
    model_path: str | Path,
    data_path: str | Path,
) -> pd.Series:
    """Predict bankruptcy probabilities for a dataset file.

    Parameters
    ----------
    model_path
        Path to a trained scikit-learn pipeline saved with pickle.
    data_path
        Path to a dataset file compatible with ``wrangle``.

    Returns
    -------
    pd.Series
        Predicted probabilities for class 1 (bankrupt), indexed by row id.
    """
    model_path = Path(model_path)
    data_path = Path(data_path)

    with model_path.open("rb") as f:
        model = pickle.load(f)

    df = wrangle(data_path)
    feat_cols = [c for c in df.columns if c.startswith("feat_")]
    X = df[feat_cols]

    proba = model.predict_proba(X)[:, 1]
    return pd.Series(proba, index=df.index)

if __name__ == "__main__":
    model_path = Path("models/poland_gradient_boosting.pkl")
    data_path = Path("data/poland-bankruptcy-data-2009.json.gz")

    probs = predict_bankruptcy_prob(model_path, data_path)
    print(probs.head())
