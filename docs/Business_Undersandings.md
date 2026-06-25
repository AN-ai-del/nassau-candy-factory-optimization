# Business Understanding

## 1. Company Background

Nassau Candy Distributor is a confectionery distribution company responsible for supplying a wide range of candy and snack products to customers across multiple regions. The company manufactures and distributes products through multiple production facilities (factories), each responsible for producing specific product categories.

As customer demand grows across different geographical regions, efficient factory allocation and shipping operations become increasingly important. Shipping delays, longer transportation distances, and inefficient factory assignments can increase operational costs, reduce customer satisfaction, and negatively affect overall profitability.

To remain competitive, Nassau Candy requires a more intelligent and data-driven approach for deciding which factory should manufacture and ship each product.

---

## 2. Business Problem

The current factory assignment process follows static business rules and legacy operational practices. Every product is permanently assigned to a predefined factory regardless of changing customer demand, shipping distance, transportation efficiency, or regional order patterns.

This approach creates several operational challenges:

- Longer shipping distances for certain customer regions.
- Increased shipping lead times.
- Higher logistics and transportation costs.
- Reduced operational efficiency.
- Lower overall profitability.
- Lack of flexibility when customer demand changes.

Furthermore, business managers currently have no analytical system that can simulate alternative factory assignments before implementing operational changes.

---

## 3. Existing Business Process

Currently, the order fulfillment workflow follows a fixed sequence:

1. A customer places an order.
2. The ordered product is linked to its predefined factory.
3. The factory manufactures or dispatches the product.
4. The shipment is delivered using the selected shipping mode.
5. The customer receives the order.

Since factory assignments remain fixed, managers cannot evaluate whether another factory could fulfill the same order more efficiently.

---

## 4. Current Challenges

The existing logistics system presents several business challenges:

- Static factory-product assignments
- Inefficient shipping routes
- Long delivery lead times
- Increasing logistics expenses
- Reduced gross profit margins
- No predictive decision support
- Inability to simulate alternative factory allocation strategies
- Limited visibility into operational performance across factories

These challenges limit the organization's ability to optimize shipping efficiency while maintaining profitability.

---

## 5. Business Objectives

The primary objective of this project is to develop an AI-powered Factory Reallocation and Shipping Optimization Recommendation System capable of supporting data-driven operational decisions.

The proposed system aims to:

- Predict shipping lead times for different shipping scenarios.
- Evaluate factory performance across multiple regions.
- Simulate alternative factory assignments.
- Recommend optimal factory allocations for each product.
- Improve shipping efficiency while preserving profitability.
- Provide decision-makers with actionable recommendations before implementing operational changes.

---

## 6. Project Goals

This project combines descriptive analytics, predictive analytics, and optimization techniques to transform historical operational data into an intelligent decision support system.

The specific goals are:

- Analyze historical shipping performance.
- Identify operational bottlenecks.
- Build machine learning models for lead time prediction.
- Compare different predictive algorithms.
- Develop a recommendation engine for factory reassignment.
- Quantify operational improvements under different scenarios.
- Build an interactive Streamlit dashboard for business users.

---

## 7. Expected Business Impact

Successful implementation of the recommendation system is expected to provide several business benefits:

- Reduced shipping lead times
- Improved customer satisfaction
- Lower transportation costs
- Increased operational efficiency
- Better utilization of factory resources
- Improved profitability
- Data-driven decision making
- Higher scalability for future business expansion

---

## 8. Success Metrics

The project will be evaluated using both machine learning and business performance metrics.

### Machine Learning Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Business Performance Metrics

- Lead Time Reduction (%)
- Profit Impact
- Recommendation Confidence Score
- Recommendation Coverage
- Factory Utilization
- Operational Efficiency Improvement

---

## 9. Project Scope

This project focuses on analyzing historical order and shipping data to develop an intelligent recommendation system for factory allocation.

The scope includes:

- Data preparation
- Exploratory Data Analysis
- Feature engineering
- Shipping lead time prediction
- Factory performance evaluation
- Route optimization analysis
- Factory recommendation engine
- What-if scenario simulation
- Interactive Streamlit dashboard
- Executive reporting

The project does not include real-time ERP integration or live production deployment.

---

## 10. Assumptions

The following assumptions are made during project development:

- Historical data accurately represents business operations.
- Product demand patterns remain reasonably consistent.
- Factory coordinates provided are accurate.
- Shipping modes remain unchanged during simulation.
- Historical shipping behavior is suitable for predictive modeling.
- Factory capacity constraints are outside the scope of this project.

---

## 11. Expected Deliverables

The final project will include:

- Clean and processed dataset
- Exploratory Data Analysis report
- Machine Learning models
- Factory Optimization Engine
- Recommendation System
- Scenario Simulation Engine
- Interactive Streamlit dashboard
- Research paper
- Executive summary
- GitHub repository with complete documentation

---

## 12. Future Scope

Future enhancements may include:

- Real-time shipment tracking integration
- Live ERP and warehouse integration
- Dynamic demand forecasting
- Factory capacity optimization
- Vehicle route optimization
- Reinforcement learning-based allocation strategies
- Cost-sensitive optimization algorithms
- Cloud deployment for enterprise-scale decision support