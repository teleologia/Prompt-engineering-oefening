from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", "")
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/get_css_colors', methods=['POST'])
def get_css_colors():
    mood = request.json['mood']
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a description of a mood, and your task is to generate the CSS code for three colors that match it. Write your output in json with a single key called \"css_code\".return just the json object nothing else"
            },
            {
                "role": "user",
                "content": mood
            }
        ],
        temperature= 0.7,
    )
    css_code = response.choices[0].message.content
    print(css_code)
    return jsonify(eval(css_code))
if __name__ == '__main__':  
    app.run(debug=True)