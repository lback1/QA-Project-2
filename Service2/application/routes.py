from application import app
import random

weapons = ['Heavy Sniper', 'SCAR', 'Drum Gun', 'Compact SMG', 'Tactical Shotgun', 'Dual Pistols', 'Rocket Launcher', 'Grenade Launcher']

@app.route('/get_weapon')
def get_weapon():
    return random.choice(weapons)