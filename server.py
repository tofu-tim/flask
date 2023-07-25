from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<name>')
def hello(name):
    return "Hi, " + name

@app.route('/repeat/<int:num>/<string>')
def repeat_string(string, num):
    return string * num

@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)