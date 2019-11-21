import time
import unittest
import flask_testing
import requests
#import requests_mock

from flask import url_for, jsonify
from itertools import combinations, product, chain, repeat
from flask_testing import TestCase, LiveServerTestCase

from felfinder.models import db

class BaseTest(TestCase):
    
    def create_app(self):
        
        from flask import session        
        from felfinder import app
        
        self.app = app
        self.app.testing = True
              
        return self.app

    def setUp(self):
        
        self.app.preprocess_request()
        db.create_all()

        self._started_at = time.time()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
        
        elapsed = time.time() - self._started_at
        print('{} ({})'.format(self.id(), round(elapsed, 2)))


class BaseLiveTest(BaseTest, LiveServerTestCase):
    pass


class BasicTests(BaseTest):

    def test_hello(self):
        print("Just a hello")
        assert 1 == 1


unittest.main()
