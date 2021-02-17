# importing in core Flask modules
from flask import Flask, render_template, url_for, redirect, request
import json

# this is for getting the secret key
with open('secrets.json') as f:
  data = json.load(f)

# creating an instance of Flask as our app
app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']

# redirect to homepage
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/fotc', methods=['GET'])
def fotc():
  return render_template('fotc.html')

@app.route('/compilers', methods=['GET'])
def compilers():
  return render_template('compilers.html')

@app.route('/pipeworks', methods=['GET'])
def pipeworks():
  return render_template('pipeworks.html')



# this is what allows you to run the app
if __name__ == "__main__":
  app.run(debug=True)