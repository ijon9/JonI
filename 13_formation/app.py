#Isaac Jon
#SoftDev1 pd6
#K13 -- Echo Echo Echo
#2018-09-28

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def landingPage():
    print(request.method)
    return render_template('home.html')

@app.route("/auth", methods=["POST", "GET"])
def authenticate():
    
    return render_template('auth.html', un=request.args.get("username"))

app.debug = True
app.run()
