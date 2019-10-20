import unittest

from tests.base_test import BaseTest

class TestModels(unittest.TestCase):
    base = BaseTest()

    def setUp(self):
        self.base.set_up()
        self.u = self.base.load_user('test@gmail.com', 'cat')
        self.u2 = self.base.load_user('test2@gmail.com', 'cat')
        self.u3 = self.base.load_user('test@gmail.com', 'dog')

    def tearDown(self):
        self.base.tear_down()

    def test_password_hashing(self):
        self.assertFalse(self.u.check_password_hash('dog'))
        self.assertTrue(self.u.check_password_hash('cat'))

    def test_random_salts(self):
        self.assertFalse(self.u.password == self.u2.password)
