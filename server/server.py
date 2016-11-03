# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time

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

    page = jinja_env.get_template('base.html')
    return page.render(emplacement1=battery, emplacement2=humidity, emplacement3=temperature, emplacement4=noise, emplacement5=pollutionno2, emplacement6=pollutionco)

@app.route("/profiles")
def profiles():
    page = jinja_env.get_template('profiles.html')
    return page.render()

@app.route("/clak")
def clak():
    time.sleep(15)
    return "YES"

# Upload snapshot
@app.route("/shot", methods=['POST'])
def shot():
   if request.method == 'POST':
       # check if the post request has the file part
       if 'image' not in request.files:
           return 'ERROR: No file..'

       file = request.files['image']
       if not file or file.filename == '':
           return 'ERROR: Wrong file..'

       # Save Snapshot with Timestamp
       filepath = os.path.join(os.path.dirname(os.path.abspath(__file__))+'/static/upload/', "usershot.jpg")
       file.save(filepath)
       print ("picture taken and saved")
       return 'SUCCESS'
   return 'ERROR: You\'re lost Dave..'


if __name__ == "__main__":
    app.run()
