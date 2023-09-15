from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'kickflip'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    if 'low_guess' not in session:
        session['low_guess'] = None
    if 'high_guess' not in session:
        session['high_guess'] = None
    message = None

    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < session['number']:
            message = 'Too low! Try again.'
            session['low_guess'] = guess
        elif guess > session['number']:
            message = 'Too high! Try again.'
            session['high_guess'] = guess
        elif guess == session['number']:
            message = 'Congratulations! You guessed it!'
        else:
            message = ''
            session.pop('number')
            session['low_guess'] = None
            session['high_guess'] = None
        return render_template('index.html', message=message, low_guess=session['low_guess'], high_guess=session['high_guess'])
    return render_template('index.html', message=message, low_guess=session['low_guess'], high_guess=session['high_guess'])

if __name__ == '__main__':
    app.run(debug=True)
