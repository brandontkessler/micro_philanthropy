import unittest

from flask import current_app
from tests.base_test import BaseTest

class TestAppSetup(unittest.TestCase):
    base = BaseTest()

    def setUp(self):
        self.base.set_up()

    def tearDown(self):
        self.base.tear_down()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
