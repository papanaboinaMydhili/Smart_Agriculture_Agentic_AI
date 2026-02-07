import joblib
from flask import Flask, request, jsonify
from chatbot.intent_detection import detect_intent
from agent.decision_agent import agent_decision

app = Flask(__name__)

# Load model safely
try:
    model = joblib.load("models/crop_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
except:
    model = None
    scaler = None

@app.route("/")
def home():
    return "🤖 Smart Agriculture Agentic AI is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    intent = detect_intent(user_input)
    response = agent_decision(intent)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
