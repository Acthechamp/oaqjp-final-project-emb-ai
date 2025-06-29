from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_api():
    # Get text from the URL query parameter
    text_to_analyze = request.args.get("textToAnalyze")

    # If empty input, return error message
    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # If the function returns None (error or blank), return message
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    # Format the result into a string response
    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_result, 200
