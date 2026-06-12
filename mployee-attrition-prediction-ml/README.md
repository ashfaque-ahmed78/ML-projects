# 👨‍💼 Employee Attrition Prediction Using Machine Learning

## 📌 Overview

Employee attrition is one of the most critical challenges faced by organizations. High turnover rates can lead to increased recruitment costs, reduced productivity, and loss of valuable organizational knowledge.

This project leverages **Machine Learning** to predict whether an employee is likely to leave the company based on demographic, professional, and workplace-related factors. The solution helps HR teams make data-driven decisions and proactively address employee retention issues.

---

## 🎯 Business Problem

Employee turnover has a direct impact on organizational performance and operational costs.

The objective of this project is to build a predictive model capable of answering the following question:

> **Will an employee leave the company?**

### Prediction Classes

| Value | Meaning |
|---------|---------|
| 0 | Employee Stays |
| 1 | Employee Leaves |

---

## 📊 Dataset

The project uses the **IBM HR Analytics Employee Attrition Dataset**, which contains employee-related information such as:

- 👤 Age
- 🚻 Gender
- ✈️ Business Travel
- 🏢 Department
- 🎓 Education
- 💼 Job Role
- 💰 Monthly Income
- 🏠 Distance From Home
- ⏰ Overtime
- 😊 Job Satisfaction
- ⚖️ Work-Life Balance
- 📅 Years At Company
- 📈 Total Working Years
- ⭐ Performance Rating

### 🎯 Target Variable

| Feature | Description |
|----------|------------|
| Attrition | Indicates whether an employee left the company |

---

## 🔄 Project Workflow

### 1️⃣ Data Understanding

- Explored dataset structure
- Identified numerical and categorical features
- Understood business relevance of each variable

### 2️⃣ Data Cleaning

Removed unnecessary features:

- EmployeeCount
- EmployeeNumber
- Over18
- StandardHours

Performed:

- Missing value analysis
- Duplicate record checks
- Data consistency validation

### 3️⃣ Feature Encoding

Categorical features were converted into numerical format using:

- Label Encoding
- One-Hot Encoding

Target variable transformation:

| Original | Encoded |
|-----------|----------|
| Yes | 1 |
| No | 0 |

### 4️⃣ Exploratory Data Analysis (EDA)

Conducted detailed analysis to uncover patterns and factors influencing employee attrition.

Key analyses included:

- 📉 Attrition Distribution
- 👤 Age Analysis
- ⏰ Overtime Analysis
- 💰 Income Analysis
- 😊 Job Satisfaction Analysis
- ⚖️ Work-Life Balance Analysis
- 🏢 Department-wise Analysis
- ✈️ Business Travel Analysis
- 🔥 Correlation Analysis

Additionally, automated EDA was performed using **YData Profiling**.

### 5️⃣ Model Development

Dataset Split:

- 📚 Training Data: 80%
- 🧪 Testing Data: 20%

Machine Learning algorithms used:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

## 🤖 Model Performance

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 87.76% |
| Decision Tree | 74.83% |
| Random Forest | 88.10% |

### 🏆 Best Performing Model

**Random Forest Classifier**

The Random Forest model achieved the highest overall accuracy and was selected as the final model.

---

## 📈 Classification Report (Random Forest)

| Metric | Score |
|----------|----------|
| Accuracy | 88% |
| Precision (Attrition Class) | 100% |
| Recall (Attrition Class) | 10% |
| F1-Score (Attrition Class) | 19% |

### ⚠️ Observation

The dataset is imbalanced, resulting in high overall accuracy but lower recall for employees who actually leave the organization.

Potential future improvements:

- SMOTE Oversampling
- Class Weight Balancing
- Hyperparameter Tuning
- XGBoost Implementation

---

## 🔍 Key Business Insights

Analysis revealed several important factors influencing employee attrition:

- ⏰ Employees working overtime are more likely to leave.
- 💰 Lower monthly income is associated with higher attrition.
- ⚖️ Poor work-life balance contributes to employee turnover.
- 👨‍💻 Younger employees show higher attrition tendencies.
- 📅 Employees with fewer years at the company are more likely to resign.
- ✈️ Frequent business travel may increase attrition risk.
- 😊 Job satisfaction is a major indicator of employee retention.

---

## 🛠️ Technologies Used

### Programming Language

- 🐍 Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn

### Automated EDA

- YData Profiling

### Deployment

- Streamlit

### Model Serialization

- Pickle

---

## 📂 Project Structure

```text
Employee_Attrition_Project/

│
├── data/
│   └── employee_attrition.csv
│
├── notebooks/
│   └── employee_attrition_analysis.ipynb
│
├── reports/
│   └── employee_attrition_report.html
│
├── employee_attrition_model.pkl
│
├── feature_names.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## 🌐 Streamlit Application

The project includes an interactive Streamlit application that allows users to:

- 📝 Enter employee information
- 🤖 Predict employee attrition
- 📊 View prediction probabilities
- 📈 Analyze employee retention risk

### ▶️ Run the Application

```bash
streamlit run app.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/employee-attrition-prediction-ml.git
```

### Navigate to Project Folder

```bash
cd employee-attrition-prediction-ml
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Improvements

- Implement SMOTE for handling class imbalance
- Perform Hyperparameter Optimization using GridSearchCV
- Train and compare XGBoost models
- Add advanced Streamlit dashboard visualizations
- Deploy application on Streamlit Cloud
- Integrate SHAP for model explainability
- Develop an Employee Retention Recommendation System

---

## 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- Classification Algorithms
- Model Evaluation
- Feature Importance Analysis
- Model Serialization
- Streamlit Deployment

---

## 🏁 Conclusion

This project showcases a complete end-to-end Machine Learning workflow for predicting employee attrition. From data preprocessing and exploratory analysis to model training and deployment, it demonstrates how Machine Learning can be applied to solve real-world HR analytics challenges.

The final Random Forest model achieved the best performance and provides valuable insights that can help organizations improve employee retention and make informed workforce management decisions.

---

## 👨‍💻 Author

**Ishfaq Ahmed**

🎓 Software Engineering Student  
📊 Aspiring Data Scientist & Machine Learning Engineer

⭐ If you found this project useful, consider giving it a star!
