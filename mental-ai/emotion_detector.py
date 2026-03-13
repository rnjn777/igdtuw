import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_emotion_model():
    """
    Loads and caches the Hugging Face emotion detection model.
    Using distilroberta-base for better accuracy and performance.
    """
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=False
    )

def detect_emotion(text):
    """
    Analyzes text and returns the detected emotion and its confidence score.
    """
    classifier = load_emotion_model()
    result = classifier(text)[0]
    return result["label"], result["score"]
