from flask import Flask, request, jsonify
from flask_cors import CORS
from emotion_detector import detect_emotion
from llm_engine import get_supportive_response
from insight_engine import get_mental_insights

app = Flask(__name__)
# Enable CORS so the separate frontend (port 8080) can communicate with this API (port 5000)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in payload"}), 400

    user_text = data['text']
    history = data.get('history', [])

    try:
        # 1. Run local DistilRoBERTa model for emotion classification
        emotion, conf = detect_emotion(user_text)

        # 2. Run local Ollama text generation for empathetic response
        # (History can be passed here if supported by the llm engine, but currently it's stateless)
        ai_response = get_supportive_response(user_text, emotion)

        # 3. Generate structured analytics
        insights = get_mental_insights(emotion, history)

        # 4. Return as JSON
        return jsonify({
            "emotion": emotion,
            "confidence": f"{int(conf * 100)}%",
            "response": ai_response,
            "insights": {
                "burnoutRisk": insights["sleep_risk"], # Use sleep_risk as a proxy for burnout
                "stressTrend": "Elevated" if "High" in insights["stress_level"] else "Calm",
                "activity": insights["suggestion"]
            }
        })

    except Exception as e:
        print(f"Error during API processing: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "MindSentry API is running"}), 200

if __name__ == '__main__':
    print("🚀 Starting MindSentry API Server on http://localhost:5000")
    print("Models are loading (this may take a few seconds)...")
    app.run(port=5000, debug=False)
