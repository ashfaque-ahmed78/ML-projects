import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved model, scaler, and features
model = joblib.load("random_forest_car_price_model.pkl")
scaler = joblib.load("scaler.pkl")
model_features = joblib.load("model_features.pkl")

st.title("Car Price Prediction App")
st.write("Predict car price based on specifications")

# User inputs
enginesize = st.number_input("Engine Size", 50, 500, 130)
horsepower = st.number_input("Horsepower", 50, 500, 111)
curbweight = st.number_input("Curb Weight", 1000, 5000, 2500)
carlength = st.number_input("Car Length", 120, 250, 180)
carwidth = st.number_input("Car Width", 60, 100, 65)
citympg = st.number_input("City MPG", 10, 50, 21)
highwaympg = st.number_input("Highway MPG", 10, 60, 27)

fueltype = st.selectbox("Fuel Type", ["gas", "diesel"])
aspiration = st.selectbox("Aspiration", ["std", "turbo"])
doornumber = st.selectbox("Door Number", ["two", "four"])
carbody = st.selectbox("Car Body Type", ["sedan", "hatchback", "wagon", "convertible", "hardtop"])
drivewheel = st.selectbox("Drive Wheel", ["fwd", "rwd", "4wd"])
enginelocation = st.selectbox("Engine Location", ["front", "rear"])
brand = st.selectbox("Brand", ["alfa-romero","audi","bmw","chevrolet","dodge","honda","isuzu","jaguar","mazda","mercedes-benz","mercury","mitsubishi","nissan","peugot","plymouth","porsche","renault","saab","subaru","toyota","volkswagen","volvo"])

# Prepare input
input_dict = {
    'enginesize': enginesize,
    'horsepower': horsepower,
    'curbweight': curbweight,
    'carlength': carlength,
    'carwidth': carwidth,
    'citympg': citympg,
    'highwaympg': highwaympg
}
input_df = pd.DataFrame([input_dict])

# One-hot encoding
encoded_df = pd.DataFrame(np.zeros((1, len(model_features))), columns=model_features)
for col in input_df.columns:
    if col in encoded_df.columns:
        encoded_df[col] = input_df[col]

def one_hot_fill(feature_name, value):
    col_name = f"{feature_name}_{value}"
    if col_name in encoded_df.columns:
        encoded_df[col_name] = 1

for feature, value in [("fueltype", fueltype), ("aspiration", aspiration),
                       ("doornumber", doornumber), ("carbody", carbody),
                       ("drivewheel", drivewheel), ("enginelocation", enginelocation),
                       ("brand", brand)]:
    one_hot_fill(feature, value)

# Scale features
encoded_df_scaled = scaler.transform(encoded_df)

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(encoded_df_scaled)
    st.success(f"Estimated Car Price: ${prediction[0]:,.2f}")
