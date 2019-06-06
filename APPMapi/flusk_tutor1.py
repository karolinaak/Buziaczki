from flask import Flask, flash, redirect, render_template, request, session, abort
import requests

def grabapidata(apistring):
    resp = requests.get(apistring)
#   resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/a/today/")

    return resp.json()

gbptop10 = grabapidata("http://api.nbp.pl/api/exchangerates/rates/a/gbp/last/10/?format=json")
chftop10 = grabapidata("http://api.nbp.pl/api/exchangerates/rates/a/chf/last/10/?format=json")
usdtop10 = grabapidata("http://api.nbp.pl/api/exchangerates/rates/a/usd/last/10/?format=json")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('html_template.html', name=name)

@app.route("/")
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('html_template.html', name=name)

@app.route("/gbp10")
@app.route("/gbp10/<name>")
def gbp10(name=None):
    return render_template('html_template.html', name=gbptop10)
@app.route("/chf10")
@app.route("/chf10/<name>")
def chf10(name=None):
    return render_template('html_template.html', name=chftop10)
@app.route("/usd10")
@app.route("/usd10/<name>")
def usd10(name=None):
    return render_template('html_template.html', name=usdtop10)

@app.route("/hello2/<string:name>/")
def hello2(name):
    return render_template('temp_pretty.html',name=name) #</string:name>

if __name__ == "__main__":
    app.run()