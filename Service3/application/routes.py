from application import app
import random

@app.route('/rarities', methods=['GET'])
def rarities():
    rarities = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']
    return random.choice(rarities)