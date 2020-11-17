import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.4
R1.4 - The login page provides a login form which requests two fields: email and passwords
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)


class FrontEndLoginR1(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_loginForm(self, *_):
        """
        This function tests that the user can type into the two
        forms 'email' and 'password'
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter users email and password into the forms
        self.type("#email", "test@test.com")
        self.type("#password", generate_password_hash('test_password'))

