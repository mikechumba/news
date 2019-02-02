from flask import Flask,render_template
from app import app

app = Flask(__name__)

@app.route('/')
def home():
       return render_template('home.html', headlines=the_news)