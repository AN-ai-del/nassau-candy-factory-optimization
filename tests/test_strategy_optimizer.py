from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.optimization.strategy_optimizer import find_best_strategy


def test_returns_dictionary():
    """
    Strategy optimizer should return a dictionary.
    """

    result = find_best_strategy(
        sales=250,
        cost=110,
        units=15,
        regions=["Atlantic", "Pacific"],
        ship_modes=["First Class", "Second Class"],
        sales_categories=["High", "Medium"]
    )

    assert isinstance(result, dict)


def test_required_keys_exist():
    """
    Verify all expected keys exist.
    """

    result = find_best_strategy(
        sales=250,
        cost=110,
        units=15,
        regions=["Atlantic", "Pacific"],
        ship_modes=["First Class", "Second Class"],
        sales_categories=["High", "Medium"]
    )

    required = [
        "Region",
        "Ship Mode",
        "Sales Category",
        "Predicted Profit",
        "Recommendation",
        "Risk"
    ]

    for key in required:
        assert key in result


def test_profit_is_numeric():
    """
    Best predicted profit should be numeric.
    """

    result = find_best_strategy(
        sales=250,
        cost=110,
        units=15,
        regions=["Atlantic", "Pacific"],
        ship_modes=["First Class", "Second Class"],
        sales_categories=["High", "Medium"]
    )

    assert isinstance(result["Predicted Profit"], float)


def test_region_valid():
    """
    Returned region should come from the supplied list.
    """

    regions = ["Atlantic", "Pacific"]

    result = find_best_strategy(
        sales=250,
        cost=110,
        units=15,
        regions=regions,
        ship_modes=["First Class", "Second Class"],
        sales_categories=["High", "Medium"]
    )

    assert result["Region"] in regions


def test_ship_mode_valid():
    """
    Returned shipping mode should come from the supplied list.
    """

    ship_modes = ["First Class", "Second Class"]

    result = find_best_strategy(
        sales=250,
        cost=110,
        units=15,
        regions=["Atlantic", "Pacific"],
        ship_modes=ship_modes,
        sales_categories=["High", "Medium"]
    )

    assert result["Ship Mode"] in ship_modes


def test_sales_category_valid():
    """
    Returned sales category should come from the supplied list.
    """

    categories = ["High", "Medium"]

    result = find_best_strategy(
        sales=250,
        cost=110,
        units=15,
        regions=["Atlantic", "Pacific"],
        ship_modes=["First Class", "Second Class"],
        sales_categories=categories
    )

    assert result["Sales Category"] in categories