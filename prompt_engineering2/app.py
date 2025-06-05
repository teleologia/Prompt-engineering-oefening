from flask import Flask, request, jsonify, render_template
from openai import OpenAI
app = Flask(__name__)
# Initialize OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/get_css_colors', methods=['POST'])
def get_css_colors():
    mood = request.json['mood']
    response = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
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