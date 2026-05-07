# ============================================
# AFFORDABLE MEDICINE RECOMMENDER
# Database - Users + Predictions
# ============================================

import sqlite3
import hashlib
import os
from datetime import datetime

DB_PATH = "database/app.db"

def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        name      TEXT NOT NULL,
        email     TEXT UNIQUE NOT NULL,
        password  TEXT NOT NULL,
        age       INTEGER,
        gender    TEXT,
        location  TEXT,
        joined    TEXT NOT NULL
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id    INTEGER NOT NULL,
        username   TEXT NOT NULL,
        symptoms   TEXT NOT NULL,
        disease    TEXT NOT NULL,
        severity   TEXT NOT NULL,
        medicines  TEXT NOT NULL,
        advice     TEXT NOT NULL,
        timestamp  TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )''')

    conn.commit()
    conn.close()
    print("Database initialized!")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup_user(name, email, password, age, gender, location):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO users
            (name, email, password, age, gender, location, joined)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (name, email, hash_password(password),
             age, gender, location,
             datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        return True, "Account created successfully!"
    except sqlite3.IntegrityError:
        return False, "Email already registered. Please login."
    finally:
        conn.close()

def login_user(email, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email=? AND password=?',
              (email, hash_password(password)))
    user = c.fetchone()
    conn.close()
    if user:
        return True, {
            "id": user[0], "name": user[1], "email": user[2],
            "age": user[4], "gender": user[5],
            "location": user[6], "joined": user[7]
        }
    return False, "Invalid email or password."

def save_prediction(user_id, username, symptoms,
                    disease, severity, medicines, advice):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO predictions
        (user_id, username, symptoms, disease,
         severity, medicines, advice, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (user_id, username, symptoms, disease,
         severity, ', '.join(medicines), advice,
         datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_user_predictions(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT * FROM predictions
                 WHERE user_id=?
                 ORDER BY id DESC''', (user_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_all_predictions():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM predictions ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

def get_stats():
    rows = get_all_predictions()
    total = len(rows)
    disease_counts = {}
    severity_counts = {"Low": 0, "Medium": 0, "High": 0}
    for row in rows:
        d = row[4]
        s = row[5]
        disease_counts[d] = disease_counts.get(d, 0) + 1
        if s in severity_counts:
            severity_counts[s] += 1
    top = sorted(disease_counts.items(),
                 key=lambda x: x[1], reverse=True)[:5]
    return total, severity_counts, top

if __name__ == "__main__":
    init_db()
    print("Done!")