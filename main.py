from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Wert zwischen -1 und 1

    if polarity > 0.1:
        return "Positiv"
    elif polarity < -0.1:
        return "Negativ"
    else:
        return "Neutral"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Bitte 'text' im JSON-Body angeben"}), 400

    text = data['text']
    sentiment = analyze_sentiment(text)

    return jsonify({
        "text": text,
        "sentiment": sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)