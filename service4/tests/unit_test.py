from application import app
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

class TestDamage(TestBase):
    def test_damage_1(self):
        response = self.client.post(
            url_for('player_damage'),
            json = {'weapons':'SCAR', 'rarities':'Mythic'}
        )
        self.assert200(response)
        self.assertIn(b'290', response.data)

    def test_damage_2(self):
        response = self.client.post(
            url_for('player_damage'),
            json = {'weapons':'Dual Pistols', 'rarities':'Rare'}
        )
        self.assert200(response)
        self.assertIn(b'75', response.data)