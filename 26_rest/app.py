#Isaac Jon
#SoftDev1 pd6
#K25 -- Getting More REST
#2018-11-15

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route('/')
def helloWorld():
    api_key = "91ed4ccb-fb9f-45b1-9cb1-90f15581898d"
    url_link = "https://content.guardianapis.com/search?api-key=[]"
    url= url_link.replace('[]',api_key)
    result = json.loads(urllib.request.urlopen(url).read())
    return render_template('index.html', res=result)
if __name__ == '__main__':
    app.debug = True
    app.run()
