from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.models.predict import (
    predict_profit,
    predict_single_order,
)

from src.data.load_data import load_processed_data


def test_model_returns_prediction():
    """
    The trained model should return one prediction
    for every row in the dataset.
    """

    df = load_processed_data()

    predictions = predict_profit(df)

    assert len(predictions) == len(df)


def test_prediction_is_numeric():
    """
    Predictions should be numeric.
    """

    df = load_processed_data()

    predictions = predict_profit(df)

    assert predictions.dtype.kind in "fi"


def test_single_prediction():
    """
    Test prediction for a single order.
    """

    prediction = predict_single_order(
        sales=250,
        cost=110,
        units=15,
        region="Pacific",
        ship_mode="Second Class",
        sales_category="High"
    )

    assert isinstance(prediction, float)


def test_prediction_positive():
    """
    Profit should be within a realistic range.
    """

    prediction = predict_single_order(
        sales=250,
        cost=110,
        units=15,
        region="Pacific",
        ship_mode="Second Class",
        sales_category="High"
    )

    assert prediction > -1000
    assert prediction < 100000