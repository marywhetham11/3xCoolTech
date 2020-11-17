import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.10
R1.10 - If email/password are correct, redirect to /
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)


class FrontEndLoginR1(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_loginRediredUponPost(self, *_):
        """
        This function tests that if the user succesfully logs in they
        are redirected to / home page
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter users email and password
        self.type("#email", "test@test.com")
        self.type("#password", generate_password_hash('test_password'))
        # click enter button
        self.click('input[type="submit"]')
        # check the current redirected page
        self.assert_element("#welcome-header")
        self.assert_text("Welcome ", "#welcome-header")

