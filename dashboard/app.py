import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Factory Optimization Dashboard",
    page_icon="🏭",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed"
MODEL_PATH = BASE_DIR / "models"

df = pd.read_csv(DATA_PATH / "factory_sales_feature_engineered.csv")
model = joblib.load(MODEL_PATH / "gradient_boosting_model.pkl")

features = [
    "Sales", "Cost", "Units", "High Value Order",
    "Order Year", "Order Month", "Order Quarter", "Is Weekend",
    "Ship Mode", "Region", "Sales Category"
]


def prepare_features(data):
    X = data[features]

    X_encoded = pd.get_dummies(
        X,
        columns=["Ship Mode", "Region", "Sales Category"],
        drop_first=True
    )

    X_encoded = X_encoded.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    return X_encoded


def predict_profit_input(
    sales,
    cost,
    units,
    region,
    ship_mode,
    sales_category,
    high_value_order
):
    sample = pd.DataFrame([{
        "Sales": sales,
        "Cost": cost,
        "Units": units,
        "High Value Order": int(high_value_order),
        "Order Year": 2024,
        "Order Month": 6,
        "Order Quarter": 2,
        "Is Weekend": 0,
        "Ship Mode": ship_mode,
        "Region": region,
        "Sales Category": sales_category
    }])

    sample_encoded = prepare_features(sample)
    return model.predict(sample_encoded)[0]


df["Predicted Profit"] = model.predict(prepare_features(df))

st.title("🏭 Factory Optimization Dashboard")

st.markdown(
    """
    Interactive AI-powered dashboard for factory profit prediction, 
    business simulation, and decision support.
    """
)

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

ship = st.sidebar.multiselect(
    "Ship Mode",
    sorted(df["Ship Mode"].unique()),
    default=sorted(df["Ship Mode"].unique())
)

