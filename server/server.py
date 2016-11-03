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
    data = requests.get('https://api.smartcitizen.me/v0/devices/1616')
    resultat = data.json()
    battery = resultat['data']['sensors'][0]['value']
    humidity = resultat['data']['sensors'][1]['value']
    temperature = resultat['data']['sensors'][2]['value']
    page = jinja_env.get_template('base.html')
    return page.render(emplacement1=battery, emplacement2=humidity, emplacement3=temperature)

@app.route("/profiles")
def profiles():
    page = jinja_env.get_template('profiles.html')
    return page.render()

if __name__ == "__main__":
    app.run()
