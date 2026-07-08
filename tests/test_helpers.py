from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.utils.helpers import (
    format_currency,
    classify_profit_opportunity,
)


# ---------------------------------------------------------
# format_currency()
# ---------------------------------------------------------

def test_currency_returns_string():
    """
    Currency formatter should return a string.
    """

    value = format_currency(129.1678)

    assert isinstance(value, str)


def test_currency_rounding():
    """
    Currency should round to two decimal places.
    """

    value = format_currency(129.1678)

    assert value == "$129.17"


def test_currency_zero():
    """
    Zero should be formatted correctly.
    """

    value = format_currency(0)

    assert value == "$0.00"


def test_currency_negative():
    """
    Negative values should also format correctly.
    """

    value = format_currency(-25.5)

    assert value == "$-25.50"


# ---------------------------------------------------------
# classify_profit_opportunity()
# ---------------------------------------------------------

def test_excellent_classification():
    """
    Very high profit should be classified as Excellent.
    """

    level, recommendation, risk = classify_profit_opportunity(
        predicted_profit=150,
        median_profit=75,
        high_profit_threshold=120
    )

    assert level == "Excellent"
    assert recommendation == "Prioritize this order"
    assert risk == "Low"


def test_moderate_classification():
    """
    Medium profit should be Moderate.
    """

    level, recommendation, risk = classify_profit_opportunity(
        predicted_profit=90,
        median_profit=75,
        high_profit_threshold=120
    )

    assert level == "Moderate"
    assert recommendation == "Acceptable order"
    assert risk == "Medium"


def test_low_classification():
    """
    Low profit should be classified as Low.
    """

    level, recommendation, risk = classify_profit_opportunity(
        predicted_profit=40,
        median_profit=75,
        high_profit_threshold=120
    )

    assert level == "Low"
    assert recommendation == "Review before prioritizing"
    assert risk == "High"


def test_boundary_high_profit():
    """
    Threshold value should still be Excellent.
    """

    level, _, risk = classify_profit_opportunity(
        predicted_profit=120,
        median_profit=75,
        high_profit_threshold=120
    )

    assert level == "Excellent"
    assert risk == "Low"


def test_boundary_median_profit():
    """
    Median value should still be Moderate.
    """

    level, _, risk = classify_profit_opportunity(
        predicted_profit=75,
        median_profit=75,
        high_profit_threshold=120
    )

    assert level == "Moderate"
    assert risk == "Medium"


def test_function_returns_three_values():
    """
    Helper should always return exactly three values.
    """

    result = classify_profit_opportunity(
        predicted_profit=100,
        median_profit=75,
        high_profit_threshold=120
    )

    assert len(result) == 3