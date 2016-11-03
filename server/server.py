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
    battery = round (resultat['data']['sensors'][1]['value'], 2)
    humidity = round(resultat['data']['sensors'][2]['value'], 2)
    temperature = round(resultat['data']['sensors'][3]['value'],2)
    noise = round(resultat['data']['sensors'][7]['value'],2)
    pollutionno2 = round(resultat['data']['sensors'][4]['value'],2)
    pollutionco = round(resultat['data']['sensors'][5]['value'],2)
    light = round(resultat['data']['sensors'][0]['value'],2)
    page = jinja_env.get_template('base.html')
    return page.render(emplacement1=battery, emplacement2=humidity, emplacement3=temperature, emplacement4=noise, emplacement5=pollutionno2, emplacement6=pollutionco, emplacement7=light)

@app.route("/profiles")
def profiles():
    page = jinja_env.get_template('profiles.html')
    return page.render()

#<<<<<<< Updated upstream
@app.route("/maps.html")
def maps():

    page = jinja_env.get_template('profiles.html')
@app.route("/contacts")
def contacts():
    page = jinja_env.get_template('contacts.html')
#>>>>>>> Stashed changes
    return page.render()

if __name__ == "__main__":
    app.run(port=10000)