category = st.sidebar.multiselect(
    "Sales Category",
    sorted(df["Sales Category"].unique()),
    default=sorted(df["Sales Category"].unique())
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

if filtered.empty:
    st.warning("No data available for selected filters.")
    st.stop()

avg_profit = filtered["Predicted Profit"].mean()
highest_profit = filtered["Predicted Profit"].max()
best_region = filtered.groupby("Region")["Predicted Profit"].mean().idxmax()
best_ship = filtered.groupby("Ship Mode")["Predicted Profit"].mean().idxmax()
best_category = filtered.groupby("Sales Category")["Predicted Profit"].mean().idxmax()
max_profit = float(df["Predicted Profit"].max())
median_profit = float(df["Predicted Profit"].median())
high_profit_threshold = float(df["Predicted Profit"].quantile(0.75))

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Average Profit", f"${avg_profit:.2f}")
col2.metric("🏆 Highest Profit", f"${highest_profit:.2f}")
col3.metric("🌍 Best Region", best_region)
col4.metric("🚚 Best Ship Mode", best_ship)

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([
    "🤖 Live Prediction",
    "📊 Overview",
    "📈 Analytics",
    "🎯 Recommendations"
])

with tab1:
    st.subheader("🤖 Live Profit Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        input_sales = st.slider("Sales", 0, 500, 250)
        input_cost = st.slider("Cost", 0, 300, 110)

    with col2:
        input_units = st.slider("Units", 1, 30, 15)
        input_region = st.selectbox("Region", sorted(df["Region"].unique()))

    with col3:
        input_ship_mode = st.selectbox("Ship Mode", sorted(df["Ship Mode"].unique()))
        input_sales_category = st.selectbox("Sales Category", sorted(df["Sales Category"].unique()))
        input_high_value = st.checkbox("High Value Order", value=True)

    predicted_profit = predict_profit_input(
        input_sales,
        input_cost,
        input_units,
        input_region,
        input_ship_mode,
        input_sales_category,
        input_high_value
    )

    if predicted_profit >= high_profit_threshold:
        status = "Excellent"
        action = "Prioritize this order"
        box = st.success
    elif predicted_profit >= median_profit:
        status = "Moderate"
        action = "Acceptable order"
        box = st.info
    else:
        status = "Low"
        action = "Review before prioritizing"
        box = st.warning

    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric("💵 Predicted Profit", f"${predicted_profit:.2f}")
        st.progress(min(predicted_profit / max_profit, 1.0))
        box(f"**Status:** {status}  \n**Action:** {action}")

    with col2:
        gauge = go.Figure(go.Indicator(
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

        st.plotly_chart(gauge, use_container_width=True)

    st.subheader("📊 Live Sales Growth Simulation")

    sales_values = [100, 150, 200, 250, 300, 350, 400]
    profits = []

    for sale in sales_values:
        profit = predict_profit_input(
            sale,
            input_cost,
            input_units,
            input_region,
            input_ship_mode,
            input_sales_category,
            input_high_value
        )
        profits.append(profit)

    simulation_df = pd.DataFrame({
        "Sales": sales_values,
        "Predicted Profit": profits
    })

    fig = px.line(
        simulation_df,
        x="Sales",
        y="Predicted Profit",
        markers=True,
        title="Impact of Sales on Predicted Profit"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🧠 AI Prediction Insight")

    st.info(f"""
    The model predicts **${predicted_profit:.2f}** profit for this order.

    **Selected Scenario**
    - Region: **{input_region}**
    - Shipping Mode: **{input_ship_mode}**
    - Sales Category: **{input_sales_category}**
    - Status: **{status}**
    - Recommended Action: **{action}**
    """)

with tab2:
    st.subheader("📈 Predicted Profit Distribution")

    fig = px.histogram(
        filtered,
        x="Predicted Profit",
        nbins=30,
        title="Distribution of Predicted Profit"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🌍 Regional Profit Overview")

    region_chart = (
        filtered.groupby("Region")["Predicted Profit"]
        .mean()
        .reset_index()
        .sort_values("Predicted Profit", ascending=False)
    )

    fig = px.bar(
        region_chart,
        x="Region",
        y="Predicted Profit",
        color="Region",
        title="Average Predicted Profit by Region"
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

with tab3:
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
        title="Average Predicted Profit by Region"
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
        title="Average Predicted Profit by Shipping Mode"
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
        title="Average Predicted Profit by Sales Category"
    )

    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("🎯 AI Recommendation Cards")

    card1, card2, card3, card4 = st.columns(4)

    card1.metric("🌍 Best Region", best_region)
    card2.metric("🚚 Best Shipping", best_ship)
    card3.metric("📦 Best Category", best_category)
    card4.metric("🏆 Highest Profit", f"${highest_profit:.2f}")

    st.subheader("🏆 Top Recommended Orders")

    top_orders = (
        filtered.sort_values("Predicted Profit", ascending=False)
        [[
            "Order ID",
            "Region",
            "Ship Mode",
            "Sales",
            "Units",
            "Sales Category",
            "Predicted Profit"
        ]]
        .head(10)
    )

    st.dataframe(
        top_orders,
        use_container_width=True,
        hide_index=True
    )

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
    - The highest predicted profit opportunity is **${highest_profit:.2f}**.
    - Sales and units strongly influence expected profit.
    - The dashboard supports factory allocation, shipment planning, and business decision-making.
    """)

    st.subheader("🧠 AI Business Insights")

    st.info(f"""
    The model recommends focusing on **{best_region}**, using **{best_ship}**, 
    and prioritizing **{best_category}** sales opportunities.

    This combination is expected to maximize profit based on historical factory sales patterns.
    """)

st.markdown("---")

st.markdown(
    """
    **Factory Optimization Dashboard**  

    Machine Learning • Gradient Boosting • Scikit-Learn • Streamlit • Plotly • Business Recommendation System  

    Developed by **Anushka Das**
    """
)