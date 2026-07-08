from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

import joblib
import numpy as np

from src.data.load_data import load_processed_data
from src.models.predict import predict_profit


MODEL_PATH = BASE_DIR / "models" / "gradient_boosting_model.pkl"


def test_model_file_exists():
    assert MODEL_PATH.exists()


def test_model_loads_successfully():
    model = joblib.load(MODEL_PATH)
    assert model is not None


def test_model_has_predict_method():
    model = joblib.load(MODEL_PATH)
    assert hasattr(model, "predict")


def test_model_has_feature_names():
    model = joblib.load(MODEL_PATH)
    assert hasattr(model, "feature_names_in_")
    assert len(model.feature_names_in_) > 0


def test_prediction_length_matches_dataset():
    df = load_processed_data()
    predictions = predict_profit(df)

    assert len(predictions) == len(df)


def test_predictions_are_numeric():
    df = load_processed_data()
    predictions = predict_profit(df)

    assert np.issubdtype(predictions.dtype, np.number)


def test_predictions_have_no_nan():
    df = load_processed_data()
    predictions = predict_profit(df)

    assert not np.isnan(predictions).any()


def test_predictions_have_no_infinite_values():
    df = load_processed_data()
    predictions = predict_profit(df)

    assert np.isfinite(predictions).all()


def test_model_feature_count_positive():
    model = joblib.load(MODEL_PATH)

    assert len(model.feature_names_in_) > 0