## 🏠 House Price Prediction using Machine Learning

#### Project Overview: 

This project develops a machine learning model to predict house prices based on area-level characteristics such as income, house age, number of rooms, number of bedrooms, and population.

#### The project includes:

1. Exploratory Data Analysis (EDA)
2. Feature selection
3. Model training and evaluation
4. Hyperparameter experimentation
5. Model comparison
6. Deployment using Gradio

## Dataset

#### Features: 
Feature	Description
Avg. Area Income	Average income of residents in the area
Avg. Area House Age	Average age of houses in the area
Avg. Area Number of Rooms	Average number of rooms
Avg. Area Number of Bedrooms	Average number of bedrooms
Area Population	Population of the area
Price	Target variable (House Price)
Address	House address (not used for modeling)

## Dataset Summary:
- Total Records: 5,000
- Missing Values: None
- Target Variable: Price

## Exploratory Data Analysis (EDA)
#### Key Findings
- Most numerical features follow approximately normal distributions.
- House prices are relatively normally distributed.
- A small number of outliers exist but do not significantly affect the dataset.
- Average Area Income has the strongest correlation with house price.
- All selected features show positive relationships with the target variable.

## Model Comparison

Sorted Model Comparison Table
================================================================================
                  Model       Train R²        Test R²                 Test MSE
0             Lasso α=1 0.917978743500 0.917997252100 10088999283.031284332275
1             Ridge α=1 0.917978680300 0.917997220400 10089003188.711675643921
2           Lasso α=0.1 0.917978743600 0.917997184200 10089007632.228765487671
3           Ridge α=0.1 0.917978742900 0.917997181400 10089007981.521389007568
4          Lasso α=0.01 0.917978743600 0.917997171500 10089009198.724899291992
5     Linear Regression 0.917978743600 0.917997170700 10089009300.893989562988
6            Ridge α=10 0.917972451900 0.917991943900 10089652363.826902389526
7   Polynomial Degree 2 0.918147037800 0.917913787400 10099268148.792512893677
8           Ridge α=100 0.917380169300 0.917403394500 10162063037.444978713989
9   Polynomial Degree 3 0.918909158300 0.917397016600 10162847726.447463989258
10              KNN k=7 0.905024606600 0.870490490900 15933872685.276611328125
11              KNN k=5 0.910855443500 0.869317068200 16078241760.745292663574
12              KNN k=3 0.928026347500 0.850692200000 18369704995.786712646484