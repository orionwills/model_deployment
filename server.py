from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/ada')
def ada_page():
    return 'The ada cohort is my favorite data science cohort!'

@app.route('/roll-dice')
def roll_dice():
    die = randint(1, 6)
    return f'<h1>You rolled a magical {die}!!!'