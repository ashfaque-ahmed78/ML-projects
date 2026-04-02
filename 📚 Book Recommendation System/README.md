
# 📚 Book Recommendation System

## 🔍 Overview
The Book Recommendation System is a machine learning based project that recommends books to users according to their interests and similarity patterns.  
It uses collaborative filtering and pre-computed similarity scores to generate accurate recommendations.

This project demonstrates:
- Data preprocessing & analysis
- Recommendation system logic
- Model persistence using Pickle
- Simple web interface using HTML templates

---

## 🚀 Features
- Popularity-based book recommendations
- Collaborative filtering recommendation system
- Exploratory Data Analysis (EDA) reports
- Fast predictions using pre-trained models
- Web interface using HTML templates

---

## 🗂 Project Structure

Book-Recommendation-System/
│
├── book_recommendation_system.ipynb
│
├── Books.xlsx
├── Ratings.xlsx
├── Users.xlsx
│
├── books.pkl
├── popular.pkl
├── pt.pkl
├── similarity_scores.pkl
│
├── books_profile_report.html
├── ratings_profile_report.html
├── users_profile_report.html
│
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
├── requirements.txt
└── README.md

---

## 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle
- Jupyter Notebook
- HTML

---

## 📊 Dataset Description
- Books.xlsx → Book metadata
- Ratings.xlsx → User ratings
- Users.xlsx → User information

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository
git clone https://github.com/USERNAME/book-recommendation-system.git
cd book-recommendation-system

### Step 2: Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt

---

## ▶️ How to Run

### Run Jupyter Notebook
jupyter notebook
Open:
book_recommendation_system.ipynb

### Run Web Application (Flask)
python app.py
Open browser:
http://127.0.0.1:5000/

---

## 🖥 Templates Folder
- index.html → Homepage
- recommend.html → Recommendation results page

These templates are connected with backend logic (Flask).

---

## 📈 EDA Reports
Interactive HTML reports are available for:
- Books
- Ratings
- Users

---

## 📌 Future Enhancements
- Deep learning based recommendations
- Improved UI using CSS & JavaScript
- Model deployment
- User authentication

---

## 👤 Author
 Ashfaque Ahmed
Software Engineering Student | Data Science Enthusiast

GitHub: https://github.com/Ashfaque-Ahmed786  
LinkedIn: https://www.linkedin.com/in/ashfaque-ahmed-29a05332b/

---

## ⭐ Support
If you find this project useful, please give it a ⭐ on GitHub.
