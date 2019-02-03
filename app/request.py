
from flask import Flask, render_template
import requests
from models import headlines,sources

Sources = sources.Sources
Headlines = headlines.Headlines

app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')

@app.route('/')
def home():
       return render_template('home.html', headlines=get_sources())



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

def get_sources():

       api_key = app.config['API_KEY']
       url = (f'https://newsapi.org/v2/sources?apiKey=')
       get_url = (f'{url}{api_key}')
       response = requests.get(get_url)
       the_news = response.json()
       the_sources = the_news['sources']

       sources = []
       for source in the_sources:
              source_id = source['id']
              name = source['name']
              description = source['description']


              if the_sources:
                     news_sources = Sources(source_id,name,description)
                     sources.append(news_sources)

       return sources

if __name__ == '__main__':
  app.run(debug=True)