from flask import Flask, request, jsonify

app = Flask(__name__)
patients = []
next_id = 1

@app.get('/')
def home():
    return jsonify({"project": "Hospital System", "version": "v3", "features": ["Add Patient", "View Patients", "Delete Patient"]})

@app.get('/health')
def health():
    return jsonify({"status": "ok", "version": "v3"})

@app.post('/patients')
def add_patient():
    global next_id
    data = request.get_json(silent=True) or {}
    name = str(data.get('name', '')).strip()
    age = data.get('age')
    disease = str(data.get('disease', '')).strip()
    if not name or age is None or not disease:
        return jsonify({"error": "name, age, and disease are required"}), 400
    try:
        age = int(age)
    except (TypeError, ValueError):
        return jsonify({"error": "age must be an integer"}), 400
    if age < 0 or age > 130:
        return jsonify({"error": "age must be between 0 and 130"}), 400
    patient = {"id": next_id, "name": name, "age": age, "disease": disease}
    patients.append(patient)
    next_id += 1
    return jsonify({"message": "Patient registered successfully", "patient": patient}), 201

@app.get('/patients')
def view_patients():
    return jsonify({"count": len(patients), "patients": patients}), 200

@app.delete('/patients/<int:patient_id>')
def delete_patient(patient_id):
    for index, patient in enumerate(patients):
        if patient['id'] == patient_id:
            deleted = patients.pop(index)
            return jsonify({"message": "Patient deleted successfully", "patient": deleted}), 200
    return jsonify({"error": "Patient not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
