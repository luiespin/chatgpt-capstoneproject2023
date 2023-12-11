from flask import Flask, render_template, request
from brain_module import ChatGPT

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        platform = request.form['platform']
        topic = request.form['topic']

        # Call a function to generate social media post suggestions based on platform and topic
        post_suggestions = generate_post_suggestions(platform, topic)
        bot = ChatGPT()
        response = bot.request_openai(post_suggestions)

        return render_template('index.html', post_suggestions=response)

    return render_template('index.html', post_suggestions=None)


def generate_post_suggestions(platform, topic):
    # Simulated logic to generate post suggestions
    if platform == 'Facebook':
        return f"As a Social Media Manager Assistant, create a Facebook post about {topic}"
    elif platform == 'Instagram':
        return f"As a Social Media Manager Assistant, create an Instagram text post about {topic}"
    elif platform == 'TikTok':
        return f"As a Social Media Manager Assistant, create a TikTok screenplay guide about {topic}"
    else:
        return f"As a Social Media Manager Assistant, create a X text post about {topic}"


if __name__ == '__main__':
    app.run(debug=True)
