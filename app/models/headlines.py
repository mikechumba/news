class Headlines:
   '''
   Class holds model for news articles
   '''

   def __init__(self,author,title,description,url,url_to_image,published_at):
      
      self.author = author
      self.title = title
      self.description = description
      self.url = url
      self.url_to_image = url_to_image
      self.published_at = published_at