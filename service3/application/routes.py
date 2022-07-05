from application import app
import random

@app.route('/get_rarity', methods=['GET'])
def get_rarity():
    rarities = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']
    return random.choice(rarities)