from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/page0")
def page0():
	return "page0 is up and running"
	
@app.route("/page1")
def page1():
	return "page1 is up and running"
	
app.run()
