from flask import render_template, Flask

app = Flask(__name__)

def jobs():
  return render_template('index.html')

@app.route('/')

@app.route('/jobs')

def jobs():
  return render_template('index.html')
