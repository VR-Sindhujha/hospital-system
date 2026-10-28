from flask import Flask, request, jsonify

app = Flask(__name__)
patients = []
next_id = 1

@app.get('/')
def home():
    return jsonify({"project": "Hospital System", "version": "v1", "features": ["Add Patient"]})

@app.get('/health')
def health():
    return jsonify({"status": "ok", "version": "v1"})

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
