# 🏠 Bangalore Home Price Prediction (Machine Learning + Flask + Web App)

## 📌 Project Overview
This is a **complete end-to-end Data Science project** that predicts **house prices in Bangalore** using Machine Learning.  
The project includes:

- 📊 Machine Learning model for house price prediction  
- 🔙 Flask backend to serve predictions as APIs  
- 🌐 Frontend website built using **HTML, CSS, and JavaScript**  
- 🔗 Frontend and backend integration  

Users enter house details on a web page, and the system returns an **estimated house price**.

---

## 🚀 Features
- Predict house price based on:
  - Location
  - Total square feet
  - Number of bedrooms (BHK)
  - Number of bathrooms
- REST APIs using Flask
- Interactive frontend UI
- Trained ML model saved using Pickle
- Clean and modular project structure

---

## 🧠 Machine Learning Details
- **Algorithm Used:** Linear Regression  
- **Dataset:** Bangalore House Price Dataset  
- **Preprocessing Steps:**
  - Handling missing values
  - Removing outliers
  - Feature engineering
  - One-hot encoding for locations  
- **Model Output:** Estimated price (in Lakhs)

---

## 🌐 Frontend (HTML, CSS, JavaScript)
The frontend is developed using:
- **HTML** – page structure  
- **CSS** – styling and layout  
- **JavaScript** – API calls and dynamic updates  

### Frontend Flow:
1. User enters property details
2. JavaScript sends request to Flask API
3. Flask server processes input
4. ML model predicts price
5. Result is displayed on the web page

---

## 🔙 Flask Backend
Flask is used to:
- Load trained ML model and columns
- Handle API requests
- Return predictions in JSON format

### API Endpoints

#### 🔹 Get Location Names
🗂️ Project Structure
BHP_PREDICTION_ML_PROJECT/
│
├── client/                     # Frontend
│   ├── app.html
│   ├── app.css
│   └── app.js
│
├── model/                      # Model training files
│   ├── bangalore_home_prices_model.pickle
│   ├── columns.json
│   └── model_training.ipynb
│
├── server/                     # Flask backend
│   ├── artifacts/
│   │   ├── bangalore_home_prices_model.pickle
│   │   └── columns.json
│   │
│   ├── server.py
│   └── util.py
│
└── README.md
⚙️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/bangalore-home-price-prediction.git
cd BHP_PREDICTION_ML_PROJECT
2️⃣ Install Required Libraries
pip install flask numpy pandas scikit-learn

3️⃣ Run Flask Server
python server/server.py

4️⃣ Run Frontend

Open client/app.html in your browser

Enter values and get price prediction

🛠️ Technologies Used

Python

Flask

Scikit-learn

Pandas

NumPy

HTML

CSS

JavaScript

🎯 Learning Outcomes

End-to-end machine learning project

Model deployment using Flask

Frontend–backend integration

Real-world Data Science workflow

📌 Future Improvements

Deploy application on cloud (Render / AWS / Heroku)

Improve model accuracy using advanced algorithms

Add database support

Improve UI/UX

👨‍💻 Author

Ashfaque Ahmed
🎓 Software Engineering Student
📊 Aspiring Data Scientist


