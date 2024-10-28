from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the emotion classifier pipeline
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message', '')
    
    if user_message:
        # Get emotion prediction
        prediction = emotion_classifier(user_message)[0]
        emotion = prediction['label']
        
        return jsonify({"message": user_message, "emotion": emotion})
    return jsonify({"message": "", "emotion": "No text provided"})

if __name__ == '__main__':
    app.run(debug=True)
