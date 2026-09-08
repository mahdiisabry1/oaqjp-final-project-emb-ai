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
        emotion = formatted_response["emotionPredictions"][0]["emotion"]
        target = formatted_response["emotionPredictions"][0]["target"]
        emotionMentions = formatted_response["emotionPredictions"][0]["emotionMentions"]
        return {
            "emotion": emotion,
            "target": target,
            "emotionMentions": emotionMentions
        }
    return {"emotion": None, "target": None, "emotionMentions": None}
