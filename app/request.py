
from flask import Flask, render_template
import requests

app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')


def get_headlines():


       api_key = app.config['API_KEY']
       url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
       get_url = (f'{url}{api_key}')
       response = requests.get(get_url)
       the_news = response.json()

if __name__ == '__main__':
  app.run(debug=True)