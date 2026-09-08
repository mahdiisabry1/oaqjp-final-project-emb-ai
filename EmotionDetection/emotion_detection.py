from flask import Flask, render_template, request
import json
import requests

app = Flask("Emotion Detection")

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, headers = Headers, json = Input_json)
    
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_result = formatted_response["emotionPredictions"][0]["emotion"]
        anger = emotion_result['anger']
        disgust = emotion_result['disgust']
        fear = emotion_result['fear']
        joy = emotion_result['joy']
        sadness = emotion_result['sadness']
        dominant_emotion = max(emotion_result, key=emotion_result.get)
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
        return{
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    
    return {"emotions": None}

