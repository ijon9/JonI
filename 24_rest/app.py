from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template(api="https://api.nasa.gov/planetary/apod?api_key=qJF4djMIqZSBeU81jvbqpKKYerJuVO0Y7hZ7pwXV",'templates/index.html')

app.run()
