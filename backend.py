# ============================================
# AFFORDABLE MEDICINE RECOMMENDER
# Backend - FastAPI + SQLite
# ============================================

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from medicine_map import get_medicine_info
from database import (init_db, signup_user, login_user,
                      save_prediction, get_user_predictions,
                      get_all_predictions, get_stats)

app = FastAPI(title="Medicine Recommender API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

init_db()
model = joblib.load("model/model.pkl")
tfidf = joblib.load("model/tfidf.pkl")
print("✅ Model loaded!")

class SignupInput(BaseModel):
    name: str
    email: str
    password: str
    age: int
    gender: str
    location: str

class LoginInput(BaseModel):
    email: str
    password: str

class PredictInput(BaseModel):
    user_id: int
    username: str
    symptoms: str
    age: int = 25
    gender: str = "Not specified"

@app.get("/")
def home():
    return {"message": "Medicine Recommender API", "status": "running"}

@app.post("/signup")
def signup(data: SignupInput):
    success, msg = signup_user(
        data.name, data.email, data.password,
        data.age, data.gender, data.location
    )
    if success:
        return {"success": True, "message": msg}
    raise HTTPException(status_code=400, detail=msg)

@app.post("/login")
def login(data: LoginInput):
    success, result = login_user(data.email, data.password)
    if success:
        return {"success": True, "user": result}
    raise HTTPException(status_code=401, detail=result)

@app.post("/predict")
def predict(data: PredictInput):
    symptoms_clean = data.symptoms.strip().lower().replace(",", " ")
    symptoms_tfidf = tfidf.transform([symptoms_clean])

    proba        = model.predict_proba(symptoms_tfidf)[0]
    classes      = model.classes_
    top3_indices = proba.argsort()[::-1][:3]

    top_disease    = str(classes[top3_indices[0]])
    top_confidence = float(proba[top3_indices[0]])

    top3 = [
        {
            "disease":    str(classes[i]),
            "confidence": round(float(proba[i]) * 100, 1)
        }
        for i in top3_indices
    ]

    if top_confidence < 0.30:
        return {
            "disease":    "Uncertain — need more symptoms",
            "severity":   "Unknown",
            "medicines":  ["Please consult a doctor"],
            "advice":     "Your symptoms are too general. Please add more specific symptoms or visit a nearby PHC.",
            "confidence": round(top_confidence * 100, 1),
            "top3":       top3,
            "warning":    True
        }

    info = get_medicine_info(top_disease)
    save_prediction(
        data.user_id, data.username, data.symptoms,
        top_disease, info["severity"],
        info["medicines"], info["advice"]
    )

    return {
        "disease":    top_disease,
        "severity":   str(info["severity"]),
        "medicines":  list(info["medicines"]),
        "advice":     str(info["advice"]),
        "confidence": round(top_confidence * 100, 1),
        "top3":       top3,
        "warning":    False
    }

@app.get("/history/{user_id}")
def history(user_id: int):
    rows = get_user_predictions(user_id)
    return {"total": len(rows), "predictions": [
        {"id":        int(r[0]),
         "symptoms":  str(r[3]),
         "disease":   str(r[4]),
         "severity":  str(r[5]),
         "medicines": str(r[6]),
         "advice":    str(r[7]),
         "timestamp": str(r[8])}
        for r in rows
    ]}

@app.get("/stats")
def stats():
    total, severity_counts, top_diseases = get_stats()
    return {
        "total_predictions": int(total),
        "severity_counts":   {k: int(v) for k, v in severity_counts.items()},
        "top_diseases":      [[str(d), int(c)] for d, c in top_diseases]
    }