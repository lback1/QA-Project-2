from application import app
import random

rarities = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']

@app.route('/get_rarity')
def get_rarity():
    return random.choice(rarities)