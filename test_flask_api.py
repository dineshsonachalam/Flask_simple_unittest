from app import app
from unittest import TestCase
import json
import sys

class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_thing(self):
        response = self.app.get('/')
        #print(json.loads(response.get_data().decode(sys.getdefaultencoding())))
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {'hello': 'world'}
        )

    def test_next(self):
        response = self.app.get('/test')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {'message':'test'}
        )






