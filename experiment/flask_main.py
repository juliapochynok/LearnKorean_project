
from flask import Flask, request, render_template, url_for
from main import make_userfile
from classes import User, WordController

ACC_NAME = ''
FILE_NAME = ''
USER = User()
TRUE_ANSWER = ''

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('start_page.html')

@app.route('/log_in', methods=['POST'])
def log_in():
    if request.method == 'POST':
        acct = request.form['accaunt']
        if " " not in acct and acct != "":
            global ACC_NAME
            ACC_NAME = acct
            return render_template('time_usage_page.html')
        else:
            return render_template('start_page2.html')


@app.route('/log_in2', methods=['POST'])
def log_in2():
    if request.method == 'POST':
        usg_time = request.form['usage_time']
        answ = ['yes', 'YES', 'Yes', 'no', 'NO', 'No']
        if usg_time in answ:
            file_name = make_userfile(ACC_NAME, usg_time)
            global FILE_NAME
            FILE_NAME = file_name
            global USER
            USER = User(FILE_NAME)
            USER.set_file(FILE_NAME)
            return render_template('options.html')
        else:
            return render_template('time_usage_page2.html')

USER.set_file(FILE_NAME)

@app.route('/learn', methods=['POST'])
def learn():
    if request.method == 'POST':
        word = USER.learn_new_word()
        word = word.split("\n")
    return render_template('learn_word.html', word=word)


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        answers = USER.test_yourself(1)
        if answers == False:
            return render_template('no_words.html')
        else:
            global TRUE_ANSWER
            TRUE_ANSWER = answers[0]
            false_answ = answers[1]
            word = answers[2]
            return render_template('test_yourself.html', answers = false_answ, word = word)

@app.route('/check_test', methods=['POST'])
def check_test():
    if request.method == 'POST':
        client_answ = request.form['client_answ'] 
        if client_answ == TRUE_ANSWER:
            return render_template("true_an.html", true_answ = TRUE_ANSWER)
        else:
            return render_template("false_an.html",  true_answ = TRUE_ANSWER)


@app.route('/wordlist', methods=['POST'])
def wordlist():
    if request.method == 'POST':
        words = USER.see_word_list()
        words = words.split("\n")
    return render_template('see_wordlist.html', words = words)


@app.route('/log_out', methods=['POST'])
def log_out():
    return render_template('start_page.html')


@app.route('/options', methods=['POST'])
def back_to_options():
    return render_template('options.html')


if __name__ == "__main__":
    app.run()
