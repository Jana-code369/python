from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Workout Data (with level + sets + reps + weight)
workouts = {
    "chest": {
        "beginner": [
            {"name": "Bench Press", "sets": 3, "reps": 10, "weight": "40kg"},
            {"name": "Incline DB Press", "sets": 3, "reps": 12, "weight": "15kg"}
        ],
        "intermediate": [
            {"name": "Bench Press", "sets": 4, "reps": 8, "weight": "60kg"},
            {"name": "Incline DB Press", "sets": 4, "reps": 10, "weight": "20kg"}
        ]
    },
    "back": {
        "beginner": [
            {"name": "Lat Pulldown", "sets": 3, "reps": 10, "weight": "30kg"},
            {"name": "Seated Row", "sets": 3, "reps": 12, "weight": "25kg"}
        ],
        "intermediate": [
            {"name": "Deadlift", "sets": 4, "reps": 6, "weight": "80kg"},
            {"name": "Pull-ups", "sets": 4, "reps": 8, "weight": "Bodyweight"}
        ]
    }
}

# Diet Plans
diet = {
    "muscle": ["Chicken", "Eggs", "Rice", "Milk", "Peanut Butter"],
    "fatloss": ["Oats", "Boiled Eggs", "Salad", "Fruits", "Green Tea"]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    part = request.form['part']
    goal = request.form['goal']
    level = request.form['level']

    workout_list = workouts.get(part, {}).get(level, [])

    return render_template('index.html',
                           workouts=workout_list,
                           diet=diet.get(goal, []))

# 🤖 AI Assistant
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get("message", "").lower()

    if "chest" in msg:
        reply = "Chest: Bench Press (4x8), Incline DB (4x10), Fly (3x12)"

    elif "back" in msg:
        reply = "Back: Deadlift (4x6), Pull-ups (4x8), Row (3x10)"

    elif "biceps" in msg:
        reply = "Biceps: Barbell Curl (3x10), Hammer Curl (3x12)"

    elif "triceps" in msg:
        reply = "Triceps: Pushdown (3x12), Skull Crushers (3x10)"

    elif "shoulder" in msg:
        reply = "Shoulders: Press (4x8), Lateral Raise (4x12)"

    elif "legs" in msg:
        reply = "Legs: Squats (4x8), Lunges (3x12)"

    elif "muscle" in msg:
        reply = "Muscle Gain: Heavy weights, high protein diet"

    elif "fat" in msg:
        reply = "Fat Loss: Cardio + calorie deficit"

    elif "beginner" in msg:
        reply = "Beginner: 3 sets, focus on form"

    elif "intermediate" in msg:
        reply = "Intermediate: 4 sets, progressive overload"

    elif "diet" in msg:
        reply = "Eat protein-rich foods for muscle, low calories for fat loss"

    else:
        reply = "Ask me about workouts, diet, or fitness!"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)