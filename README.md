# 💊 Affordable Medicine Recommender

An AI-powered full stack web application that helps underprivileged
and rural patients in India identify possible diseases based on their
symptoms and recommends affordable generic medicines.

## 🎯 Problem Statement
Poor and rural patients in India often cannot afford doctors.
This system allows them to enter their symptoms and get:
- Predicted disease using Machine Learning
- Affordable generic medicine recommendations
- Severity level (Low / Medium / High)
- Medical advice and where to get free medicines

## 🛠️ Tech Stack
- **Frontend**: Streamlit (Python)
- **Backend**: FastAPI (Python)
- **Database**: SQLite
- **ML Model**: Random Forest Classifier (Scikit-learn)
- **NLP**: TF-IDF Vectorizer
- **Charts**: Plotly
- **Dataset**: Kaggle Disease Symptom Dataset (4920 records, 41 diseases)

## 📁 Project Structure
medicine-recommender/
├── dataset/
│   └── symptom_disease.csv
├── model/
│   ├── model.pkl
│   └── tfidf.pkl
├── database/
│   └── app.db
├── app.py
├── backend.py
├── database.py
├── medicine_map.py
├── train_model.py
├── requirements.txt
└── README.md
## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model
```bash
python train_model.py
```

### 3. Start the backend
```bash
uvicorn backend:app --reload
```

### 4. Start the frontend
```bash
streamlit run app.py
```

### 5. Open browser
http://localhost:8501
## 📊 Model Performance
- Algorithm: Random Forest (100 trees)
- Dataset: 4920 records, 41 diseases
- Accuracy: 100% on test data
- Features: TF-IDF vectorized symptom text

## 👤 Features
- User Signup and Login with password hashing
- AI-powered symptom analysis
- Top 3 disease predictions with confidence scores
- Affordable generic medicine mapping
- Severity classification (Low/Medium/High)
- Prediction history per user
- Statistics dashboard with charts

## ⚠️ Disclaimer
This application is for educational purposes only.
It is NOT a substitute for professional medical advice.
Always consult a qualified doctor.
Emergency: 108 | Jan Aushadhi: 1800-180-8080