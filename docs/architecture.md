# 🏗️ System Architecture

---

# Document Purpose

This document describes the architecture of the **Nassau Candy Factory Optimization** system.

Unlike the README, which introduces the project and explains its features, this document focuses on the internal system design, component interactions, architectural decisions, and software engineering principles that enable the application.

The objective is to provide developers and contributors with a clear understanding of how data flows through the system, how the various modules interact, and why the project has been organized in its current form.

---

# System Overview

The Nassau Candy Factory Optimization project is an AI-powered business decision support system that combines data engineering, machine learning, business analytics, optimization techniques, and interactive visualization into a unified application.

Rather than functioning as a simple prediction model, the system provides an end-to-end workflow capable of:

- Processing historical factory data
- Engineering predictive features
- Estimating order profitability
- Generating AI-assisted business recommendations
- Optimizing production strategies
- Supporting business decision-making through an interactive dashboard

The architecture follows a modular design philosophy in which each component has a clearly defined responsibility and communicates through reusable interfaces.

---

# Architecture Goals

The architecture has been designed to satisfy the following objectives.

## Functional Goals

- Predict factory order profitability
- Generate business recommendations
- Optimize production strategies
- Visualize business performance
- Support interactive business analysis

---

## Software Engineering Goals

- High modularity
- Low coupling
- High cohesion
- Reusability
- Maintainability
- Scalability
- Readability
- Testability

---

# Design Principles

The project follows several software engineering principles.

---

## Separation of Concerns

Each module performs exactly one responsibility.

Examples include:

- Data loading
- Prediction
- Optimization
- Visualization
- Dashboard rendering

No module mixes unrelated responsibilities.

---

## Modularity

The project is organized into independent packages.

```text
src/
├── data/
├── models/
├── optimization/
├── utils/
└── visualization/
```

Each package may evolve independently without affecting the others.

---

## Reusability

Core functionality is implemented as reusable Python modules instead of being embedded directly inside the dashboard.

For example:

- Prediction functions are reusable by notebooks.
- Recommendation logic can be reused by APIs.
- Plotting functions are shared across dashboards and reports.

---

## Maintainability

The architecture minimizes duplicate logic.

Changes to one component rarely require modifications elsewhere.

For example:

Updating the machine learning model only affects the prediction module while leaving the dashboard unchanged.

---

## Extensibility

New functionality can be added without restructuring the project.

Examples include:

- Additional ML models
- REST APIs
- Authentication
- Database integration
- Cloud deployment
- Deep learning models

---

# High-Level Architecture

```text
                                ┌────────────────────────────┐
                                │  Nassau Candy Dataset      │
                                └──────────────┬─────────────┘
                                               │
                                               ▼
                         ┌─────────────────────────────────────┐
                         │ Data Preparation & Cleaning         │
                         └──────────────┬──────────────────────┘
                                        │
                                        ▼
                         ┌─────────────────────────────────────┐
                         │ Feature Engineering                 │
                         └──────────────┬──────────────────────┘
                                        │
                                        ▼
                         ┌─────────────────────────────────────┐
                         │ Gradient Boosting Regressor         │
                         └──────────────┬──────────────────────┘
                                        │
                       ┌────────────────┴────────────────┐
                       ▼                                 ▼
          ┌────────────────────┐             ┌────────────────────────┐
          │ Prediction Module  │             │ Recommendation Engine  │
          └──────────┬─────────┘             └──────────┬─────────────┘
                     │                                  │
                     └───────────────┬──────────────────┘
                                     ▼
                    ┌─────────────────────────────────────┐
                    │ Strategy Optimizer                  │
                    └──────────────┬──────────────────────┘
                                   ▼
                    ┌─────────────────────────────────────┐
                    │ Streamlit Dashboard                 │
                    └──────────────┬──────────────────────┘
                                   ▼
                    ┌─────────────────────────────────────┐
                    │ Business Decision Support           │
                    └─────────────────────────────────────┘
```

---

# Layered Architecture

The system is divided into four logical layers.

```text
┌───────────────────────────────────────────────────────────┐
│                 Presentation Layer                        │
│                                                           │
│          Streamlit Dashboard (dashboard/)                │
└───────────────────────────────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────┐
│                Business Logic Layer                       │
│                                                           │
│ Recommendation Engine                                     │
│ Strategy Optimizer                                        │
│ Helper Functions                                          │
└───────────────────────────────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────┐
│              Machine Learning Layer                       │
│                                                           │
│ Gradient Boosting Model                                   │
│ Prediction Module                                         │
└───────────────────────────────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────┐
│                     Data Layer                            │
│                                                           │
│ Data Loading                                              │
│ Feature Engineered Dataset                                │
└───────────────────────────────────────────────────────────┘
```

