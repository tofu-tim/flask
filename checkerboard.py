from flask import Flask, render_template, redirect, request

app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template("index.html", rows=8, cols=8, color1="black", color2="white")

@app.route('/<int:rows>')
def checkerboard_rows(rows):
    return render_template("index.html", rows=rows, cols=8, color1="black", color2="white")

@app.route('/<int:rows>/<int:cols>')
def checkerboard_custom(rows, cols):
    return render_template("index.html", rows=rows, cols=cols, color1="black", color2="white")

@app.route('/<int:rows>/<int:cols>/<color1>/<color2>')
def checkerboard_custom_colors(rows, cols, color1, color2):
    return render_template("index.html", rows=rows, cols=cols, color1=color1, color2=color2)

@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

