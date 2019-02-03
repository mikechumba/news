from flask import Flask,render_template
from app import request
from app import app

get_sources = request.get_sources()

@app.route('/')
def home():
       return render_template('home.html', sources=get_sources)

@app.route('/<news_source>')
def highlights(news_source):
       return render_template('highlights.html', id=news_source)
