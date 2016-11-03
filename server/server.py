# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
app = Flask(__name__)

#Dashboard Template
from jinja2 import Environment, PackageLoader
jinja_env = Environment(loader=PackageLoader('server','views'))

@app.route("/")
def home():
    import requests
    data = requests.get('https://api.smartcitizen.me/v0/devices/3740')
    resultat = data.json()
    battery = resultat['data']['sensors'][0]['value']
    humidity = resultat['data']['sensors'][1]['value']
    temperature = resultat['data']['sensors'][2]['value']
    noise = resultat['data']['sensors'][6]['value']
    pollutionno2 = resultat['data']['sensors'][3]['value']
    pollutionco = resultat['data']['sensors'][4]['value']

    lat = resultat ['data']['location']['latitude']['value']
    longi = resultat ['data']['location']['longitude']['value']

    page = jinja_env.get_template('base.html')
    return page.render(emplacement1=battery, emplacement2=humidity, emplacement3=temperature, emplacement4=noise, emplacement5=pollutionno2, emplacement6=pollutionco, emplacement7=lat, emplacement8=longi)

@app.route("/profiles")
def profiles():
    page = jinja_env.get_template('profiles.html')
    return page.render()

@app.route("/maps")
def maps():
    page = jinja_env.get_template('localization.html')
    return page.render()
    
if __name__ == "__main__":
    app.run(port=10000)
