import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import streamlit as st
import pandas as pd

from src.data.load_data import load_processed_data
from src.models.predict import predict_profit
from src.optimization.recommendation_engine import recommend_strategy
from src.optimization.strategy_optimizer import find_best_strategy
from src.utils.helpers import format_currency, classify_profit_opportunity
from src.visualization.plots import (
    profit_distribution_chart,
    region_profit_chart,
    shipping_profit_chart,
    sales_category_profit_chart,
    region_distribution_chart,
    sales_growth_simulation_chart,
    profit_gauge,
)


st.set_page_config(
    page_title="Factory Optimization Dashboard",
    page_icon="🏭",
    layout="wide"
)

df = load_processed_data()
df["Predicted Profit"] = predict_profit(df)

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

col1.metric("💰 Average Profit", format_currency(avg_profit))
col2.metric("🏆 Highest Profit", format_currency(highest_profit))
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

    recommendation = recommend_strategy(
        sales=input_sales,
        cost=input_cost,
        units=input_units,
        region=input_region,
        ship_mode=input_ship_mode,
        sales_category=input_sales_category,
        high_value_order=int(input_high_value)
    )

    predicted_profit = recommendation["Predicted Profit"]

    status, action, risk = classify_profit_opportunity(
        predicted_profit,
        median_profit,
        high_profit_threshold
    )

    left, right = st.columns([1, 2])

    with left:
        st.metric("💵 Predicted Profit", format_currency(predicted_profit))
        st.progress(min(predicted_profit / max_profit, 1.0))

        message = f"""
**Status:** {status}

**Action:** {action}

**AI Recommendation:** {recommendation['Recommendation']}

**Risk Level:** {recommendation['Risk']}
"""

        if risk == "Low":
            st.success(message)
        elif risk == "Medium":
            st.info(message)
        else:
            st.warning(message)

    with right:
        st.plotly_chart(
            profit_gauge(
                predicted_profit,
                max_profit,
                median_profit,
                high_profit_threshold
            ),
            width="stretch",
            key="live_profit_gauge"
        )

    st.subheader("📊 Live Sales Growth Simulation")

    sales_values = [100, 150, 200, 250, 300, 350, 400]
    profits = []

    for sale in sales_values:
        result = recommend_strategy(
            sales=sale,
            cost=input_cost,
            units=input_units,
            region=input_region,
            ship_mode=input_ship_mode,
            sales_category=input_sales_category,
            high_value_order=int(input_high_value)
        )
        profits.append(result["Predicted Profit"])

    simulation_df = pd.DataFrame({
        "Sales": sales_values,
        "Predicted Profit": profits
    })

    st.plotly_chart(
        sales_growth_simulation_chart(simulation_df),
        width="stretch",
        key="live_sales_growth_simulation"
    )

    st.subheader("🧠 AI Prediction Insight")

    st.info(f"""
### 💰 Predicted Profit

**{format_currency(predicted_profit)}**

---

### 📋 AI Recommendation

{recommendation['Recommendation']}

---

### ⚠ Risk Level

**{recommendation['Risk']}**

---

### Selected Scenario

- Region: **{input_region}**
- Shipping Mode: **{input_ship_mode}**
- Sales Category: **{input_sales_category}**
- High Value Order: **{'Yes' if input_high_value else 'No'}**
""")

with tab2:
    st.subheader("📈 Predicted Profit Distribution")

    st.plotly_chart(
        profit_distribution_chart(filtered),
        width="stretch",
        key="overview_profit_distribution"
    )

    st.subheader("🌍 Regional Profit Overview")

    st.plotly_chart(
        region_profit_chart(filtered),
        width="stretch",
        key="overview_region_profit"
    )

    st.subheader("🍩 Order Distribution by Region")

    st.plotly_chart(
        region_distribution_chart(filtered),
        width="stretch",
        key="overview_region_distribution"
    )

with tab3:
    st.subheader("🌍 Regional Performance")

    st.plotly_chart(
        region_profit_chart(filtered),
        width="stretch",
        key="analytics_region_profit"
    )

    st.subheader("🚚 Shipping Mode Performance")

    st.plotly_chart(
        shipping_profit_chart(filtered),
        width="stretch",
        key="analytics_shipping_profit"
    )

    st.subheader("📦 Sales Category Performance")

    st.plotly_chart(
        sales_category_profit_chart(filtered),
        width="stretch",
        key="analytics_category_profit"
    )

with tab4:
    st.subheader("🎯 AI Recommendation Cards")

    card1, card2, card3, card4 = st.columns(4)

    card1.metric("🌍 Best Region", best_region)
    card2.metric("🚚 Best Shipping", best_ship)
    card3.metric("📦 Best Category", best_category)
    card4.metric("🏆 Highest Profit", format_currency(highest_profit))

    st.subheader("🧠 Automatic Strategy Optimizer")

    best_strategy = find_best_strategy(
        sales=250,
        cost=110,
        units=15,
        regions=sorted(df["Region"].unique()),
        ship_modes=sorted(df["Ship Mode"].unique()),
        sales_categories=sorted(df["Sales Category"].unique())
    )

    st.success(f"""
### 🏆 Best Strategy Found

✅ **Region:** {best_strategy['Region']}

✅ **Shipping Mode:** {best_strategy['Ship Mode']}

✅ **Sales Category:** {best_strategy['Sales Category']}

✅ **Expected Profit:** {format_currency(best_strategy['Predicted Profit'])}

✅ **Risk Level:** {best_strategy['Risk']}

### AI Recommendation

{best_strategy['Recommendation']}
""")

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
        width="stretch",
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
- The highest predicted profit opportunity is **{format_currency(highest_profit)}**.
- Sales and units strongly influence expected profit.
- The dashboard supports factory allocation, shipment planning, and business decision-making.
""")

    st.subheader("🧠 AI Business Insights")

    st.info(f"""
The model recommends focusing on **{best_region}**, using **{best_ship}**, 
and prioritizing **{best_category}** sales opportunities.

The automatic strategy optimizer also searches across multiple business combinations 
to identify the strongest profit opportunity.
""")

st.markdown("---")

st.markdown(
    """
    **Factory Optimization Dashboard**  

    Machine Learning • Gradient Boosting • Scikit-Learn • Streamlit • Plotly • Business Recommendation System  

    Developed by **Anushka Das**
    """
)