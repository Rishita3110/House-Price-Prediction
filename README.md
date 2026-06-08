# House Price Prediction using Ames Housing Dataset

## Project Overview

This project predicts house prices using the Ames Housing Dataset. Multiple regression models were evaluated, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest Regressor

Lasso Regression achieved the best overall performance and was selected for deployment.

## Dataset

Source:

* Kaggle House Prices: Advanced Regression Techniques Competition

Target Variable:

* SalePrice

## Data Preprocessing

* Missing value handling
* One-hot encoding of categorical features
* Feature scaling using StandardScaler
* Train-test split (80:20)

## Models Evaluated

| Model             | R² Score | MAE     | RMSE    |
| ----------------- | -------- | ------- | ------- |
| Linear Regression | 0.88536  | 0.08554 | 0.12732 |
| Ridge Regression  | 0.88547  | 0.08544 | 0.12726 |
| Lasso Regression  | 0.89503  | 0.08101 | 0.12183 |
| Random Forest     | 0.86808  | 0.09070 | 0.13658 |

## Feature Importance

Top contributing features:

* GrLivArea
* OverallQual
* YearBuilt
* TotalBsmtSF
* OverallCond
* LotArea

## Visualizations

### Feature Importance

![Feature Importance](images/Feature%20Importance.png)

### Actual vs Predicted

![Actual vs Predicted](images/actual_vs_predicted.png)

### Residual Plot

![Residual Plot](images/residual_plot.png)

## Deployment

A Streamlit application was developed using the trained Lasso Regression model.

### Run Locally

pip install -r requirements.txt

streamlit run app.py

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

## Author

Sri Sai Rishita
