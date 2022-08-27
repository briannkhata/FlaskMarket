from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return "<h1>About Page</h1>"

@app.route('/profile/<username>')
def profile_page(username):
    return f"<h1>Profile for {username}</h1>"