from flask import Flask, jsonify
import random

app = Flask(__name__)

# 🧠 "Base de datos"
items = [
    {"name": "Santiago", "job": "Frontend Developer"},
    {"name": "Lucia", "job": "Backend Engineer"},
    {"name": "Mateo", "job": "Data Scientist"},
    {"name": "Valentina", "job": "UI/UX Designer"},
    {"name": "Tomas", "job": "DevOps Engineer"},
]

# 🎯 función para generar impacto
def generate_impact(job):
    base = {
        "Frontend Developer": 80,
        "Backend Engineer": 85,
        "Data Scientist": 95,
        "UI/UX Designer": 75,
        "DevOps Engineer": 90
    }
    return base.get(job, 70) + random.randint(-5, 5)

# 📤 endpoint principal
@app.route("/items", methods=["GET"])
def get_items():
    result = []
    for item in items:
        result.append({
            "name": item["name"],
            "job": item["job"],
            "impact": generate_impact(item["job"])
        })
    return jsonify(result)

# 🔍 endpoint por nombre
@app.route("/items/<name>", methods=["GET"])
def get_item(name):
    for item in items:
        if item["name"].lower() == name.lower():
            return jsonify({
                "name": item["name"],
                "job": item["job"],
                "impact": generate_impact(item["job"])
            })
    return jsonify({"error": "No encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)