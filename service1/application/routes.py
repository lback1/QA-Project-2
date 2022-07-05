from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    weapons = requests.get('http://service2:5000/get_weapon').text
    rarities = requests.get('http://service3:5000/get_rarity').text
    damage = requests.post('http://service4:5000/player_damage', json={'weapons':weapons, 'rarities':rarities})
    return render_template('home.html', damage=damage.text, weapons=weapons, rarities=rarities)