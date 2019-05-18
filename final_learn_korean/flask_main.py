
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
    '''
    Returns start page.
    '''
    return render_template('start_page.html')

@app.route('/log_in', methods=['POST'])
def log_in():
    '''
    Returns page that asks if it's your first time 
    using this program if you enter right account name
    if you enter wrong account name - returns start page 
    '''
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
    '''
    Returns page with options - menu page
    '''
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


@app.route('/learn', methods=['POST'])
def learn():
    '''
    Return page for learning new word
    '''
    if request.method == 'POST':
        word = USER.learn_new_word()
        if word == None:
            return render_template('no_more_words.html')
        word = word.split("\n")
    return render_template('learn_word.html', word=word)


@app.route('/test', methods=['POST'])
def test():
    '''
    Returns test page
    '''
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
    '''
    Check test and returns True of False page depending on user answer
    '''
    if request.method == 'POST':
        client_answ = request.form['client_answ'] 
        if client_answ == TRUE_ANSWER:
            return render_template("true_an.html", true_answ = TRUE_ANSWER)
        else:
            return render_template("false_an.html",  true_answ = TRUE_ANSWER)


@app.route('/wordlist', methods=['POST'])
def wordlist():
    '''
    Returns page with s wordlist
    '''
    if request.method == 'POST':
        words = USER.see_word_list()
        words = words.split("\n")
    return render_template('see_wordlist.html', words = words)


@app.route('/log_out', methods=['POST'])
def log_out():
    '''
    Returns start page
    '''
    return render_template('start_page.html')


@app.route('/options', methods=['POST'])
def back_to_options():
    '''
    Returns options-menu page
    '''
    return render_template('options.html')


if __name__ == "__main__":
    app.run()
