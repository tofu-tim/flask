from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'kickflip'

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/process', methods=['POST'])
def process():
    session['first_name'] = request.form['first_name']
    session['middle_name'] = request.form['middle_name']
    session['last_name'] = request.form['last_name']
    session['address'] = request.form['address']
    session['city'] = request.form['city']
    session['state'] = request.form['state']
    session['zip_code'] = request.form['zip_code']
    session['fav_programming_language'] = request.form['fav_programming_language']
    session['comment'] = request.form['comment']

    return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)
