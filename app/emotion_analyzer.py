from transformers import pipeline


emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def emotion_analyzer(text):
    # Detect emotion
    emotion_result = emotion_classifier(text)

    print(emotion_result)
    dominant_emotion = max(emotion_result, key=lambda x: x['score'])['label']

    return dominant_emotion
