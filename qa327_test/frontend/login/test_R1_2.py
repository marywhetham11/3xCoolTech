import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.2
R1.2 - Login page has a default message that says please login
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)


class FrontEndLoginR1(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_loginMessageCheck(self, *_):
        """
        This function tests that the /login page has a default message 
        which says 'Please login'
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # make sure the page is /login
        self.assert_element("#header")
        self.assert_text("Log In", "#header")
        # check that the message is displayed 
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

