#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Tests for User class"""
    def setUp(self):
        super().setUp()
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test first_name attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last_name attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
