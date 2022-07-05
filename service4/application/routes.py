from application import app
from flask import request

@app.route('/player_damage', methods=['POST'])
def player_damage():
    damage = 0
    data = request.get_json()

    if data['weapons'] == 'Dual Pistols':
        damage += 15
    if data['weapons'] == 'Compact SMG':
        damage += 30     
    if data['weapons'] == 'Drum Gun':
        damage += 45
    if data['weapons'] == 'Grenade Launcher':
        damage += 60
    if data['weapons'] == 'Tactical Shotgun':
        damage += 75
    if data['weapons'] == 'SCAR':
        damage += 90
    if data['weapons'] == 'Rocket Launcher':
        damage += 105
    if data['weapons'] == 'Heavy Sniper':
        damage += 120

    if data['rarities'] == 'Common':
        damage += 20
    if data['rarities'] == 'Uncommon':
        damage += 40
    if data['rarities'] == 'Rare':
        damage += 60
    if data['rarities'] == 'Epic':
        damage += 80
    if data['rarities'] == 'Legendary':
        damage += 100
    if data['rarities'] == 'Mythic':
        damage += 200

    return str(damage)