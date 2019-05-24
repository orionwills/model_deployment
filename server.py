from flask import Flask, render_template, request
from random import randint
import numpy as np
from math import factorial as f

app = Flask(__name__)

@app.route('/')
def index():
    number = randint(1,6)
    print('User rolled {}'.format(number))
    return render_template('index.html', random_number=number)

@app.route('/ada')
def ada_page():
    return 'The ada cohort is my favorite data science cohort!'

@app.route('/roll-dice')
def roll_dice():
    die = randint(1, 6)
    print('User rolled', die)
    return '<h1>You rolled a magical {}!!!</h1>'.format(die)

@app.route('/fancy-math-form')
def fancy_math():
    return render_template('fancy-math-form.html')

@app.route('/math-results', methods=["POST"])
def math_results():
    number = request.form['number']
    result = int(number) + 3
    return render_template('math-results.html', number=number, result=result)

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=["POST"])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('make-greeting.html', greeting=greeting)

@app.route('/factorial')
def get_factorial():
    return render_template('factorial.html')

@app.route('/factorial-solved', methods=["POST"])
def factorial():
    f_number = int(request.form['f_number'])
    f_len = len(str(f(f_number)))
    f_solved = str(f(f_number))
    return render_template('factorial-solved.html', f_number=f_number, f_solved=f_solved, f_len=f_len)

@app.route('/resume')
def resume():
    return render_template('resume.html')




###
if __name__ == '__main__':
    import waitress
    waitress.serve(app, port=5005)