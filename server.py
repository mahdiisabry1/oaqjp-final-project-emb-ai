"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.
"""


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def senti_analyzer():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    stored_text = emotion_detector(text_to_analyze)
    if stored_text['dominant_emotion'] is not None:
        anger = stored_text['anger']
        disgust = stored_text['disgust']
        fear = stored_text['fear']
        joy = stored_text['joy']
        sadness = stored_text['sadness']
        dominant_emotion = stored_text['dominant_emotion']
        return (
            f"For the given statement, the system response is  'anger': {anger} "
            f"'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}." 
            )
    return "invalid input ! try agin"

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
