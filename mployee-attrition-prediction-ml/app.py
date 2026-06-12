import streamlit as st
import pandas as pd
import pickle

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# Load Model
# -------------------------

with open("employee_attrition_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("feature_names.pkl", "rb") as file:
    feature_names = pickle.load(file)

# -------------------------
# Title
# -------------------------

st.title("📊 Employee Attrition Prediction System")

st.markdown(
    """
Predict whether an employee is likely to leave the company.
"""
)

st.divider()

# -------------------------
# Sidebar
# -------------------------

st.sidebar.header("Employee Information")

# -------------------------
# Dynamic Input Creation
# -------------------------

input_data = {}

for feature in feature_names:

    input_data[feature] = st.sidebar.number_input(
        label=feature,
        value=0.0,
        step=1.0
    )

# -------------------------
# Convert to DataFrame
# -------------------------

input_df = pd.DataFrame(
    [input_data]
)

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Attrition"):

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)

    leave_probability = probability[0][1]

    stay_probability = probability[0][0]

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.error(
            "⚠️ Employee is likely to leave the company."
        )

    else:

        st.success(
            "✅ Employee is likely to stay in the company."
        )

    st.write("---")

    st.metric(
        "Probability of Leaving",
        f"{leave_probability*100:.2f}%"
    )

    st.metric(
        "Probability of Staying",
        f"{stay_probability*100:.2f}%"
    )

    st.write("---")

    st.subheader("Input Features")

    st.dataframe(input_df)