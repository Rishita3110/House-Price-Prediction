import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load files
model = joblib.load("deployment_lasso.pkl")
scaler = joblib.load("deployment_scaler.pkl")
feature_columns = joblib.load("deployment_features.pkl")

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Predict house prices using the Ames Housing Dataset and Lasso Regression")

# Inputs
grlivarea = st.number_input(
    "Ground Living Area (sq ft)",
    min_value=300,
    max_value=10000,
    value=1500
)

overallqual = st.slider(
    "Overall Quality",
    min_value=1,
    max_value=10,
    value=5
)

yearbuilt = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2025,
    value=2000
)

totalbsmtsf = st.number_input(
    "Total Basement Area",
    min_value=0,
    max_value=5000,
    value=1000
)

lotarea = st.number_input(
    "Lot Area",
    min_value=1000,
    max_value=100000,
    value=8000
)

garagecars = st.number_input(
    "Garage Capacity (Cars)",
    min_value=0,
    max_value=10,
    value=2
)

if st.button("Predict Price"):

    # Create dataframe with ALL training columns
    input_df = pd.DataFrame(
        np.zeros((1, len(feature_columns))),
        columns=feature_columns
    )

    # Fill user inputs
    if "GrLivArea" in input_df.columns:
        input_df["GrLivArea"] = grlivarea

    if "OverallQual" in input_df.columns:
        input_df["OverallQual"] = overallqual

    if "YearBuilt" in input_df.columns:
        input_df["YearBuilt"] = yearbuilt

    if "TotalBsmtSF" in input_df.columns:
        input_df["TotalBsmtSF"] = totalbsmtsf

    if "LotArea" in input_df.columns:
        input_df["LotArea"] = lotarea

    if "GarageCars" in input_df.columns:
        input_df["GarageCars"] = garagecars

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)

    # If SalePrice was log transformed
    predicted_price = np.expm1(prediction[0])

    st.success(f"🏡 Estimated House Price: ${predicted_price:,.0f}")