from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

import pandas as pd

from src.data.load_data import load_processed_data


def test_dataset_is_dataframe():
    """
    Loaded dataset should be a pandas DataFrame.
    """

    df = load_processed_data()

    assert isinstance(df, pd.DataFrame)


def test_dataset_not_empty():
    """
    Dataset should contain records.
    """

    df = load_processed_data()

    assert len(df) > 0


def test_required_columns_exist():
    """
    Verify essential columns exist.
    """

    df = load_processed_data()

    required_columns = [
        "Order ID",
        "Region",
        "Ship Mode",
        "Sales",
        "Units",
        "Cost",
        "Sales Category",
        "High Value Order"
    ]

    for column in required_columns:
        assert column in df.columns


def test_numeric_columns_are_numeric():
    """
    Numeric columns should have numeric dtype.
    """

    df = load_processed_data()

    numeric_columns = [
        "Sales",
        "Units",
        "Cost",
        "Profit Margin (%)",
        "Profit Per Unit",
        "Cost Percentage (%)"
    ]

    for column in numeric_columns:
        assert pd.api.types.is_numeric_dtype(df[column])


def test_no_duplicate_column_names():
    """
    Dataset should not contain duplicate column names.
    """

    df = load_processed_data()

    assert len(df.columns) == len(set(df.columns))


def test_sales_are_non_negative():
    """
    Sales values should not be negative.
    """

    df = load_processed_data()

    assert (df["Sales"] >= 0).all()


def test_units_are_positive():
    """
    Units should always be positive.
    """

    df = load_processed_data()

    assert (df["Units"] > 0).all()


def test_cost_is_non_negative():
    """
    Cost should not be negative.
    """

    df = load_processed_data()

    assert (df["Cost"] >= 0).all()


def test_region_has_values():
    """
    Region column should not contain missing values.
    """

    df = load_processed_data()

    assert df["Region"].notna().all()


def test_ship_mode_has_values():
    """
    Shipping mode should not contain missing values.
    """

    df = load_processed_data()

    assert df["Ship Mode"].notna().all()


def test_sales_category_has_values():
    """
    Sales Category should not contain missing values.
    """

    df = load_processed_data()

    assert df["Sales Category"].notna().all()


def test_high_value_order_is_binary():
    """
    High Value Order should only contain 0 or 1.
    """

    df = load_processed_data()

    values = set(df["High Value Order"].unique())

    assert values.issubset({0, 1})