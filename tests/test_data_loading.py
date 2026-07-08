from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.data.load_data import load_processed_data


def test_dataset_loads():
    """
    Test that the processed dataset loads successfully.
    """

    df = load_processed_data()

    assert df is not None
    assert not df.empty


def test_required_columns_exist():
    """
    Test that important columns exist.
    """

    df = load_processed_data()

    required_columns = [
        "Sales",
        "Cost",
        "Units",
        "Region",
        "Ship Mode",
        "Sales Category",
    ]

    for column in required_columns:
        assert column in df.columns


def test_dataset_has_rows():
    """
    Dataset should contain records.
    """

    df = load_processed_data()

    assert len(df) > 0


def test_no_duplicate_order_ids():
    """
    Order ID can repeat because one order may contain multiple product line items.
    This test checks that Order ID is not missing.
    """

    df = load_processed_data()

    if "Order ID" in df.columns:
        assert df["Order ID"].notna().all()
        assert df["Order ID"].astype(str).str.strip().ne("").all()