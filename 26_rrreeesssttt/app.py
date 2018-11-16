#Isaac Jon
#SoftDev1 pd6
#K26 -- Getting More REST
#2018-11-16

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route('/')
def helloWorld():
    #Guardian Lookup. Content: Fortnite
    api_key = "91ed4ccb-fb9f-45b1-9cb1-90f15581898d"
    url_link = "https://content.guardianapis.com/search?q=fortnite&api-key=[]"
    url= url_link.replace('[]',api_key)
    result = json.loads(urllib.request.urlopen(url).read())
    #==============================

    #Google Books
    #No need for api_key
    gbUrl = "https://www.googleapis.com/books/v1/volumes?q=isbn:0575087056"
    gbResult = json.loads(urllib.request.urlopen(gbUrl).read())
    #================================

    #Numbers API
    #No need for api key
    nUrl = "http://numbersapi.com/random/math"
    nResult = urllib.request.urlopen(nUrl).read()

    return render_template('index.html', guard=result['response']['results'], gb=gbResult['items'][0]['volumeInfo'], num=nResult)
if __name__ == '__main__':
    app.debug = True
    app.run()
