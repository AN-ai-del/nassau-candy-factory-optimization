"""
Business Recommendation Engine

Generates actionable recommendations based on
predicted profit.
"""

from src.models.predict import predict_single_order


def recommend_strategy(
    sales: float,
    cost: float,
    units: int,
    region: str,
    ship_mode: str,
    sales_category: str,
    high_value_order: int,
):
    """
    Returns:
        predicted_profit
        recommendation
        risk
    """

    predicted_profit = predict_single_order(
        sales=sales,
        cost=cost,
        units=units,
        region=region,
        ship_mode=ship_mode,
        sales_category=sales_category,
        high_value_order=high_value_order,
    )

    # Business rules
    if predicted_profit >= 120:
        recommendation = (
            "Highly Recommended. Prioritize this order for production and shipping."
        )
        risk = "Low"

    elif predicted_profit >= 90:
        recommendation = (
            "Profitable order. Accept with standard planning."
        )
        risk = "Medium"

    elif predicted_profit >= 60:
        recommendation = (
            "Moderate profitability. Review production cost before accepting."
        )
        risk = "Medium"

    else:
        recommendation = (
            "Low expected profit. Reconsider pricing, shipping, or production."
        )
        risk = "High"

    return {
        "Predicted Profit": round(predicted_profit, 2),
        "Recommendation": recommendation,
        "Risk": risk,
    }