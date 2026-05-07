# ============================================
# AFFORDABLE MEDICINE RECOMMENDER
# Phase 5: Medicine Mapping Logic
# ============================================

# Each disease maps to:
# - medicines: affordable generic medicines
# - severity: Low / Medium / High
# - advice: what the patient should do

MEDICINE_MAP = {
    "Fungal infection": {
        "medicines": ["Clotrimazole cream", "Fluconazole 150mg", "Miconazole powder"],
        "severity": "Low",
        "advice": "Keep the affected area clean and dry. Apply cream twice daily. See a doctor if no improvement in 2 weeks."
    },
    "Allergy": {
        "medicines": ["Cetirizine 10mg", "Loratadine 10mg", "Chlorpheniramine 4mg"],
        "severity": "Low",
        "advice": "Avoid the allergen. Take antihistamine. See a doctor if breathing is affected."
    },
    "GERD": {
        "medicines": ["Omeprazole 20mg", "Ranitidine 150mg", "Antacid syrup"],
        "severity": "Medium",
        "advice": "Avoid spicy food and eat small meals. Take medicine before meals. Consult a doctor if pain persists."
    },
    "Chronic cholestasis": {
        "medicines": ["Ursodeoxycholic acid 300mg", "Vitamin K supplements"],
        "severity": "High",
        "advice": "This is a liver condition. Please visit a doctor immediately. Do not self-medicate."
    },
    "Drug Reaction": {
        "medicines": ["Stop the suspected drug immediately", "Cetirizine 10mg for rash"],
        "severity": "High",
        "advice": "Stop the medication causing reaction immediately and visit a doctor or emergency room."
    },
    "Peptic ulcer diseae": {
        "medicines": ["Omeprazole 20mg", "Pantoprazole 40mg", "Antacid gel"],
        "severity": "Medium",
        "advice": "Avoid NSAIDs and alcohol. Eat soft foods. See a doctor for H. pylori test."
    },
    "AIDS": {
        "medicines": ["Refer to government ART centre for free medicine"],
        "severity": "High",
        "advice": "Visit the nearest government hospital. Free ART medicines are available. Do not delay."
    },
    "Diabetes": {
        "medicines": ["Metformin 500mg", "Glipizide 5mg"],
        "severity": "High",
        "advice": "Monitor blood sugar daily. Take medicine after meals. Consult a doctor for proper dosage."
    },
    "Gastroenteritis": {
        "medicines": ["ORS (Oral Rehydration Salts)", "Zinc 20mg", "Metronidazole 400mg"],
        "severity": "Medium",
        "advice": "Drink ORS frequently to avoid dehydration. Eat bland food. See doctor if vomiting persists."
    },
    "Bronchial Asthma": {
        "medicines": ["Salbutamol inhaler", "Budesonide inhaler", "Montelukast 10mg"],
        "severity": "High",
        "advice": "Always carry inhaler. Avoid dust and smoke. Visit a doctor for long-term management."
    },
    "Hypertension": {
        "medicines": ["Amlodipine 5mg", "Enalapril 5mg", "Hydrochlorothiazide 25mg"],
        "severity": "High",
        "advice": "Reduce salt intake. Exercise regularly. Take medicine daily without skipping. Monitor BP."
    },
    "Migraine": {
        "medicines": ["Paracetamol 500mg", "Ibuprofen 400mg", "Sumatriptan 50mg"],
        "severity": "Medium",
        "advice": "Rest in a dark quiet room. Take medicine at first sign of headache. See doctor for frequent migraines."
    },
    "Cervical spondylosis": {
        "medicines": ["Ibuprofen 400mg", "Diclofenac gel", "Muscle relaxant (Thiocolchicoside)"],
        "severity": "Medium",
        "advice": "Avoid long screen time. Do neck exercises. See a physiotherapist."
    },
    "Paralysis (brain hemorrhage)": {
        "medicines": ["Emergency care only"],
        "severity": "High",
        "advice": "EMERGENCY! Call ambulance immediately. This requires urgent hospital care."
    },
    "Jaundice": {
        "medicines": ["Liv 52 syrup", "Vitamin B complex", "ORS for hydration"],
        "severity": "Medium",
        "advice": "Rest and drink plenty of fluids. Avoid fatty food. See a doctor for liver function test."
    },
    "Malaria": {
        "medicines": ["Chloroquine 250mg", "Artemether-Lumefantrine (Coartem)"],
        "severity": "High",
        "advice": "Visit a doctor immediately for blood test confirmation. Free malaria medicines available at govt hospitals."
    },
    "Chicken pox": {
        "medicines": ["Calamine lotion", "Paracetamol 500mg", "Acyclovir 400mg"],
        "severity": "Medium",
        "advice": "Stay isolated to avoid spreading. Do not scratch. See doctor if fever is very high."
    },
    "Dengue": {
        "medicines": ["Paracetamol 500mg", "ORS for hydration"],
        "severity": "High",
        "advice": "Do NOT take Aspirin or Ibuprofen. Monitor platelet count. Visit doctor immediately."
    },
    "Typhoid": {
        "medicines": ["Ciprofloxacin 500mg", "Azithromycin 500mg"],
        "severity": "High",
        "advice": "Drink boiled water only. Take full course of antibiotics. Visit a doctor for confirmation."
    },
    "Hepatitis A": {
        "medicines": ["Paracetamol 500mg (for fever)", "Vitamin supplements", "ORS"],
        "severity": "Medium",
        "advice": "Rest and eat light food. Avoid alcohol completely. Usually resolves on its own in 4-8 weeks."
    },
    "Hepatitis B": {
        "medicines": ["Tenofovir 300mg", "Entecavir 0.5mg"],
        "severity": "High",
        "advice": "Visit a government hospital — free Hepatitis B medicines available. Avoid alcohol."
    },
    "Hepatitis C": {
        "medicines": ["Sofosbuvir 400mg", "Daclatasvir 60mg"],
        "severity": "High",
        "advice": "Free Hepatitis C treatment available at government hospitals. Consult a liver specialist."
    },
    "Hepatitis D": {
        "medicines": ["Pegylated Interferon (doctor prescribed only)"],
        "severity": "High",
        "advice": "Requires specialist care. Visit a government hospital immediately."
    },
    "Hepatitis E": {
        "medicines": ["ORS for hydration", "Paracetamol 500mg", "Vitamin E supplements"],
        "severity": "Medium",
        "advice": "Drink only boiled water. Rest completely. Usually self-limiting in 4-6 weeks."
    },
    "Alcoholic hepatitis": {
        "medicines": ["Prednisolone 40mg (doctor prescribed)", "Vitamin B1 (Thiamine)"],
        "severity": "High",
        "advice": "Stop alcohol consumption immediately. This is a serious liver condition. Visit a doctor urgently."
    },
    "Tuberculosis": {
        "medicines": ["DOTS therapy (Rifampicin + Isoniazid + Pyrazinamide + Ethambutol)"],
        "severity": "High",
        "advice": "Free TB treatment available at all government hospitals under DOTS program. Complete the full course."
    },
    "Common Cold": {
        "medicines": ["Paracetamol 500mg", "Cetirizine 10mg", "Steam inhalation"],
        "severity": "Low",
        "advice": "Rest, drink warm fluids, and take steam. Usually resolves in 5-7 days without medication."
    },
    "Pneumonia": {
        "medicines": ["Amoxicillin 500mg", "Azithromycin 500mg"],
        "severity": "High",
        "advice": "Visit a doctor immediately. Pneumonia can be life-threatening if untreated."
    },
    "Dimorphic hemmorhoids(piles)": {
        "medicines": ["Sitz bath", "Lignocaine ointment", "Isabgol husk (fibre)"],
        "severity": "Medium",
        "advice": "Eat high fibre diet and drink plenty of water. See a doctor if bleeding is heavy."
    },
    "Heart attack": {
        "medicines": ["Aspirin 325mg (chew immediately)", "Emergency care"],
        "severity": "High",
        "advice": "EMERGENCY! Call ambulance immediately. Chew one Aspirin tablet if available. Do not delay."
    },
    "Varicose veins": {
        "medicines": ["Diosmin + Hesperidin tablets", "Compression stockings"],
        "severity": "Medium",
        "advice": "Elevate legs while resting. Avoid standing for long periods. See a doctor for severe cases."
    },
    "Hypothyroidism": {
        "medicines": ["Levothyroxine 50mcg"],
        "severity": "Medium",
        "advice": "Take medicine on empty stomach every morning. Regular thyroid function tests needed."
    },
    "Hyperthyroidism": {
        "medicines": ["Carbimazole 10mg", "Propranolol 40mg"],
        "severity": "Medium",
        "advice": "Avoid iodine rich foods. See an endocrinologist for proper dosage and monitoring."
    },
    "Hypoglycemia": {
        "medicines": ["Glucose powder / sugar water (immediate)", "Glucagon injection (severe)"],
        "severity": "High",
        "advice": "Immediately eat sugar or drink glucose water. If unconscious call emergency. Monitor blood sugar."
    },
    "Osteoarthristis": {
        "medicines": ["Paracetamol 500mg", "Ibuprofen 400mg", "Glucosamine supplements"],
        "severity": "Medium",
        "advice": "Do low impact exercises like walking and swimming. See a physiotherapist."
    },
    "Arthritis": {
        "medicines": ["Ibuprofen 400mg", "Methotrexate (doctor prescribed)", "Calcium + Vitamin D"],
        "severity": "Medium",
        "advice": "Do gentle exercises. Avoid cold exposure. See a rheumatologist for long term management."
    },
    "(vertigo) Paroymsal  Positional Vertigo": {
        "medicines": ["Meclizine 25mg", "Betahistine 16mg"],
        "severity": "Medium",
        "advice": "Do Epley maneuver exercises. Avoid sudden head movements. See an ENT specialist."
    },
    "Acne": {
        "medicines": ["Benzoyl peroxide 2.5% gel", "Clindamycin gel", "Salicylic acid face wash"],
        "severity": "Low",
        "advice": "Wash face twice daily. Avoid oily food. See a dermatologist for severe acne."
    },
    "Urinary tract infection": {
        "medicines": ["Nitrofurantoin 100mg", "Trimethoprim 200mg", "Drink plenty of water"],
        "severity": "Medium",
        "advice": "Drink at least 3 litres of water daily. Complete the full antibiotic course. See doctor if fever develops."
    },
    "Psoriasis": {
        "medicines": ["Betamethasone cream", "Coal tar shampoo", "Moisturizer (Vaseline)"],
        "severity": "Medium",
        "advice": "Keep skin moisturized. Avoid stress and skin injuries. See a dermatologist."
    },
    "Impetigo": {
        "medicines": ["Mupirocin ointment 2%", "Amoxicillin 500mg"],
        "severity": "Low",
        "advice": "Keep the affected area clean. Do not touch or scratch. Wash hands frequently."
    }
}

def get_medicine_info(disease):
    """Given a disease name, return medicine and advice info."""
    disease = disease.strip()
    if disease in MEDICINE_MAP:
        return MEDICINE_MAP[disease]
    else:
        return {
            "medicines": ["Please consult a doctor"],
            "severity": "Unknown",
            "advice": "We don't have medicine data for this condition. Please visit a nearby government hospital."
        }

def get_severity_color(severity):
    """Return a color based on severity for UI display."""
    colors = {
        "Low": "green",
        "Medium": "orange",
        "High": "red",
        "Unknown": "gray"
    }
    return colors.get(severity, "gray")

# ── TEST THE MAPPING ──────────────────────────
if __name__ == "__main__":
    test_diseases = ["Diabetes", "Common Cold", "Heart attack", "Tuberculosis"]
    for disease in test_diseases:
        info = get_medicine_info(disease)
        print(f"\nDisease: {disease}")
        print(f"Severity: {info['severity']}")
        print(f"Medicines: {', '.join(info['medicines'])}")
        print(f"Advice: {info['advice']}")
        print("-" * 60)

    print("\n✅ Phase 5 Complete! Medicine mapping is ready.")