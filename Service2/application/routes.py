from application import app
import random

@app.route('/weapons', methods=['GET'])
def weapons():
    weapons = ['Heavy Sniper', 'SCAR', 'Drum Gun', 'Compact SMG', 'Tactical Shotgun', 'Dual Pistols', 'Rocket Launcher', 'Grenade Launcher']
    return random.choice(weapons)