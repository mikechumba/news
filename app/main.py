from flask import Flask,render_template
from app import request
from app import app

get_sources = request.get_sources()

@app.route('/')
def home():
       return render_template('home.html', sources=get_sources)

@app.route('/headlines/<news_source>')
def highlights(news_source):

       get_headlines = request.get_headlines(news_source)
       return render_template('highlights.html', headlines=get_headlines)
