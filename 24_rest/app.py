#Isaac Jon
#SoftDev1 pd6
#K24 -- A RESTful Journey Skyward
#2018-11-14

from flask import Flask, render_template
import urllib, json
app = Flask(__name__)

@app.route('/')
def helloWorld():
    api = json.loads(urllib.request.urlopen('https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-11-13&cloud_score=True&api_key=qJF4djMIqZSBeU81jvbqpKKYerJuVO0Y7hZ7pwXV').read())
    print(api)
    return render_template('index.html', image=api['url'])

if __name__ == '__main__':
    app.debug = True
    app.run()
