from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", input1=8, input2=8)

@app.route('/<int:input1>')
def checkerboard_rows(input1):
    return render_template("index.html", input1=input1, input2=8)

@app.route('/<int:input1>/<int:input2>')
def checkerboard_custom(input1, input2):
    return render_template("index.html", input1=input1, input2=input2)

@app.route('/<int:input1>/<int:input2>/<color1>/<color2>')
def checkerboard_custom_colors(input1, input2, color1, color2):
    return render_template("index.html", input1=input1, input2=input2, color1=color1, color2=color2)

@app.route('/static/style.css')
def style():
    return app.send_static_file('style.css')

@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
