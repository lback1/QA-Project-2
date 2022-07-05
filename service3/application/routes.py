from flask import jsonify
from application import app
import random

@app.route('/get_rarity', methods=['GET'])
def get_rarity():
    rarities = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']
    return jsonify(random.choice(list(rarities)))