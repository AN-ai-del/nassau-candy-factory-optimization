# 🏭 Nassau Candy Factory Optimization
### AI-Powered Factory Reallocation & Profit Optimization System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📌 Overview

**Nassau Candy Factory Optimization** is an end-to-end Artificial Intelligence and Machine Learning system designed to optimize factory operations by predicting order profitability, simulating production strategies, and generating business recommendations.

Unlike traditional machine learning projects that stop after training a predictive model, this project extends the workflow into an intelligent decision-support platform.

The application enables managers to:

- Predict profit for new factory orders
- Compare multiple production strategies
- Analyze regional and shipping performance
- Simulate future business scenarios
- Receive AI-generated business recommendations
- Optimize production allocation based on predicted profitability

The project combines data engineering, feature engineering, machine learning, business analytics, optimization algorithms, and an interactive Streamlit dashboard into a modular production-style repository.

---

# ✨ Key Features

## 🤖 Machine Learning

- Gradient Boosting Regression model
- Automated feature engineering
- Profit prediction engine
- Reusable prediction API
- Model evaluation and performance analysis

---

## 📊 Interactive Dashboard

- Live profit prediction
- Interactive filters
- KPI cards
- Business analytics
- Executive recommendations
- Downloadable prediction results
- Regional performance analysis
- Shipping mode analysis
- Product category analysis

---

## 🧠 AI Decision Support

- Intelligent recommendation engine
- Factory allocation optimization
- Strategy comparison
- Risk estimation
- Business interpretation of predictions

---

## 📈 Business Simulation

- Sales growth simulation
- Shipping strategy simulation
- Cost sensitivity analysis
- High-value order simulation
- Factory optimization scenarios

---

## 📁 Production-Ready Structure

- Modular Python architecture
- Separate visualization library
- Reusable utility functions
- Configuration management
- Documentation
- Research paper
- Executive summary
- Notebook-based development pipeline

---

