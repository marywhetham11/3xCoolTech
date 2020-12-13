import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from qa327.backend import get_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for the backend.py method login_user.
This method returns an instance of the user with the given email if the password
given is correct for that user
"""

test_user = User(
    email='test_backend@test.com',
    name='test_backend',
    password='Test_Backend_Password'
)

class BackEndGetUser(BaseCase):

    def test_loginUserT1(self, *_):
        """
        This function tests test T1 for login_user conditional coverage testing ("not user" : true)
        """

        # create the user test_user if they don't already exist in the database
        if (not get_user(test_user.email)):
            # open register page
            self.open(base_url + '/register')
            # fill email, user name and password
            self.type("#email", test_user.email)
            self.type("#name", test_user.name)
            self.type("#password", test_user.password)
            self.type("#password2", test_user.password)
            # click enter button
            self.click('input[type="submit"]')

        # check if "not user" equals true results in entering the block (returns None)
        self.assert_equal(login_user("not_a_user", test_user.password), None)

    def test_loginUserT2(self, *_):
        """
        This function tests test T2 for login_user conditional coverage testing ("not user" : false and
        "not check_password_hash(user.password, password)" : false)
        """

        # create the user test_user if they don't already exist in the database
        if (not get_user(test_user.email)):
            # open register page
            self.open(base_url + '/register')
            # fill email, user name and password
            self.type("#email", test_user.email)
            self.type("#name", test_user.name)
            self.type("#password", test_user.password)
            self.type("#password2", test_user.password)
            # click enter button
            self.click('input[type="submit"]')

        # check if "not user" or "not check_password_hash(user.password, password)" equals false
        # results in not entering the block (returns user)
        self.assert_equal(login_user(test_user.email, test_user.password), get_user(test_user.email))

    def test_loginUserT3(self, *_):
        """
        This function tests test T3 for login_user conditional coverage testing 
        ("not check_password_hash(user.password, password)" : true)
        """

        # create the user test_user if they don't already exist in the database
        if (not get_user(test_user.email)):
            # open register page
            self.open(base_url + '/register')
            # fill email, user name and password
            self.type("#email", test_user.email)
            self.type("#name", test_user.name)
            self.type("#password", test_user.password)
            self.type("#password2", test_user.password)
            # click enter button
            self.click('input[type="submit"]')

        # check if "not check_password_hash(user.password, password)r" equals true results 
        # in entering the block (returns None)
        self.assert_equal(login_user(test_user.email, "not_correct_password"), None)