---

# Benefits of the Layered Design

The layered architecture provides several advantages.

- Clear separation between UI and business logic.
- Reusable machine learning modules.
- Independent visualization components.
- Easier debugging.
- Improved scalability.
- Simplified testing.
- Easier deployment of individual components.
- Better long-term maintainability.

---

# 🧩 Component Architecture

The project is organized into independent modules, each responsible for a specific part of the Machine Learning pipeline.

This separation improves maintainability, reusability, and scalability while keeping business logic independent from the presentation layer.

---

# Project Directory Architecture

```text
                    ┌──────────────────────────────┐
                    │        config/               │
                    │ Configuration & Constants    │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
        ┌──────────────────────────────────────────────────┐
        │                  dashboard/                      │
        │          Streamlit User Interface                │
        └──────────────┬───────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────────┐
        │                    src/                          │
        │ Prediction • Optimization • Utilities • Plots   │
        └──────────────┬───────────────────────────────────┘
                       │
          ┌────────────┼─────────────┐
          ▼            ▼             ▼
      models/       data/      visualization/
          │
          ▼
 recommendation_engine.py
 strategy_optimizer.py
 helpers.py

                       │
                       ▼
        ┌──────────────────────────────────────────────────┐
        │                 models/                          │
        │      Trained Gradient Boosting Model             │
        └──────────────────────────────────────────────────┘
```

---

# Configuration Layer

Location

```text
config/
```

## Purpose

The configuration layer centralizes all configurable project parameters.

Instead of hardcoding values throughout the codebase, common settings are stored in one location.

Examples include:

- Dataset paths
- Model paths
- Constants
- Dashboard configuration
- Default parameters

Primary files

```text
config.py
constants.py
```

### Benefits

- Easier maintenance
- Single source of truth
- Cleaner application code
- Environment-independent configuration

---

# Data Layer

Location

```text
src/data/
```

## Purpose

The Data Layer acts as the gateway between stored datasets and the rest of the application.

It abstracts all file loading operations so that downstream modules never directly access CSV files.

Primary module

```text
load_data.py
```

Responsibilities

- Load processed datasets
- Validate file availability
- Return ready-to-use DataFrames
- Separate storage from business logic

---

## Data Flow

```text
CSV File
     │
     ▼
load_data.py
     │
     ▼
Pandas DataFrame
     │
     ▼
Prediction Pipeline
```

---

# Machine Learning Layer

Location

```text
src/models/
```

## Purpose

The Machine Learning layer is responsible for all inference-related operations.

This module hides implementation details such as:

- Model loading
- Feature encoding
- Column alignment
- Prediction generation

Primary module

```text
predict.py
```

Responsibilities

- Load trained model
- Encode categorical features
- Match training feature order
- Predict batch records
- Predict individual orders

Inputs

```text
Sales
Cost
Units
Region
Ship Mode
Sales Category
High Value Order
```

Output

```text
Predicted Profit
```

---

## Prediction Workflow

```text
User Input
      │
      ▼
Feature Encoding
      │
      ▼
Column Alignment
      │
      ▼
Gradient Boosting Model
      │
      ▼
Predicted Profit
```

---

# Optimization Layer

Location

```text
src/optimization/
```

The optimization layer transforms machine learning predictions into business decisions.

Instead of stopping at prediction, the project continues into recommendation and optimization.

The optimization layer consists of two modules.

---

## Recommendation Engine

Module

```text
recommendation_engine.py
```

Purpose

Interpret predicted profit using business rules.

Responsibilities

- Estimate business risk
- Classify profitability
- Generate recommendations
- Produce decision-ready output

Example

```text
Predicted Profit

↓

Highly Recommended

↓

Low Risk

↓

Prioritize Production
```

---

## Strategy Optimizer

Module

```text
strategy_optimizer.py
```

Purpose

Evaluate multiple business scenarios automatically.

Instead of predicting one order, the optimizer searches multiple combinations.

Search Dimensions

- Region
- Shipping Mode
- Sales Category

Outputs

- Best Region
- Best Shipping Mode
- Best Sales Category
- Maximum Predicted Profit
- Recommended Strategy

---

## Optimization Workflow

```text
Predicted Profit
       │
       ▼
Recommendation Engine
       │
       ▼
Strategy Optimizer
       │
       ▼
Business Strategy
```

---

# Visualization Layer

