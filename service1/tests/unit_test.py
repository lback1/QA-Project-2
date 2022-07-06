from application import app
from flask_testing import TestCase
from flask import url_for
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFront(TestBase):
    def test_get_front_1(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/get_weapon', text = 'SCAR')
            m.get('http://service3:5000/get_rarity', text = 'Epic')
            m.post('http://service4:5000/player_damage', text = '170')
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'170 Player Damage', response.data)

    def test_get_front_2(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5000/get_weapon', text = 'Heavy Sniper')
            m.get('http://service3:5000/get_rarity', text = 'Legendary')
            m.post('http://service4:5000/player_damage', text = '220')
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'220 Player Damage', response.data)