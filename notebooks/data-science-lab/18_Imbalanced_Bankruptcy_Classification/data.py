"""Module for handling data."""

from __future__ import annotations

import json
import gzip

from pathlib import Path
from typing import Any


import pandas as pd


def load_json(path: str | Path) -> Any:
    """Load a JSON file that may be gzip-compressed.

    Parameters
    ----------
    path
        Path to a ``.json`` or ``.json.gz`` file.

    Returns
    -------
    Any
        Parsed JSON (often a dict, sometimes a list).
    """
    p = Path(path)

    if p.suffix == ".gz":
        with gzip.open(p, mode="rt", encoding="utf-8") as f:
            return json.load(f)

    with p.open(mode="rt", encoding="utf-8") as f:
        return json.load(f)


def records_to_frame(records: list[dict[str, Any]]) -> pd.DataFrame:
    """
    Convert a list of record dicts into a DataFrame.

    Parameters
    ----------
    records
        List of dictionaries, one per observation.

    Returns
    -------
    pandas.DataFrame
        DataFrame created from records.
    """
    has_nested = any(isinstance(v, (dict, list)) for r in records for v in r.values())
    if has_nested:
        return pd.json_normalize(records)
    return pd.DataFrame.from_records(records)


def extract_records(payload: Any) -> list[dict[str, Any]]:
    """
    Extract the list of record dictionaries from the dataset payload.

    Parameters
    ----------
    payload
        Parsed JSON payload (expected: dict with records under a known key).

    Returns
    -------
    list of dict
        The dataset records.

    Raises
    ------
    KeyError
        If neither ``data`` nor ``observations`` is present.
    TypeError
        If the record container exists but is not a list of dicts.
    """
    if not isinstance(payload, dict):
        raise TypeError("Expected the JSON payload to be a dict.")

    if "data" in payload:
        records = payload["data"]
    elif "observations" in payload:
        records = payload["observations"]
    else:
        raise KeyError(
            "Could not find records. Expected key 'data' or 'observations'. "
            f"Found keys: {list(payload.keys())}"
        )

    if not isinstance(records, list):
        raise TypeError("Expected the records container to be a list.")

    if records and not isinstance(records[0], dict):
        raise TypeError("Expected records to be a list of dicts.")

    return records


def normalize_columns(columns: list[str]) -> list[str]:
    """
    Normalize column names to a consistent snake_case style.

    Parameters
    ----------
    columns
        Original column names.

    Returns
    -------
    list of str
        Normalized column names.
    """
    out: list[str] = []
    for c in columns:
        c2 = str(c).strip().lower()
        c2 = c2.replace(" ", "_").replace("-", "_")
        c2 = "".join(ch for ch in c2 if ch.isalnum() or ch == "_")
        while "__" in c2:
            c2 = c2.replace("__", "_")
        out.append(c2)
    return out


def clean_financials(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset for modeling (simple version).

    Parameters
    ----------
    df
        Raw DataFrame extracted from JSON.

    Returns
    -------
    pandas.DataFrame
        Cleaned DataFrame with normalized columns and numeric values where
        possible.
    """
    df2 = df.copy()
    df2.columns = normalize_columns([str(c) for c in df2.columns])

    for col in df2.columns:
        df2[col] = pd.to_numeric(df2[col], errors="coerce")

    return df2


def wrangle(path: str | Path) -> pd.DataFrame:
    """
    Load + transform a bankruptcy dataset into a clean DataFrame.

    Parameters
    ----------
    path
        Path to a ``.json`` or ``.json.gz`` file.

    Returns
    -------
    pandas.DataFrame
        Cleaned DataFrame ready for analysis.
    """
    payload = load_json(path)
    records = extract_records(payload)
    df_raw = records_to_frame(records)
    return clean_financials(df_raw)
