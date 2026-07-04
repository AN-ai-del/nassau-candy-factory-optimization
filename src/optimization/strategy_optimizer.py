import itertools

from src.optimization.recommendation_engine import recommend_strategy


def find_best_strategy(
    sales,
    cost,
    units,
    regions,
    ship_modes,
    sales_categories,
):
    """
    Searches every possible combination and
    returns the highest predicted profit.
    """

    best = None

    for region, ship_mode, category in itertools.product(
        regions,
        ship_modes,
        sales_categories,
    ):

        result = recommend_strategy(
            sales=sales,
            cost=cost,
            units=units,
            region=region,
            ship_mode=ship_mode,
            sales_category=category,
            high_value_order=1,
        )

        if best is None or result["Predicted Profit"] > best["Predicted Profit"]:

            best = {
                "Region": region,
                "Ship Mode": ship_mode,
                "Sales Category": category,
                **result,
            }

    return best