Location

```text
src/visualization/
```

Purpose

The visualization layer contains reusable Plotly chart generators.

Separating visualization from the dashboard keeps UI code concise and allows charts to be reused across notebooks, reports, and future web applications.

Primary module

```text
plots.py
```

Available Charts

- Profit Distribution
- Regional Performance
- Shipping Performance
- Sales Category Analysis
- Profit Gauge
- Sales Growth Simulation
- Order Distribution

---

## Visualization Workflow

```text
Filtered Dataset
        │
        ▼
Plot Functions
        │
        ▼
Plotly Figure
        │
        ▼
Dashboard
```

---

# Utility Layer

Location

```text
src/utils/
```

Purpose

Provides reusable helper functions used throughout the application.

Primary module

```text
helpers.py
```

Responsibilities

- Currency formatting
- Profit classification
- Business labels
- Shared helper logic

This prevents duplicate code across notebooks, optimization modules, and the dashboard.

---

# Dashboard Layer

Location

```text
dashboard/
```

Purpose

The dashboard is the presentation layer of the system.

It coordinates all backend modules but does not contain prediction or optimization logic itself.

Responsibilities

- Collect user input
- Display KPIs
- Render visualizations
- Show recommendations
- Present optimization results
- Export filtered data

The dashboard delegates computation to backend modules, keeping the interface lightweight and maintainable.

---

## Dashboard Dependency Graph

```text
dashboard/app.py
        │
        ├────────────► config/
        │
        ├────────────► load_data.py
        │
        ├────────────► predict.py
        │
        ├────────────► recommendation_engine.py
        │
        ├────────────► strategy_optimizer.py
        │
        ├────────────► helpers.py
        │
        └────────────► plots.py
```

---

# Model Storage

Location

```text
models/
```

Contents

```text
gradient_boosting_model.pkl
```

The trained model is serialized using Joblib.

Advantages of storing the model separately include:

- Faster startup
- No retraining required
- Easy model replacement
- Version control of trained models

---

# Documentation Layer

Location

```text
docs/
```

Purpose

The documentation layer contains technical and business documentation that complements the source code.

Documents include:

- Architecture
- Methodology
- Business Understanding
- Future Improvements
- Development Roadmap

This ensures project knowledge is preserved independently of the implementation.

---

# 🔄 System Data Flow

The Nassau Candy Factory Optimization system processes data through a sequence of interconnected components.

Each layer transforms the data before passing it to the next stage.

---

## End-to-End Workflow

```text
                  Raw Dataset
                       │
                       ▼
          Data Preparation & Cleaning
                       │
                       ▼
            Feature Engineering
                       │
                       ▼
          Processed Feature Dataset
                       │
                       ▼
          Trained ML Model (.pkl)
                       │
                       ▼
            Prediction Module
                       │
                       ▼
         Recommendation Engine
                       │
                       ▼
          Strategy Optimizer
                       │
                       ▼
          Visualization Layer
                       │
                       ▼
          Streamlit Dashboard
                       │
                       ▼
        Business Decision Support
```

---

# Runtime Execution Flow

The following diagram illustrates the execution sequence when a user interacts with the dashboard.

```text
User
 │
 ▼
Streamlit Dashboard
 │
 ▼
Collect User Inputs
 │
 ▼
Prediction Module
 │
 ▼
Gradient Boosting Model
 │
 ▼
Predicted Profit
 │
 ▼
Recommendation Engine
 │
 ▼
Business Recommendation
 │
 ▼
Strategy Optimizer
 │
 ▼
Optimal Strategy
 │
 ▼
Visualization Layer
 │
 ▼
Dashboard Rendering
 │
 ▼
User
```

---

# Prediction Request Lifecycle

Whenever a user changes an input parameter, the following sequence occurs.

```text
User changes input
        │
        ▼
Dashboard receives values
        │
        ▼
predict.py
        │
        ▼
Feature Encoding
        │
        ▼
Feature Alignment
        │
        ▼
Gradient Boosting Model
        │
        ▼
Predicted Profit
        │
        ▼
recommendation_engine.py
        │
        ▼
Business Recommendation
        │
        ▼
Dashboard Update
```

---

# Automatic Strategy Optimization Workflow

The Strategy Optimizer evaluates multiple possible business scenarios instead of a single prediction.

```text
Input Parameters
        │
        ▼
Generate Candidate Strategies
        │
        ▼
Predict Profit
        │
        ▼
Generate Recommendation
        │
        ▼
Compare Results
        │
        ▼
Select Highest Profit
        │
        ▼
Return Best Strategy
```

