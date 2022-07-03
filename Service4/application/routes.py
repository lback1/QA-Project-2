from flask import request
from application import app

@app.route('/damage', methods=['POST'])
def player_damage():
    player_damage = 0
    data = request.get_json()

    if data['weapons'] == 'Dual Pistols':
        player_damage + 15
    if data['weapons'] == 'Compact SMG':
        player_damage + 30     
    if data['weapons'] == 'Drum Gun':
        player_damage + 45
    if data['weapons'] == 'Grenade Launcher':
        player_damage + 60
    if data['weapons'] == 'Tactical Shotgun':
        player_damage + 75
    if data['weapons'] == 'SCAR':
        player_damage + 90
    if data['weapons'] == 'Rocket Launcher':
        player_damage + 105
    if data['weapons'] == 'Heavy Sniper':
        player_damage + 120

    if data['rarities'] == 'Common':
        player_damage + 20
    if data['rarities'] == 'Uncommon':
        player_damage + 40
    if data['rarities'] == 'Rare':
        player_damage + 60
    if data['rarities'] == 'Epic':
        player_damage + 80
    if data['rarities'] == 'Legendary':
        player_damage + 100
    if data['rarities'] == 'Mythic':
        player_damage + 200

    return str(player_damage)