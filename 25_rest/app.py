#Isaac Jon
#SoftDev1 pd6
#K25 -- Getting More REST
#2018-11-15

from flask import Flask, render_template
import urllib, json
import clearbit

clearbit.key = 'sk_61cc587ea8b9e3237403b8a487d20684'
app = Flask(__name__)

@app.route('/')
def helloWorld():
    url = "https://autocomplete.clearbit.com/v1/companies/suggest?query=Google" #Autocomplete API
    #url2 = 'https://company.clearbit.com/v2/companies/find?domain=google.com' #Returns data about a company
    result = json.loads(urllib.request.urlopen(url).read())
    #result2 = json.loads(urllib.request.urlopen(url2).read())
    return render_template('index.html', res=result)#, res2=result2)

if __name__ == '__main__':
    app.debug = True
    app.run()
