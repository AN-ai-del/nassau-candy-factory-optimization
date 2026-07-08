from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.optimization.recommendation_engine import recommend_strategy


def test_returns_dictionary():
    """
    Recommendation engine should return a dictionary.
    """

    result = recommend_strategy(
        sales=250,
        cost=110,
        units=15,
        region="Pacific",
        ship_mode="Second Class",
        sales_category="High",
        high_value_order=1
    )

    assert isinstance(result, dict)


def test_required_keys_exist():
    """
    Verify expected keys exist.
    """

    result = recommend_strategy(
        sales=250,
        cost=110,
        units=15,
        region="Pacific",
        ship_mode="Second Class",
        sales_category="High",
        high_value_order=1
    )

    required = [
        "Predicted Profit",
        "Recommendation",
        "Risk"
    ]

    for key in required:
        assert key in result


def test_profit_is_numeric():
    """
    Predicted profit should be numeric.
    """

    result = recommend_strategy(
        sales=250,
        cost=110,
        units=15,
        region="Pacific",
        ship_mode="Second Class",
        sales_category="High",
        high_value_order=1
    )

    assert isinstance(result["Predicted Profit"], float)


def test_recommendation_not_empty():
    """
    Recommendation text should not be empty.
    """

    result = recommend_strategy(
        sales=250,
        cost=110,
        units=15,
        region="Pacific",
        ship_mode="Second Class",
        sales_category="High",
        high_value_order=1
    )

    assert len(result["Recommendation"]) > 0


def test_risk_value():
    """
    Risk should be one of the supported values.
    """

    result = recommend_strategy(
        sales=250,
        cost=110,
        units=15,
        region="Pacific",
        ship_mode="Second Class",
        sales_category="High",
        high_value_order=1
    )

    assert result["Risk"] in [
        "Low",
        "Medium",
        "High"
    ]