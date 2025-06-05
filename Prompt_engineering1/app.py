from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", "")
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
app = Flask(__name__)
reviews = []
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit_review', methods=['POST'])
def submit_review():
    review_text = request.json['review']
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system",
             "content": "You are a sentiment analysis tool. you only return: 'neutral', 'positive' or 'negative' Classify the sentiment of the following review."},
            {"role": "user", "content": review_text}
        ],
        temperature=0.7,
        max_tokens=10,
        n=1,
        stop=None
    )
    sentiment = response.choices[0].message.content
    print(sentiment)
    if 'positive' in sentiment:
        color = 'green'
    elif 'negative' in sentiment:
        color = 'red'
    else:
        color = 'black'
    reviews.append({
        'text': review_text,
        'color': color
    })
    return jsonify(reviews=reviews)
if __name__ == '__main__':
    app.run(debug=True)