---

## Optimization Logic

The optimizer searches combinations of:

```text
Region
×

Shipping Mode
×

Sales Category
```

Each candidate is evaluated independently using the trained prediction model.

The candidate with the highest predicted profit is returned to the dashboard.

---

# Dashboard Rendering Workflow

The dashboard is organized into independent tabs.

```text
Dashboard
     │
     ├────────► Overview
     │              │
     │              ▼
     │      Business KPIs
     │
     ├────────► Live Prediction
     │              │
     │              ▼
     │      Recommendation Engine
     │
     ├────────► Analytics
     │              │
     │              ▼
     │      Interactive Charts
     │
     └────────► Recommendations
                    │
                    ▼
            Strategy Optimizer
```

Each tab requests information from the backend modules instead of implementing business logic internally.

---

# Module Interaction Diagram

```text
                  dashboard/app.py
                         │
 ┌───────────────────────┼────────────────────────┐
 │                       │                        │
 ▼                       ▼                        ▼
load_data.py       predict.py              plots.py
                          │
                          ▼
            recommendation_engine.py
                          │
                          ▼
             strategy_optimizer.py
                          │
                          ▼
                    helpers.py
```

The dashboard orchestrates these modules but does not duplicate their functionality.

---

# Machine Learning Inference Pipeline

```text
Input Features
      │
      ▼
Categorical Encoding
      │
      ▼
Feature Alignment
      │
      ▼
Gradient Boosting Model
      │
      ▼
Predicted Profit
      │
      ▼
Business Interpretation
      │
      ▼
Recommendation
```

This design allows prediction logic to remain completely independent of the dashboard.

---

# Visualization Pipeline

The visualization layer receives processed data rather than raw datasets.

```text
Processed Dataset
        │
        ▼
Visualization Functions
        │
        ▼
Plotly Figure
        │
        ▼
Dashboard Component
```

Advantages include:

- Code reuse
- Consistent styling
- Easier maintenance
- Reusable charts for notebooks and reports

---

# Configuration Flow

Application settings are centralized in the configuration layer.

```text
config/
      │
      ├────► Dataset Paths
      │
      ├────► Model Paths
      │
      ├────► Constants
      │
      └────► Dashboard Configuration
```

This removes hard-coded values from the application.

---

# Error Handling Strategy

The architecture incorporates defensive programming practices to improve robustness.

Examples include:

- Dataset availability checks
- Empty DataFrame validation
- Feature alignment before prediction
- Model loading validation
- Safe formatting of outputs
- Filter validation in the dashboard

These checks help prevent runtime failures caused by invalid inputs or missing resources.

---

# Architectural Decisions

Several key design decisions were made during development.

## Modular Architecture

Business logic is separated from the user interface to improve maintainability.

---

## Reusable Prediction Engine

The prediction module is designed to be reusable across notebooks, dashboards, APIs, and future applications.

---

## Separate Visualization Layer

Charts are generated through dedicated plotting functions instead of embedding Plotly code inside the dashboard.

---

## Independent Recommendation Engine

Business recommendations are implemented separately from machine learning inference.

This allows recommendation rules to evolve independently of the predictive model.

---

## Strategy Optimizer

Optimization is treated as a separate layer rather than being embedded within the recommendation engine.

This separation enables future optimization algorithms (such as genetic algorithms or reinforcement learning) to be integrated without changing the prediction pipeline.

---

# Benefits of the Architecture

The current architecture provides:

- High cohesion within modules
- Low coupling between components
- Improved readability
- Reusable business logic
- Easier debugging
- Simplified testing
- Better scalability
- Cleaner project organization
- Production-inspired software design

---

# 📈 Scalability Strategy

The current architecture has been designed with future expansion in mind.

Rather than tightly coupling business logic to the dashboard, each functional area has been isolated into independent modules. This enables the project to evolve without requiring large-scale restructuring.

Potential scaling opportunities include:

- Multiple machine learning models
- Additional optimization algorithms
- REST API integration
- Cloud deployment
- Database connectivity
- Authentication and authorization
- Real-time prediction services
- Enterprise reporting systems

The modular design minimizes the impact of these future enhancements on the existing codebase.

---

# 🔧 Maintainability

Maintainability was a primary architectural objective throughout development.

Several engineering practices were adopted to reduce complexity and improve long-term maintainability.

## Single Responsibility Principle

Each module performs one well-defined task.

Examples include:

