import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/CoCa')

def hello():
    return render_template('kursy_walut.html', kursy = dane())

def dane():
    r = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/usd/today/?format=json')
    print(r.json())
    return r.json()
app.run()
