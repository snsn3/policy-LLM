from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# initialize client 
openai.api_key = os.getenv('OPENAI_API_KEY')
#app
@app.route('/')
def index():
    return render_template('index.html')
#app  route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  #model choice as of oct. 2024
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response.choices[0].message['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
