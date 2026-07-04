import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def profit_distribution_chart(data):
    return px.histogram(
        data,
        x="Predicted Profit",
        nbins=30,
        title="Distribution of Predicted Profit"
    )


def region_profit_chart(data):
    region_chart = (
        data.groupby("Region")["Predicted Profit"]
        .mean()
        .reset_index()
        .sort_values("Predicted Profit")
    )

    return px.bar(
        region_chart,
        x="Predicted Profit",
        y="Region",
        orientation="h",
        color="Predicted Profit",
        color_continuous_scale="Viridis",
        title="Average Predicted Profit by Region"
    )


def shipping_profit_chart(data):
    ship_chart = (
        data.groupby("Ship Mode")["Predicted Profit"]
        .mean()
        .reset_index()
        .sort_values("Predicted Profit")
    )

    return px.bar(
        ship_chart,
        x="Predicted Profit",
        y="Ship Mode",
        orientation="h",
        color="Predicted Profit",
        color_continuous_scale="Viridis",
        title="Average Predicted Profit by Shipping Mode"
    )


def sales_category_profit_chart(data):
    category_chart = (
        data.groupby("Sales Category")["Predicted Profit"]
        .mean()
        .reset_index()
        .sort_values("Predicted Profit")
    )

    return px.bar(
        category_chart,
        x="Predicted Profit",
        y="Sales Category",
        orientation="h",
        color="Predicted Profit",
        color_continuous_scale="Viridis",
        title="Average Predicted Profit by Sales Category"
    )


def region_distribution_chart(data):
    region_count = data["Region"].value_counts().reset_index()
    region_count.columns = ["Region", "Order Count"]

    return px.pie(
        region_count,
        names="Region",
        values="Order Count",
        hole=0.45,
        title="Order Distribution by Region"
    )


def sales_growth_simulation_chart(simulation_df: pd.DataFrame):
    return px.line(
        simulation_df,
        x="Sales",
        y="Predicted Profit",
        markers=True,
        title="Impact of Sales on Predicted Profit"
    )


def profit_gauge(predicted_profit, max_profit, median_profit, high_profit_threshold):
    return go.Figure(go.Indicator(
        mode="gauge+number",
        value=predicted_profit,
        title={"text": "Profit Opportunity Score"},
        gauge={
            "axis": {"range": [0, max_profit]},
            "bar": {"color": "#00cc96"},
            "steps": [
                {"range": [0, median_profit], "color": "#ffcccc"},
                {"range": [median_profit, high_profit_threshold], "color": "#fff3cd"},
                {"range": [high_profit_threshold, max_profit], "color": "#d4edda"}
            ]
        }
    ))