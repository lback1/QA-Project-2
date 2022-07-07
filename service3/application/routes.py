from application import app
from random import choice

@app.route('/get_rarity', methods=['GET'])
def get_rarity():
    rarities = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']
    return choice(rarities)