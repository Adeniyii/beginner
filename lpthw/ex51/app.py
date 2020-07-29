from flask import request
from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():

    greeting = "Hello World!"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}!"
        return render_template('index.html', greeting=greeting)

    else:
        return render_template('hello_form.html')


@app.route('/hello2', methods=['POST', 'GET'])
def hello2():
    return render_template('index.html', greeting="SHAKABULA")


if __name__ == "__main__":
    app.run() 
