def get_mental_insights(emotion, history):
    """
    Analyzes emotion history and current state to provide analytics and suggestions.
    This logic turns the app into a wellness analyzer for hackathon judges.
    """
    # Defensive copy and update
    current_history = history.copy()
    current_history.append(emotion)
    
    # Stress trend logic
    # Higher counts of perceived negative emotions indicate higher stress
    stress_emotions = ["anger", "disgust", "fear", "sadness"]
    stress_count = sum(1 for e in current_history[-5:] if e in stress_emotions)
    
    if stress_count >= 3:
        stress_level = "↑ High"
    elif stress_count >= 1:
        stress_level = "↗ Moderate"
    else:
        stress_level = "→ Low"
        
    # Sleep risk and suggestions based on current emotion
    if emotion == "sadness":
        suggestion = "Consider reaching out to a trusted friend or journaling your thoughts."
        sleep_risk = "Moderate"
    elif emotion == "anger":
        suggestion = "Try a quick grounding exercise or stepping away for a 5-minute walk."
        sleep_risk = "Moderate"
    elif emotion == "fear":
        suggestion = "Use box breathing (4-4-4-4) to help calm your nervous system."
        sleep_risk = "High"
    elif emotion == "disgust":
        suggestion = "Focus on one small thing you can control in your environment."
        sleep_risk = "Low"
    elif emotion == "surprise":
        suggestion = "Take a moment to ground yourself in the present reality."
        sleep_risk = "Low"
    elif emotion == "joy":
        suggestion = "Lean into this positive energy; maybe share it with someone else!"
        sleep_risk = "Very Low"
    else:
        suggestion = "Maintain your healthy routines and ensure you get enough rest."
        sleep_risk = "Low"
        
    return {
        "emotion": emotion,
        "stress_level": stress_level,
        "suggestion": suggestion,
        "sleep_risk": sleep_risk,
        "timeline_data": current_history[-5:] # Return last 5 for visualization
    }

def get_emoji_map():
    """Returns mapping of emotion labels to emojis for visualization."""
    return {
        "anger": "😠",
        "disgust": "🤢",
        "fear": "😟",
        "joy": "😊",
        "neutral": "😐",
        "sadness": "😞",
        "surprise": "😲"
    }
