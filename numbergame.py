from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'kickflip'  # Change this to a secure random key

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    low_guess = 25
    high_guess = 75
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < session['number']:
            message = 'Too low! Try again.'
        elif guess > session['number']:
            message = 'Too high! Try again.'
        else:
            message = 'Congratulations! You guessed it!'
            session.pop('number')
        return render_template('index.html', message=message, low_guess=low_guess, high_guess=high_guess)
    return render_template('index.html', message=None, low_guess=low_guess, high_guess=high_guess)

if __name__ == '__main__':
    app.run(debug=True)
