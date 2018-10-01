from flask import Flask,render_template,request,session,url_for,redirect

app = Flask(__name__)
username = 'zero123'
password = '1234'
loggedIn = False


@app.route("/")
def helloWorld():
    if loggedin:
        return redirect(url_for("authPage"))
    else:
        return render_template('home.html')

@app.route("/auth")
def authPage():
    if request.args['username'] != username:
        return render_template('welcome.html', message = "Username incorrect ", x = "retry")
    elif request.args['username'] == username: 
        if request.args['password'] == password:
            print(url_for('helloWorld'))
            print(session)
            return render_template('welcome.html', u = username, message = "Welcome ", x = "Logout")
        else:
            return render_template('welcome.html', message = "Password incorrect", x = "retry")


app.debug = True
app.run()