# 📚 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Business Problem](#-business-problem)
- [Project Objectives](#-project-objectives)
- [Dataset Description](#-dataset-description)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Project Architecture](#-project-architecture)
- [Dashboard Features](#-dashboard-features)
- [Recommendation Engine](#-recommendation-engine)
- [Strategy Optimization](#-strategy-optimization)
- [Project Structure](#-project-structure)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [Results](#-results)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

# 🎯 Business Problem

Manufacturing companies receive thousands of customer orders with varying characteristics such as:

- Sales amount
- Production cost
- Shipping method
- Geographic region
- Product category
- Order size

Choosing which orders deserve priority and identifying the most profitable production strategy is a complex business challenge.

Traditional reporting tools only describe historical performance, requiring managers to manually interpret dashboards and make subjective decisions.

This project addresses that challenge by transforming historical sales data into an AI-powered decision-support system capable of predicting profitability, recommending optimal strategies, and simulating future business scenarios.

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Predict the expected profit of factory orders using Machine Learning.
- Identify high-profit production opportunities.
- Analyze regional business performance.
- Compare shipping strategies.
- Recommend optimal production allocation.
- Simulate alternative business strategies.
- Provide actionable recommendations instead of raw predictions.
- Build an interactive dashboard suitable for business stakeholders.
- Demonstrate a production-ready AI workflow suitable for real-world deployment.

---

# 📊 Dataset Description

The project is built using the **Nassau Candy Distribution** sales dataset, containing historical transactional records from a manufacturing and distribution environment.

The dataset captures operational, financial, and logistical information required to predict order profitability and optimize factory decision-making.

## Dataset Features

| Feature | Description |
|----------|-------------|
| Order ID | Unique identifier for each customer order |
| Order Date | Date when the order was placed |
| Ship Date | Date when the order was shipped |
| Ship Mode | Shipping method used for the order |
| Customer | Customer information |
| Product | Product purchased |
| Category | Product category |
| Region | Sales region |
| Sales | Revenue generated from the order |
| Cost | Manufacturing cost |
| Units | Quantity ordered |
| Profit | Actual profit generated |

---

## Feature Engineering

Several additional features were created to improve model performance and business interpretability.

### Time Features

- Order Year
- Order Month
- Order Quarter
- Is Weekend

### Business Features

- High Value Order
- Sales Category
- Profit Margin
- Cost Ratio

### Machine Learning Encoding

Categorical variables were converted using:

- One-Hot Encoding
- Feature Alignment
- Missing Category Handling

This ensured compatibility with the trained Gradient Boosting model.

---

# ⚙️ Machine Learning Pipeline

The project follows an end-to-end Machine Learning workflow, from raw data ingestion to business recommendation generation.

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Data Preprocessing
      │
      ▼
Train/Test Split
      │
      ▼
Gradient Boosting Model
      │
      ▼
Profit Prediction
      │
      ▼
Recommendation Engine
      │
      ▼
Strategy Optimizer
      │
      ▼
Interactive Dashboard
```

---

## Step 1 — Data Preparation

The dataset undergoes preprocessing to improve quality and consistency.

### Tasks Performed

- Duplicate removal
- Missing value handling
- Date conversion
- Data type correction
- Feature selection
- Outlier inspection

---

## Step 2 — Exploratory Data Analysis

Exploratory analysis was performed to understand business trends and uncover relationships within the dataset.

### Visualizations Generated

- Monthly Sales Trend
- Sales by Region
- Sales by Product
- Shipping Mode Distribution
- Profit by Product
- Profit Margin Analysis
- Missing Value Heatmap
- Dataset Composition

The EDA stage provided valuable insights for feature engineering and model selection.

---

## Step 3 — Feature Engineering

Additional predictive features were generated to improve model accuracy.

### Engineered Features

- High Value Order Flag
- Sales Category
- Order Year
- Order Month
- Order Quarter
- Weekend Indicator

Categorical variables were encoded using One-Hot Encoding before model training.

---

## Step 4 — Model Development

A **Gradient Boosting Regressor** was selected as the primary predictive model due to its ability to model complex, non-linear relationships while maintaining strong predictive performance.

### Training Workflow

1. Train-Test Split
2. Feature Encoding
3. Model Training
4. Hyperparameter Configuration
5. Model Evaluation
6. Model Serialization using Joblib

The trained model is stored as:

```text
models/
└── gradient_boosting_model.pkl
```

---

## Step 5 — Prediction Module

To improve modularity, the prediction logic is separated from the dashboard.

The reusable prediction module located in:

```text
src/models/predict.py
```

provides:

- Batch prediction
- Single-order prediction
- Automatic feature encoding
- Feature alignment with the trained model
- Prediction API reusable across the project

This design allows the Streamlit dashboard, recommendation engine, and future APIs to share the same prediction logic.

---

## Step 6 — Recommendation Engine

Rather than displaying only a numerical prediction, the system converts model output into actionable business recommendations.

Based on predicted profit, each order is classified into categories such as:

- Highly Recommended
- Recommended
- Moderate Opportunity
- Low Priority
- Avoid Production

The recommendation engine also estimates business risk and provides a human-readable explanation for decision-makers.

---

## Step 7 — Strategy Optimization

The optimization module evaluates multiple business scenarios to identify the most profitable combination of:

- Region
- Shipping Mode
- Sales Category

Instead of evaluating a single order, the optimizer compares multiple combinations and recommends the strategy with the highest predicted profitability.

This transforms the project from a prediction system into an AI-assisted business optimization platform.

---

# 🏗️ Project Architecture

The project follows a modular architecture that separates data processing, machine learning, optimization logic, visualization, and the user interface into independent components.

```text
                    ┌────────────────────────┐
                    │   Raw Dataset          │
                    └──────────┬─────────────┘
                               │
                               ▼
                    ┌────────────────────────┐
                    │ Data Preparation       │
                    └──────────┬─────────────┘
                               │
                               ▼
                    ┌────────────────────────┐
                    │ Feature Engineering    │
                    └──────────┬─────────────┘
                               │
                               ▼
                    ┌────────────────────────┐
                    │ Gradient Boosting Model│
                    └──────────┬─────────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
       Prediction Module          Recommendation Engine
                  │                         │
                  └────────────┬────────────┘
                               ▼
                    Strategy Optimizer
                               │
                               ▼
                  Interactive Streamlit Dashboard
```

---

# 🧩 Source Code Architecture

The project has been organized into reusable modules so that every component has a single responsibility.

| Module | Purpose |
|----------|----------|
| `src/data` | Data loading and preprocessing |
| `src/models` | Machine learning prediction |
| `src/optimization` | Recommendation engine and strategy optimizer |
| `src/utils` | Common helper functions |
| `src/visualization` | Reusable Plotly charts |
| `dashboard` | Interactive Streamlit application |
| `config` | Global configuration and constants |
| `docs` | Project documentation |
| `reports` | Figures, summaries, and research paper |

---

# 🤖 Machine Learning Model

The prediction engine is powered by a **Gradient Boosting Regressor** trained on engineered transactional features.

### Model Responsibilities

- Learn relationships between operational variables
- Predict expected order profit
- Generalize to unseen orders
- Support downstream business optimization

---

## Model Inputs

The model predicts profit using engineered business features including:

- Sales
- Cost
- Units
- High Value Order
- Order Year
- Order Month
- Order Quarter
- Weekend Indicator
- Shipping Mode
- Region
- Sales Category

---

## Model Output

The model produces:

```text
Predicted Profit ($)
```

This prediction becomes the foundation for the recommendation engine and optimization system.

---

# 📊 Interactive Dashboard

The project includes an interactive Streamlit dashboard designed for business users rather than data scientists.

Instead of displaying raw model outputs, the dashboard provides decision support through analytics, simulations, and recommendations.

---

## 📈 Live Profit Prediction

Users can estimate the expected profit of a hypothetical order by adjusting operational variables.

### Adjustable Parameters

- Sales
- Cost
- Units
- Region
- Shipping Mode
- Sales Category
- High Value Order

The dashboard instantly predicts the expected profit using the trained machine learning model.

---

## 📊 Business Analytics

Historical performance can be explored through interactive visualizations.

Available analyses include:

- Profit Distribution
- Regional Performance
- Shipping Performance
- Product Category Performance
- Order Distribution
- KPI Cards

These charts help managers understand historical trends before making strategic decisions.

---

## 🎯 Recommendation Engine

The recommendation engine converts numerical predictions into actionable business guidance.

Instead of showing:

```text
Predicted Profit = $129.17
```

The system generates insights such as:

```text
✅ Highly Recommended

🟢 Low Risk

🚚 Prioritize Production

📈 High Expected Profit
```

This makes model outputs understandable for non-technical decision-makers.

---

# 🚀 Strategy Optimizer

The strategy optimizer extends beyond single-order prediction by evaluating multiple business scenarios.

Instead of testing one configuration, it searches different combinations of:

- Regions
- Shipping Modes
- Sales Categories

and identifies the strategy with the highest expected profitability.

The optimizer automatically compares every candidate using the trained prediction model and recommendation engine.

Example output:

```text
Best Region:
Pacific

Best Shipping Mode:
Second Class

Best Category:
High

Predicted Profit:
$129.17

Recommendation:
Highly Recommended

Risk:
Low
```

---

# 📈 Business Simulation Engine

The dashboard also includes simulation tools that help estimate the impact of changing business variables.

Available simulations include:

- Sales Growth Simulation
- Shipping Mode Comparison
- Cost Sensitivity Analysis
- High-Value Order Analysis
- Factory Strategy Comparison

These simulations allow managers to evaluate "what-if" scenarios before making operational decisions.

---

# 📉 Data Visualization Library

To improve code reusability, all Plotly visualizations are implemented in a dedicated visualization module.

Located at:

```text
src/visualization/plots.py
```

The module contains reusable functions for generating:

- Profit Distribution
- Regional Performance
- Shipping Performance
- Sales Category Charts
- Profit Gauge
- Sales Growth Simulation
- Cost Sensitivity Simulation
- High Value Order Simulation

This approach keeps the Streamlit dashboard clean while making charts reusable across notebooks, reports, and future applications.

---

# ⚡ Modular Design Philosophy

Every major component of the project has been separated into independent modules.

Benefits include:

- Better readability
- Easier testing
- Improved maintainability
- Code reuse
- Simpler debugging
- Production-style architecture
- Easier deployment as APIs or web services

This modular approach reflects software engineering best practices commonly used in real-world AI applications.

---

# 📂 Project Structure

The repository follows a modular, production-inspired architecture that separates data engineering, machine learning, optimization, visualization, documentation, and dashboard development into independent components.

```text
nassau-candy-factory-optimization
│
├── config/
│   ├── config.py
│   └── constants.py
│
├── dashboard/
│   ├── assets/
│   │   ├── css/
│   │   ├── icons/
│   │   └── images/
│   ├── pages/
│   └── app.py
│
├── data/
│   ├── external/
│   ├── processed/
│   └── raw/
│
├── docs/
│   ├── architecture.md
│   ├── Business_Understandings.md
│   ├── Future_Improvements.md
│   ├── Methodology.md
│   └── Project_Roadmap.md
│
├── models/
│   └── gradient_boosting_model.pkl
│
├── notebooks/
│   ├── 01_Data_Preparation_Quality.ipynb
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
│   ├── data/
│   ├── models/
│   ├── optimization/
│   ├── utils/
│   └── visualization/
│
├── tests/
│
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 📒 Notebook Workflow

The project was developed incrementally through seven notebooks, each representing a stage of the complete machine learning lifecycle.

| Notebook | Purpose |
|-----------|---------|
| **01_Data_Preparation_Quality.ipynb** | Data loading, cleaning, preprocessing, and quality assessment |
| **02_Exploratory_Data_Analysis.ipynb** | Business insights and exploratory visualizations |
| **03_Feature_Engineering.ipynb** | Feature creation, transformation, and encoding |
| **04_Predictive_Modeling.ipynb** | Machine learning model training and evaluation |
| **05_Factory_Optimization.ipynb** | Business simulations and optimization experiments |
| **06_Recommendation_System.ipynb** | AI recommendation engine development |
| **07_Model_Evaluation_and_Insights.ipynb** | Model evaluation, sensitivity analysis, and final insights |

---

# 📁 Documentation

Project documentation has been organized into dedicated files for better readability and maintainability.

| Document | Description |
|----------|-------------|
| **Project_Roadmap.md** | Complete day-wise development roadmap |
| **architecture.md** | Overall system architecture |
| **Methodology.md** | End-to-end machine learning methodology |
| **Business_Understandings.md** | Business problem analysis and domain understanding |
| **Future_Improvements.md** | Planned enhancements and future roadmap |

---

# 📊 Reports

The `reports` directory contains supporting project artifacts including:

- Executive summaries
- Research paper
- Model evaluation figures
- Business visualizations
- Simulation charts

These reports complement the interactive dashboard and provide static documentation suitable for presentations and business reporting.

---

# ⚙️ Technology Stack

## Programming Language

- Python 3.11

---

## Machine Learning

- Scikit-Learn
- Gradient Boosting Regressor
- Joblib

---

## Data Processing

- Pandas
- NumPy

---

## Data Visualization

- Plotly
- Matplotlib

---

## Dashboard Development

- Streamlit

---

## Development Environment

- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

## Project Organization

- Modular Python Architecture
- Configuration Management
- Reusable Visualization Library
- Recommendation Engine
- Strategy Optimizer

---

# 📦 Installation

## Clone the Repository

```bash
git clone https://github.com/AN-ai-del/nassau-candy-factory-optimization.git
```

Move into the project directory.

```bash
cd nassau-candy-factory-optimization
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Launch the Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

The application will open automatically in your default browser.

---

## Execute the Prediction Module

```bash
python src/models/predict.py
```

---

## Execute the Recommendation Engine

```bash
python src/optimization/recommendation_engine.py
```

---

## Execute the Strategy Optimizer

```bash
python src/optimization/strategy_optimizer.py
```

---

# 💻 Dashboard Modules

The Streamlit application is organized into multiple functional sections.

### 🤖 Live Prediction

- Predict profit for new factory orders
- AI-generated recommendations
- Risk assessment
- Interactive profit gauge
- Sales growth simulation

---

### 📊 Overview

Displays:

- KPI cards
- Profit distribution
- Regional overview
- Order distribution

---

### 📈 Analytics

Provides detailed business analytics including:

- Regional performance
- Shipping performance
- Sales category analysis
- Historical business trends

---

### 🎯 Recommendations

Generates intelligent business recommendations using the trained machine learning model and optimization engine.

Includes:

- Executive recommendations
- Automatic strategy optimizer
- Best-performing business strategy
- Top recommended orders
- Business insights

---

# 📈 Generated Visualizations

The project automatically generates and stores multiple business visualizations including:

- Dataset composition
- Missing value heatmap
- Monthly sales trend
- Sales by region
- Sales by shipping mode
- Sales by product
- Profit by product
- Profit margin analysis
- Sales vs Profit
- Cost sensitivity simulation
- High-value order simulation
- Best strategy heatmap
- Shipping mode simulation
- Sales growth simulation

These figures are stored in the `reports/figures/` directory for reporting and documentation purposes.

---

# 📊 Project Results

The project successfully demonstrates an end-to-end Artificial Intelligence and Machine Learning workflow for factory profit optimization and business decision support.

## Technical Achievements

- ✅ Built a complete Machine Learning pipeline from raw data to deployment
- ✅ Engineered domain-specific features for improved predictive performance
- ✅ Trained and evaluated a Gradient Boosting Regression model
- ✅ Developed reusable prediction and optimization modules
- ✅ Designed a modular production-style project architecture
- ✅ Created an interactive Streamlit dashboard for real-time decision support

---

## Business Achievements

The system helps decision-makers by:

- Predicting the profitability of incoming orders
- Identifying high-value production opportunities
- Comparing shipping strategies
- Evaluating regional performance
- Optimizing production allocation
- Simulating multiple business scenarios
- Providing AI-generated recommendations instead of raw numerical predictions

---

# 📈 Key Project Highlights

✔ End-to-End Machine Learning Pipeline

✔ Production-Style Modular Architecture

✔ Interactive Business Dashboard

✔ AI Recommendation Engine

✔ Strategy Optimization System

✔ Business Simulation Engine

✔ Executive Decision Support

✔ Professional Documentation

✔ Research-Oriented Development Workflow

---

# 🚀 Future Improvements

This project has been designed with scalability in mind. Future enhancements may include:

## Machine Learning

- XGBoost and LightGBM model comparison
- Deep Learning regression models
- Automated Hyperparameter Optimization
- Ensemble Learning
- Explainable AI using SHAP and LIME

---

## Dashboard

- User authentication
- Role-based dashboards
- Dark mode
- Advanced filtering
- Export to PDF and Excel
- Interactive report generation

---

## Deployment

- Docker containerization
- REST API using FastAPI
- Cloud deployment on AWS, Azure, or GCP
- CI/CD pipeline with GitHub Actions
- Database integration
- Real-time prediction service

---

## Business Intelligence

- Inventory optimization
- Demand forecasting
- Production scheduling
- Supply chain optimization
- Multi-factory allocation
- Customer segmentation
- Sales forecasting
- Automated anomaly detection

---

# 📖 Project Documentation

The repository includes comprehensive documentation to support understanding, maintenance, and future development.

| Document | Description |
|----------|-------------|
| **README.md** | Project overview and usage guide |
| **Project_Roadmap.md** | Day-wise project development roadmap |
| **architecture.md** | System architecture and component interactions |
| **Methodology.md** | Machine Learning methodology |
| **Business_Understandings.md** | Business context and objectives |
| **Future_Improvements.md** | Planned enhancements |

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes.

```bash
git commit -m "Add your feature"
```

4. Push to your branch.

```bash
git push origin feature/your-feature-name
```

5. Open a Pull Request.

Please ensure that all new code follows the existing project structure and coding style.

---

# 👩‍💻 Author

## Anushka Das

Artificial Intelligence & Machine Learning Enthusiast

### Connect with me

**GitHub**

https://github.com/AN-ai-del

---

# 🙏 Acknowledgements

This project was developed as part of an advanced Machine Learning portfolio focused on applying Artificial Intelligence to solve real-world manufacturing and business optimization problems.

Special thanks to the open-source Python ecosystem, including:

- Scikit-Learn
- Pandas
- NumPy
- Plotly
- Streamlit
- Joblib

for providing the tools that made this project possible.

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the license.

For more information, see the **LICENSE** file.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a star on GitHub!

### Thank you for visiting this repository!

**Built with ❤️ using Python, Machine Learning, and Streamlit**

</div>