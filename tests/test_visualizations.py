from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

import pandas as pd
import plotly.graph_objects as go

from src.visualization.plots import (
    profit_distribution_chart,
    region_profit_chart,
    shipping_profit_chart,
    sales_category_profit_chart,
    region_distribution_chart,
    sales_growth_simulation_chart,
    profit_gauge,
)


def sample_data():
    return pd.DataFrame({
        "Predicted Profit": [10.5, 20.0, 35.5, 50.0],
        "Region": ["Atlantic", "Pacific", "Atlantic", "Gulf"],
        "Ship Mode": ["First Class", "Second Class", "Standard Class", "Same Day"],
        "Sales Category": ["Low", "Medium", "High", "High"],
    })


def test_profit_distribution_chart_returns_figure():
    fig = profit_distribution_chart(sample_data())
    assert isinstance(fig, go.Figure)


def test_region_profit_chart_returns_figure():
    fig = region_profit_chart(sample_data())
    assert isinstance(fig, go.Figure)


def test_shipping_profit_chart_returns_figure():
    fig = shipping_profit_chart(sample_data())
    assert isinstance(fig, go.Figure)


def test_sales_category_profit_chart_returns_figure():
    fig = sales_category_profit_chart(sample_data())
    assert isinstance(fig, go.Figure)


def test_region_distribution_chart_returns_figure():
    fig = region_distribution_chart(sample_data())
    assert isinstance(fig, go.Figure)


def test_sales_growth_simulation_chart_returns_figure():
    simulation_df = pd.DataFrame({
        "Sales": [100, 150, 200, 250],
        "Predicted Profit": [40, 60, 80, 100],
    })

    fig = sales_growth_simulation_chart(simulation_df)
    assert isinstance(fig, go.Figure)


def test_profit_gauge_returns_figure():
    fig = profit_gauge(
        predicted_profit=129.17,
        max_profit=150,
        median_profit=75,
        high_profit_threshold=120,
    )

    assert isinstance(fig, go.Figure)


def test_profit_gauge_has_indicator():
    fig = profit_gauge(
        predicted_profit=129.17,
        max_profit=150,
        median_profit=75,
        high_profit_threshold=120,
    )

    assert fig.data[0].type == "indicator"