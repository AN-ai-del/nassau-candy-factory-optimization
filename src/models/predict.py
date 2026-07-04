import pandas as pd
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "models" / "gradient_boosting_model.pkl"

model = joblib.load(MODEL_PATH)

FEATURES = [
    "Sales",
    "Cost",
    "Units",
    "High Value Order",
    "Order Year",
    "Order Month",
    "Order Quarter",
    "Is Weekend",
    "Ship Mode",
    "Region",
    "Sales Category"
]


def prepare_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare input data so it matches the features used during model training.
    """

    x = data[FEATURES]

    x_encoded = pd.get_dummies(
        x,
        columns=["Ship Mode", "Region", "Sales Category"],
        drop_first=True
    )

    x_encoded = x_encoded.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    return x_encoded


def predict_profit(data: pd.DataFrame):
    """
    Predict profit for a dataframe of factory orders.
    """

    x_encoded = prepare_features(data)
    predictions = model.predict(x_encoded)

    return predictions


def predict_single_order(
    sales: float,
    cost: float,
    units: int,
    region: str,
    ship_mode: str,
    sales_category: str,
    high_value_order: int = 1,
    order_year: int = 2024,
    order_month: int = 6,
    order_quarter: int = 2,
    is_weekend: int = 0
) -> float:
    """
    Predict profit for one factory order scenario.
    """

    sample = pd.DataFrame([{
        "Sales": sales,
        "Cost": cost,
        "Units": units,
        "High Value Order": high_value_order,
        "Order Year": order_year,
        "Order Month": order_month,
        "Order Quarter": order_quarter,
        "Is Weekend": is_weekend,
        "Ship Mode": ship_mode,
        "Region": region,
        "Sales Category": sales_category
    }])

    prediction = predict_profit(sample)[0]

    return float(prediction)