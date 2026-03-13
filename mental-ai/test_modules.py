from emotion_detector import detect_emotion
from insight_engine import get_mental_insights
import requests

def test_flow():
    test_text = "I am feeling very stressed and anxious about my exams."
    print(f"Testing text: {test_text}")
    
    # Test Emotion Detector
    print("Testing emotion detection...")
    emotion, confidence = detect_emotion(test_text)
    print(f"Detected Emotion: {emotion} ({confidence})")
    
    # Test Insight Engine
    print("Testing insight engine...")
    history = ["neutral", "neutral"]
    insights = get_mental_insights(emotion, history)
    print(f"Insights: {insights}")
    
    # Verify 'emotion' key is present
    if 'emotion' in insights:
        print("PASS: 'emotion' key found in insights.")
    else:
        print("FAIL: 'emotion' key NOT found in insights.")
        
    # Test Ollama Connection (Assuming it's running)
    print("Testing LLM engine connection...")
    try:
        from llm_engine import get_supportive_response
        response = get_supportive_response(test_text, emotion)
        print(f"AI Response Snippet: {response[:100]}...")
    except Exception as e:
        print(f"LLM Engine Error (expected if server offline): {e}")

if __name__ == "__main__":
    test_flow()
