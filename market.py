from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/register")
def register_page():
    return render_template('register.html')

@app.route("/market")
def market_page():
    items = [
            {
                'Name':"Brian",
                'Age':14
            },
            {
                'Name':"Brian2",
                'Age':14
            },
            {
                'Name':"Brian3",
                'Age':14
            }
        ]
    return render_template('market.html',items=items)
