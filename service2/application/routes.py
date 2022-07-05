from flask import jsonify
from application import app
import random

@app.route('/get_weapon', methods=['GET'])
def get_weapon():
    weapons = ['Heavy Sniper', 'SCAR', 'Drum Gun', 'Compact SMG', 'Tactical Shotgun', 'Dual Pistols', 'Rocket Launcher', 'Grenade Launcher']
    return jsonify(random.choice(list(weapons)))