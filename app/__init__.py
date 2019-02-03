from flask import Flask
from scss import Scss

app = Flask(__name__)

if __name__=='__main__':
   app.run(debug=True)

   
from app import error
from app import main
from app import models