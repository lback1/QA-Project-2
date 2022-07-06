from application import app, routes
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestRarities(TestBase):
    @patch('application.routes.choice', return_value='Common')
    def test_get_rarity_1(self, patched):
        response = self.client.get(url_for('get_rarity'))
        self.assert200(response)
        self.assertIn(b'Common', response.data)

    @patch('application.routes.choice', return_value='Uncommon')
    def test_get_rarity_2(self, patched):
        response = self.client.get(url_for('get_rarity'))
        self.assert200(response)
        self.assertIn(b'Uncommon', response.data)

    @patch('application.routes.choice', return_value='Rare')
    def test_get_rarity_3(self, patched):
        response = self.client.get(url_for('get_rarity'))
        self.assert200(response)
        self.assertIn(b'Rare', response.data)

    @patch('application.routes.choice', return_value='Epic')
    def test_get_rarity_4(self, patched):
        response = self.client.get(url_for('get_rarity'))
        self.assert200(response)
        self.assertIn(b'Epic', response.data)

    @patch('application.routes.choice', return_value='Legendary')
    def test_get_rarity_5(self, patched):
        response = self.client.get(url_for('get_rarity'))
        self.assert200(response)
        self.assertIn(b'Legendary', response.data)

    @patch('application.routes.choice', return_value='Mythic')
    def test_get_rarity_6(self, patched):
        response = self.client.get(url_for('get_rarity'))
        self.assert200(response)
        self.assertIn(b'Mythic', response.data)