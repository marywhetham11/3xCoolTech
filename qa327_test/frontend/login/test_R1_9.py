import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.9
R1.9 - For any formatting errors, render the login page and show the message email/password format is incorrect.
"""

class FrontEndLoginR1(BaseCase):

    def test_nonMatchingEmailPass(self, *_):
        """
        This function tests that when a valid email and password are entered
        but no ecisting user is found, the propper error message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter a valid email
        self.type("#email", "test@test.com")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("email/password combination incorrect", "#message")
