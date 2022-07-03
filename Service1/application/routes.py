from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    weapons = requests.get('http://Service2:5000/get_weapon').text
    rarities = requests.get('http://Service3:5000/get_rarity').text
    player_damage = requests.post('http://Service4:5000/damage', json=dict(weapons=weapons, rarities=rarities))
    return render_template('home.html', player_damage=player_damage.text)