from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    weapons = requests.get('http://service2:5000/weapons').text
    rarities = requests.get('http://service3:5000/rarities').text
    damage = requests.post('http://service4:5000/damage', json={'weapons':weapons, 'rarities':rarities})
    return render_template('home.html', weapons=weapons, rarities=rarities, damage=damage.text)