from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is my test homepage'

@app.route('/about')
def tuna():
    return'My name is <h2>Maria</h2>. <em>I am learning Python.</em>'

@app.route('/profile/<username>')
def profile(username):
    return "Good morning my love %s" %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Your post ID is %s" %post_id

if __name__ == "__main__":
    app.run()