| Module | Responsibility |
|----------|----------------|
| `load_data.py` | Dataset loading |
| `predict.py` | Machine learning inference |
| `recommendation_engine.py` | Business recommendation generation |
| `strategy_optimizer.py` | Strategy optimization |
| `plots.py` | Visualization generation |
| `helpers.py` | Shared utility functions |

This separation minimizes dependencies between components.

---

## Code Reuse

Common functionality is implemented once and reused throughout the project.

Examples include:

- Prediction functions
- Currency formatting
- Business classification
- Plot generation
- Optimization routines

This reduces duplication while improving consistency.

---

## Loose Coupling

Modules communicate through function interfaces rather than direct implementation dependencies.

For example:

```text
Dashboard
      │
      ▼
Prediction Module
```

The dashboard does not need to know how predictions are generated.

Likewise,

```text
Recommendation Engine
```

does not require knowledge of Streamlit components.

This loose coupling simplifies maintenance and future upgrades.

---

# 🧪 Testing Strategy

Although this project is primarily portfolio-oriented, the architecture supports automated testing.

The `tests/` directory is reserved for validating:

- Data loading
- Feature engineering
- Prediction functions
- Recommendation generation
- Strategy optimization
- Visualization utilities

Example future tests include:

- Unit tests
- Integration tests
- Regression tests
- Data validation tests

Separating core logic from the dashboard makes these components easier to test independently.

---

# 🔒 Security Considerations

The current implementation is intended for local execution and educational purposes.

Nevertheless, several architectural practices improve robustness.

Examples include:

- Separation of configuration files
- Encapsulation of prediction logic
- Controlled access to trained models
- Input validation before prediction
- Safe handling of missing data
- Centralized configuration management

For production deployment, additional measures would be recommended, including:

- Authentication
- Authorization
- HTTPS
- API rate limiting
- Secret management
- Environment-specific configuration
- Database access controls

---

# ☁️ Deployment Architecture

The project has been designed so that deployment can be introduced with minimal architectural changes.

A potential deployment architecture is shown below.

```text
                    End User
                        │
                        ▼
                 Web Browser
                        │
                        ▼
                Streamlit Dashboard
                        │
                        ▼
              Prediction API (Future)
                        │
                        ▼
           Recommendation Engine
                        │
                        ▼
            Strategy Optimizer
                        │
                        ▼
            Trained ML Model (.pkl)
```

Future deployment targets include:

- Streamlit Community Cloud
- Render
- Railway
- Microsoft Azure
- AWS
- Google Cloud Platform

---

# 🚀 Future Architecture Roadmap

The modular architecture enables numerous future enhancements without major restructuring.

## Machine Learning

- XGBoost
- LightGBM
- CatBoost
- Deep Neural Networks
- Ensemble Models

---

## Business Intelligence

- Demand Forecasting
- Inventory Optimization
- Supply Chain Analytics
- Production Scheduling
- Factory Capacity Planning

---

## Dashboard

- User Authentication
- Role-Based Access
- Report Generation
- Dark Theme
- Custom Dashboards
- Export to Excel and PDF

---

## MLOps

- MLflow
- Model Versioning
- Experiment Tracking
- Automated Retraining
- CI/CD Pipelines

---

## Cloud

- Docker
- Kubernetes
- FastAPI
- PostgreSQL
- Redis
- Object Storage
- Monitoring Dashboard

---

# 💡 Key Architectural Strengths

Compared to a traditional notebook-based machine learning project, this architecture provides several advantages.

## Modular Design

Each component can evolve independently.

---

## Reusable Components

Prediction, recommendation, optimization, and visualization modules can be reused in future applications.

---

## Production-Oriented Structure

The project follows a layered architecture similar to real-world AI applications.

---

## Business-Centric Design

The system focuses on decision support rather than only prediction.

Machine learning predictions are translated into meaningful business recommendations.

---

## Extensibility

New functionality can be integrated with minimal impact on existing modules.

Examples include:

- New dashboards
- APIs
- Additional optimization techniques
- Alternative prediction models

---

# 📄 Conclusion

The Nassau Candy Factory Optimization project demonstrates a modular, scalable, and production-inspired software architecture for applied machine learning.

Instead of treating machine learning as an isolated predictive model, the architecture integrates data engineering, model inference, business recommendation, optimization, visualization, and interactive analytics into a unified decision-support system.

By emphasizing modularity, separation of concerns, reusability, and scalability, the project provides a strong foundation for future enhancements, cloud deployment, and enterprise-level adoption.

The architectural principles adopted throughout this project reflect industry best practices for developing maintainable and extensible AI applications while remaining approachable for future contributors and continued development.

---