def format_currency(value: float) -> str:
    """
    Format numeric value as currency.
    """
    return f"${value:.2f}"


def classify_profit_opportunity(predicted_profit: float, median_profit: float, high_profit_threshold: float):
    """
    Classify prediction into business opportunity level.
    """
    if predicted_profit >= high_profit_threshold:
        return "Excellent", "Prioritize this order", "Low"

    if predicted_profit >= median_profit:
        return "Moderate", "Acceptable order", "Medium"

    return "Low", "Review before prioritizing", "High"