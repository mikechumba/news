import unittest
from .headlines import Headlines

class HeadlinesTest(unittest.TestCase):
   '''
   Tests the behaviour of the Headlines Class
   '''

   def setUp(self):
      '''
      Method to run before every test
      '''
      self.headline = Headlines('Glenn Greenwald',
      'Video: The Dramatic Scandal Swallowing the Bolsonaro Presidency Just Drove an LGBT Congressman to Flee Brazil',
      'Bolsonaro is trash.','https://images.google.com','https://images.google.com','January 25 2019')

   def test_init(self):

      self.assertEqual(self.headline.author,'Glenn Greenwald')
      self.assertEqual(self.headline.title,'Video: The Dramatic Scandal Swallowing the Bolsonaro Presidency Just Drove an LGBT Congressman to Flee Brazil')
      self.assertEqual(self.headline.description,'Bolsonaro is trash')
      self.assertEqual(self.headline.url,'https://images.google.com')
      self.assertEqual(self.headline.url_to_image,'https://images.google.com')
      self.assertEqual(self.headline.published_at,'January 25 2019')


if __name__ == '__main__':
   unittest.main()