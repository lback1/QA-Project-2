from application import app, routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestWeapons(TestBase):
    @patch('application.routes.choice', return_value='Heavy Sniper')
    def test_get_weapon_1(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'Heavy Sniper', response.data)

    @patch('application.routes.choice', return_value='SCAR')
    def test_get_weapon_2(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'SCAR', response.data)

    @patch('application.routes.choice', return_value='Drum Gun')
    def test_get_weapon_3(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'Drum Gun', response.data)

    @patch('application.routes.choice', return_value='Compact SMG')
    def test_get_weapon_4(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'Compact SMG', response.data)

    @patch('application.routes.choice', return_value='Tactical Shotgun')
    def test_get_weapon_5(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'Tactical Shotgun', response.data)

    @patch('application.routes.choice', return_value='Dual Pistols')
    def test_get_weapon_6(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'Dual Pistols', response.data)

    @patch('application.routes.choice', return_value='Rocket Launcher')
    def test_get_weapon_7(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'Rocket Launcher', response.data)

    @patch('application.routes.choice', return_value='Grenade Launcher')
    def test_get_weapon_8(self, patched):
        response = self.client.get(url_for('get_weapon'))
        self.assert200(response)
        self.assertIn(b'Grenade Launcher', response.data)