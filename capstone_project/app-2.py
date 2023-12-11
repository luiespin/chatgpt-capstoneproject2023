from flask import Flask, render_template, request
from brain_module import ChatGPT
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['user_message']
    bot = ChatGPT()
    response = bot.request_openai(user_message)
    # Handle the user's message (you can perform actions or generate a response here)
    # For simplicity, let's echo the message back in this example.
    return render_template('index.html', chatgpt_message=response)


if __name__ == '__main__':
    app.run(debug=True)
