
from flask import Flask, render_template
import requests
from models import headlines
Headlines = headlines.Headlines

app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')

@app.route('/')
def home():
       return render_template('home.html', headlines=get_headlines('bbc-news'))

def get_headlines(source):

       api_key = app.config['API_KEY']
       url = (f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey=')
       get_url = (f'{url}{api_key}')
       response = requests.get(get_url)
       the_news = response.json()
       the_news = the_news['articles']

       articles = []

       for news in the_news:
              author = news['author']
              title = news['title']
              description = news['description']
              url = news['url']
              url_to_image = news['urlToImage']
              published_at = news['publishedAt']

              if the_news:
                     the_articles = Headlines(author,title,description,url,url_to_image,published_at)
                     articles.append(the_articles)

       return articles

if __name__ == '__main__':
  app.run(debug=True)