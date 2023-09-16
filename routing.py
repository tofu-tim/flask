from flask import Flask
import random

app = Flask(__name__)
app.secret_key = 'kickflip'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    hello = "Hello world!"
    return hello

@app.route('/dojo', methods=['GET', 'POST'])
def hello_dojo():
    dojo = "Heyo Dojo!"
    return dojo

@app.route('/say/<string:name>', methods=['GET', 'POST'])
def say_hi(name):
    greeting = f"Hi {name} "
    return greeting

# @app.route('/repeat/<int:num>/<string:word>', methods=['GET', 'POST'])
# def repetition(num, word):
#     repeated_word = f"{word} " * num
#     return repeated_word

@app.route('/repeat/<int:num>/<string:word>', methods=['GET', 'POST'])
def repetition(num, word):
    repeated_word = '\n'.join([f"{i + 1}. {word}" for i in range(num)])
    return repeated_word


if __name__ == '__main__':
    app.run(debug=True)
