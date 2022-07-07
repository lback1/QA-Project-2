from application import app
from random import choice

@app.route('/get_weapon', methods=['GET'])
def get_weapon():
    weapons = ['Heavy Sniper', 'SCAR', 'Drum Gun', 'Compact SMG', 'Tactical Shotgun', 'Dual Pistols', 'Rocket Launcher', 'Grenade Launcher']
    return choice(weapons)