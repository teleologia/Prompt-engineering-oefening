from flask import Flask, request, jsonify, render_template
import sqlite3
import openai
app = Flask(__name__)
# Configure OpenAI API Key  
openai.api_key = ''
def execute_query(query):
    connection = sqlite3.connect('chocolate_shop.db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Given the following SQL tables, your job is to write queries given a user’s request.\n\n    CREATE TABLE IF NOT EXISTS Products (\n      product_id INTEGER PRIMARY KEY,\n      name TEXT NOT NULL,\n      description TEXT,\n      price REAL NOT NULL,\n      stock INTEGER NOT NULL\n    );\n\n    CREATE TABLE IF NOT EXISTS Customers (\n      customer_id INTEGER PRIMARY KEY,\n      name TEXT NOT NULL,\n      email TEXT NOT NULL UNIQUE\n    );\n\n    CREATE TABLE IF NOT EXISTS Orders (\n      order_id INTEGER PRIMARY KEY,\n      customer_id INTEGER,\n      product_id INTEGER,\n      quantity INTEGER NOT NULL,\n      order_date TEXT NOT NULL,\n      FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),\n      FOREIGN KEY(product_id) REFERENCES Products(product_id)\n    ); only return the raw sql query nothing else (eg: SELECT AVG(total_value) AS average_order_value FROM (SELECT SUM(p.price * o.quantity) AS total_value FROM Orders o JOIN Products p ON o.product_id = p.product_id WHERE o.order_date = '2023-04-01' GROUP BY o.order_id) AS order_totals);"
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
        temperature=0.7,
        max_tokens=150
    )
    sql_query = response.choices[0].message.content
    sql_query = sql_query.strip().strip('```sql').strip('```')
    print(f"SQL Query generated: {sql_query}")
    try:
        result = execute_query(sql_query)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
if __name__ == '__main__':
    app.run(debug=True)