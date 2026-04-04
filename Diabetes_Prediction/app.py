import streamlit as st
import pickle

# 🔹 Load Pickle Files
with open("logreg_model.pkl", "rb") as f:
    lr = pickle.load(f)  # your trained Logistic Regression model
with open("scaler (2).pkl", "rb") as f:
    sc = pickle.load(f)
# your trained StandardScaler

# 🔹 App Title
st.title("🩺 Diabetes Prediction Web App")
st.write("Enter patient details to predict diabetes risk:")

# 🔹 User Inputs
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=120)
bp = st.number_input("Blood Pressure", min_value=0, max_value=140, value=70)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
age = st.number_input("Age", min_value=1, max_value=100, value=30)

# 🔹 Predict Button
if st.button("Predict Diabetes Risk"):
    user_input = [[pregnancies, glucose, bp, bmi, dpf, age]]
    
    # Scale input
    user_input_scaled = sc.transform(user_input)
    
    # Make prediction
    prediction = lr.predict(user_input_scaled)
    probability = lr.predict_proba(user_input_scaled)[0][1]  # probability of diabetes
    
    # Display Result
    if prediction[0] == 1:
        st.error(f"⚠️ High risk of Diabetes! Probability: {probability*100:.2f}%")
    else:
        st.success(f"✅ Low risk of Diabetes. Probability: {probability*100:.2f}%")
