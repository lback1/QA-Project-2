from application import app
from flask import request

@app.route('/player_damage', methods=['POST'])
def player_damage():
    damage = 0
    data_sent = request.get_json()

    if data_sent['weapons'] == 'Dual Pistols':
        damage += 15
    if data_sent['weapons'] == 'Compact SMG':
        damage += 30     
    if data_sent['weapons'] == 'Drum Gun':
        damage += 45
    if data_sent['weapons'] == 'Grenade Launcher':
        damage += 60
    if data_sent['weapons'] == 'Tactical Shotgun':
        damage += 75
    if data_sent['weapons'] == 'SCAR':
        damage += 90
    if data_sent['weapons'] == 'Rocket Launcher':
        damage += 105
    if data_sent['weapons'] == 'Heavy Sniper':
        damage += 120

    if data_sent['rarities'] == 'Common':
        damage += 20
    if data_sent['rarities'] == 'Uncommon':
        damage += 40
    if data_sent['rarities'] == 'Rare':
        damage += 60
    if data_sent['rarities'] == 'Epic':
        damage += 80
    if data_sent['rarities'] == 'Legendary':
        damage += 100
    if data_sent['rarities'] == 'Mythic':
        damage += 200

    return str(damage)