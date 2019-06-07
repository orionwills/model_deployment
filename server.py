from flask import Flask, render_template, request
from random import randint
import numpy as np
from math import factorial as f
import pickle
import pandas as pd

app = Flask(__name__,
            static_url_path='',
            static_folder='public/')

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

@app.route('/be-model-agents')
def model_agents():
    return render_template('be-model-agents.html')

@app.route('/predict-agent', methods=["POST"])
def predict_agent():
    avg_sales_trans = int(request.form['avg_sales_trans'])
    trans_count = int(request.form['trans_count'])
    list_trans_count = int(request.form['list_trans_count'])
    buyer_trans_count = int(request.form['buyer_trans_count'])
    list_sell_ratio = list_trans_count / (list_trans_count + buyer_trans_count)
    number_of_zips = request.form['unique_zip_codes']
    # importing the pickle
    with open('public/dt_model_agents.obj', 'rb') as fp:
        dt_model_agents = pickle.load(fp)
    #
    agent_cols = ['trans_count', 'avg_sales_trans', 'list_sell_ratio', 'number_of_zips']
    agent_info = [19, 350000, .75, 5]
    #
    agent_dict = dict(zip(agent_cols, agent_info))
    agent_info = pd.DataFrame(agent_dict, index=[1])
    #
    output = dt_model_agents.predict(agent_info)
    if output == 'True':
        prediction = 'Agent is trending to be a $5mil+ agent.'
    else:
        prediction = 'Agent is not trending to be a $5mil+ agent.'

    return render_template('predict-agent.html',avg_sales_trans=avg_sales_trans,
                                                trans_count=trans_count,
                                                list_trans_count=list_trans_count,
                                                buyer_trans_count=buyer_trans_count,
                                                list_sell_ratio=list_sell_ratio,
                                                unique_zip_codes=number_of_zips,
                                                prediction=prediction)

if __name__ == '__main__':
    import waitress
    waitress.serve(app, port=5005)