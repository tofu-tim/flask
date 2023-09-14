from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'kickflip'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('counter.html', visit_count=session['counter'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two_visits')
def add_two_visits():
    session['counter'] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
