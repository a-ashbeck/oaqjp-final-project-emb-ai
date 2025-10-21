"""Flask server for the Emotion Detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """Analyze text from the 'textToAnalyze' query param and return emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "<strong>Invalid text! Please try again!</strong>"

    return (
        "For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, and "
        f"'sadness': {sadness_score}. The dominant emotion is "
        f"<strong>{dominant_emotion}</strong>"
    )


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
