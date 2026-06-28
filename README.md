# 🍬 Nassau Candy Factory Reallocation & Shipping Optimization Recommendation System

## 📌 Project Status

🚧 **In Progress**

### Current Milestone

- ✅ Business Understanding
- ✅ Data Preparation & Quality Assessment
- ✅ Exploratory Data Analysis
- ✅ Feature Engineering
- ⏳ Predictive Modeling
- ⏳ Factory Optimization Engine
- ⏳ Recommendation System
- ⏳ Streamlit Dashboard
- ⏳ Final Research Report

---

# Project Overview

This project develops an intelligent recommendation system for **Nassau Candy Distributor** to optimize factory-product assignments and improve shipping efficiency.

Instead of relying on static factory allocation rules, the system leverages **data analysis, feature engineering, machine learning, and optimization techniques** to support better operational decision-making.

The project combines predictive analytics, optimization algorithms, and interactive business intelligence into a complete decision-support platform for factory reallocation.

---

# Business Problem

Current factory assignments are primarily based on historical operational practices rather than data-driven optimization.

This can lead to:

- Increased shipping lead times
- Higher logistics costs
- Uneven factory utilization
- Lower operational efficiency
- Reduced profitability
- Limited ability to evaluate alternative factory assignments

The objective is to build a recommendation engine capable of evaluating different factory allocation scenarios before implementation.

---

# Project Objectives

The project aims to:

- Analyze historical sales and shipping data
- Perform exploratory business analysis
- Engineer predictive business features
- Build machine learning models
- Simulate factory reassignment scenarios
- Recommend optimal factory allocations
- Balance shipping efficiency and profitability
- Build an interactive decision-support dashboard

---

# Dataset

The project uses a transactional dataset containing approximately **10,000+ customer orders**.

### Dataset Features

- Order Information
- Customer Information
- Product Information
- Sales
- Gross Profit
- Cost
- Units Sold
- Shipping Mode
- Geographic Information
- Factory Information

Additional factory coordinate information will be integrated during the optimization stage.

---

# Project Structure

```text
NASSAU-CANDY-FACTORY-OPTIMIZATION
│
├── config/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   ├── 01_Data_Preparation.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Predictive_Modeling.ipynb
│   ├── 05_Factory_Optimization.ipynb
│   ├── 06_Recommendation_System.ipynb
│   └── 07_Model_Evaluation_and_Insights.ipynb
│
├── reports/
│   ├── executive_summary/
│   ├── figures/
│   └── research_paper/
│
├── src/
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# Current Progress

| Phase | Status |
|--------|--------|
| Business Understanding | ✅ Complete |
| Data Preparation | ✅ Complete |
| Exploratory Data Analysis | ✅ Complete |
| Feature Engineering | ✅ Complete |
| Predictive Modeling | ⏳ In Progress |
| Factory Optimization | ⏳ Pending |
| Recommendation System | ⏳ Pending |
| Dashboard Development | ⏳ Pending |
| Research Paper | ⏳ Pending |

---

# Completed Work

## ✅ Business Understanding

Completed:

- Defined the business objective
- Identified operational challenges
- Established project scope
- Documented expected business impact
- Created project roadmap

---

## ✅ Data Preparation & Quality Assessment

Completed:

- Loaded the raw dataset
- Validated dataset structure
- Checked data types
- Identified missing values
- Removed duplicate records
- Examined numerical distributions
- Performed quality assessment
- Documented data issues

---

## ✅ Exploratory Data Analysis

Completed:

- Sales distribution analysis
- Product performance analysis
- Gross profit analysis
- Regional sales analysis
- Shipping mode analysis
- Monthly sales trend analysis
- Sales vs Profit comparison
- Business insight generation
- Data visualization

---

## ✅ Feature Engineering

Created machine learning-ready features including:

### Date Features

- Order Year
- Order Month
- Order Month Name
- Order Quarter
- Order Weekday
- Weekend Indicator

### Financial Features

- Profit Margin (%)
- Profit Per Unit
- Cost Percentage (%)
- High Value Order Flag
- Sales Category
- Profit Category

---

## Data Quality Decision

During feature engineering, delivery-related variables were evaluated but intentionally excluded.

The dataset contains inconsistent **Ship Date** values that generate unrealistic delivery durations (hundreds of days after the order date).

Rather than introducing misleading variables into the machine learning pipeline, delivery-based features were omitted.

This reflects good data science practice by prioritizing data quality over feature quantity.

---

# Tech Stack

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Machine Learning

- Scikit-learn

## Visualization

- Matplotlib
- Seaborn
- Plotly

## Dashboard

- Streamlit

## Geographic Analysis

- Folium

---

# Project Roadmap

- ✅ Business Understanding
- ✅ Data Preparation
- ✅ Exploratory Data Analysis
- ✅ Feature Engineering
- ⏳ Predictive Modeling
- ⏳ Factory Optimization
- ⏳ Recommendation Engine
- ⏳ Scenario Simulation
- ⏳ Streamlit Dashboard
- ⏳ Research Paper
- ⏳ Executive Summary

---

# Future Work

The remaining stages include:

- Build predictive machine learning models
- Optimize factory allocation
- Develop recommendation engine
- Simulate alternative factory assignments
- Build interactive Streamlit dashboard
- Add geographic shipment visualization
- Evaluate model performance
- Prepare research paper
- Deploy the project

---

# Expected Outcomes

The completed system will enable decision-makers to:

- Predict shipment performance
- Evaluate factory reassignment scenarios
- Reduce logistics costs
- Improve operational efficiency
- Maintain profitability
- Support data-driven factory allocation decisions

---

# Author

## Anushka Das

**AI • Machine Learning • Data Science**

GitHub:

https://github.com/AN-ai-del