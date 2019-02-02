from flask import Flask, render_template
app = Flask(__name__,instance_relative_config=True)

app.config.from_pyfile('config.py')

@app.route('/')
def home():
       return render_template('home.html')


if __name__ == '__main__':
  app.run(debug=True)