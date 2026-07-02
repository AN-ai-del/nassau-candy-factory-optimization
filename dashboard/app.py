import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Factory Optimization Dashboard",
    layout="wide"
)

DATA_PATH = Path("../data/processed")
MODEL_PATH = Path("../models")

df = pd.read_csv(DATA_PATH / "factory_sales_feature_engineered.csv")
model = joblib.load(MODEL_PATH / "gradient_boosting_model.pkl")

features = [
    "Sales", "Cost", "Units", "High Value Order",
    "Order Year", "Order Month", "Order Quarter", "Is Weekend",
    "Ship Mode", "Region", "Sales Category"
]

X = df[features]

X_encoded = pd.get_dummies(
    X,
    columns=["Ship Mode", "Region", "Sales Category"],
    drop_first=True
)

X_encoded = X_encoded.reindex(
    columns=model.feature_names_in_,
    fill_value=0
)

df["Predicted Profit"] = model.predict(X_encoded)

st.title("🏭 Factory Optimization Dashboard")

st.markdown(
    """
    Interactive machine learning dashboard for factory profit optimization.
    """
)

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

ship = st.sidebar.multiselect(
    "Ship Mode",
    df["Ship Mode"].unique(),
    default=df["Ship Mode"].unique()
)

category = st.sidebar.multiselect(
    "Sales Category",
    df["Sales Category"].unique(),
    default=df["Sales Category"].unique()
)

filtered = df[
    (df["Region"].isin(region)) &
    (df["Ship Mode"].isin(ship)) &
    (df["Sales Category"].isin(category))
]

st.sidebar.download_button(
    "⬇ Download Filtered Data",
    filtered.to_csv(index=False),
    file_name="factory_predictions.csv",
    mime="text/csv"
)

avg_profit = filtered["Predicted Profit"].mean()
highest_profit = filtered["Predicted Profit"].max()
best_region = filtered.groupby("Region")["Predicted Profit"].mean().idxmax()
best_ship = filtered.groupby("Ship Mode")["Predicted Profit"].mean().idxmax()
best_category = filtered.groupby("Sales Category")["Predicted Profit"].mean().idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Profit", f"${avg_profit:.2f}")
col2.metric("Highest Profit", f"${highest_profit:.2f}")
col3.metric("Best Region", best_region)
col4.metric("Best Ship Mode", best_ship)

st.subheader("📈 Predicted Profit Distribution")

fig = px.histogram(
    filtered,
    x="Predicted Profit",
    nbins=30,
    title="Distribution of Predicted Profit",
    hover_data=["Predicted Profit"]
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🌍 Regional Performance")

region_chart = (
    filtered.groupby("Region")["Predicted Profit"]
    .mean()
    .reset_index()
    .sort_values("Predicted Profit")
)

fig = px.bar(
    region_chart,
    x="Predicted Profit",
    y="Region",
    orientation="h",
    color="Predicted Profit",
    color_continuous_scale="Viridis",
    title="Average Predicted Profit by Region",
    hover_name="Region"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🚚 Shipping Mode Performance")

ship_chart = (
    filtered.groupby("Ship Mode")["Predicted Profit"]
    .mean()
    .reset_index()
    .sort_values("Predicted Profit")
)

fig = px.bar(
    ship_chart,
    x="Predicted Profit",
    y="Ship Mode",
    orientation="h",
    color="Predicted Profit",
    color_continuous_scale="Viridis",
    title="Average Predicted Profit by Shipping Mode",
    hover_name="Ship Mode"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📦 Sales Category Performance")

category_chart = (
    filtered.groupby("Sales Category")["Predicted Profit"]
    .mean()
    .reset_index()
    .sort_values("Predicted Profit")
)

fig = px.bar(
    category_chart,
    x="Predicted Profit",
    y="Sales Category",
    orientation="h",
    color="Predicted Profit",
    color_continuous_scale="Viridis",
    title="Average Predicted Profit by Sales Category",
    hover_name="Sales Category"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🍩 Order Distribution by Region")

region_count = filtered["Region"].value_counts().reset_index()
region_count.columns = ["Region", "Order Count"]

fig = px.pie(
    region_count,
    names="Region",
    values="Order Count",
    hole=0.45,
    title="Order Distribution by Region"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🏆 Top Recommended Orders")

top_orders = (
    filtered.sort_values("Predicted Profit", ascending=False)
    [[
        "Order ID",
        "Region",
        "Ship Mode",
        "Sales",
        "Units",
        "Predicted Profit"
    ]]
    .head(10)
)

st.dataframe(top_orders, use_container_width=True)

st.subheader("📋 Executive Recommendation")

st.success(f"""
### Recommended Strategy

✅ Prioritize production in **{best_region}**

✅ Prefer **{best_ship}** shipping

✅ Focus on **{best_category}** sales category

### Executive Summary

- **{best_region}** generates the highest average predicted profit.
- **{best_ship}** provides the strongest expected shipping return.
- **{best_category}** sales category shows the highest profitability.
- The recommended strategy supports better factory allocation, shipment planning, and profit optimization.
""")

st.markdown("---")

st.markdown(
    """
    **Factory Optimization Dashboard**  
    Machine Learning • Gradient Boosting • Business Recommendation System  

    Developed by **Anushka Das**
    """
)