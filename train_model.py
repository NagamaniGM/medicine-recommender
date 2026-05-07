# ============================================
# AFFORDABLE MEDICINE RECOMMENDER
# Phase 3: Data Preprocessing
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. LOAD THE DATASET ──────────────────────
df = pd.read_csv('dataset/symptom_disease.csv')

print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

# ── 2. CLEAN THE DATA ────────────────────────
# Strip extra spaces from column names
df.columns = df.columns.str.strip()

# Strip spaces from all text values
df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)

# Replace NaN values with empty string
df = df.fillna('')

print("\nMissing values after cleaning:")
print(df.isnull().sum().sum(), "missing values remaining")

# ── 3. COMBINE ALL SYMPTOMS INTO ONE COLUMN ──
# Instead of 17 separate columns, combine into one text
symptom_cols = [col for col in df.columns if col.startswith('Symptom')]

def combine_symptoms(row):
    symptoms = [row[col] for col in symptom_cols if row[col] != '']
    return ' '.join(symptoms)

df['all_symptoms'] = df.apply(combine_symptoms, axis=1)

print("\nSample combined symptoms:")
print(df[['Disease', 'all_symptoms']].head())

# ── 4. EDA - TOP 10 DISEASES ─────────────────
plt.figure(figsize=(10, 5))
disease_counts = df['Disease'].value_counts().head(10)
sns.barplot(x=disease_counts.values, y=disease_counts.index, palette='Blues_r')
plt.title('Top 10 Most Common Diseases in Dataset')
plt.xlabel('Number of Records')
plt.ylabel('Disease')
plt.tight_layout()
plt.savefig('dataset/top_diseases.png')
plt.show()
print("\nChart saved to dataset/top_diseases.png")

print("\n✅ Phase 3 Complete! Data is clean and ready.")
# ============================================
# Phase 4: ML Model Building
# ============================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# ── 1. PREPARE INPUT AND OUTPUT ──────────────
X = df['all_symptoms']   # Input  → symptoms (text)
y = df['Disease']        # Output → disease name (label)

print("\nTotal records:", len(X))
print("Total unique diseases:", y.nunique())

# ── 2. CONVERT TEXT SYMPTOMS TO NUMBERS ──────
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(X)

print("\nShape after TF-IDF conversion:", X_tfidf.shape)

# ── 3. SPLIT DATA INTO TRAINING & TESTING ────
# 80% data → train the model
# 20% data → test how well it learned
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])

# ── 4. TRAIN THE RANDOM FOREST MODEL ─────────
print("\nTraining the model... please wait")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("✅ Model trained successfully!")

# ── 5. EVALUATE THE MODEL ────────────────────
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ── 6. SAVE THE MODEL & VECTORIZER ───────────
joblib.dump(model, 'model/model.pkl')
joblib.dump(tfidf, 'model/tfidf.pkl')
print("\n✅ Model and vectorizer saved to model/ folder!")