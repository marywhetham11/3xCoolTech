import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from qa327.backend import get_user
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for the backend.py method get_user.
This method returns an instance of the user with the given email
"""

test_user = User(
    email='test_backend@test.com',
    name='test_backend',
    password='Test_Backend_Password'
)

class BackEndGetUser(BaseCase):

    def test_getUserSuccess(self, *_):
        """
        This function tests that if an email that does exist is inputted into
        get_user then the method returns an instance of the user
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

        check_user = get_user(test_user.email)

        # check if check_user is a User instance and contains the correct information
        self.assert_true(isinstance(check_user, User))
        self.assert_equal(check_user.email, test_user.email)
        self.assert_equal(check_user.name, test_user.name)
        self.assert_true(check_password_hash(check_user.password,test_user.password))

    def test_getUserFail(self, *_):
        """
        This function tests that if an email that does not exist is inputted into
        get_user then the method returns None
        """
        self.assert_equal(get_user("not_an_email@test.com"), None)