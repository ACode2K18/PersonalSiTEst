from flask import Flask, render_template
from random import randint 

x = ["I was gonna pay my child support but then I got high", "Don't cry because it's over, smile because it happened", "Be yourself; everyone else is already taken"]

app = Flask(__name__) 

@app.route("/")
def index():
	return "Hello world!"

@app.route("/hello")
def hi():
	return "Hi!"

@app.route("/randomquote")
def bye():
	return render_template('test.html')



if __name__ == '__main__':
	app.run(debug=True)