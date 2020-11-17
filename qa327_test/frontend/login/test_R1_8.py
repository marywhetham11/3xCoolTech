import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.8
R1.8 - Password has to meet the required complexity
"""

class FrontEndLoginR1(BaseCase):

    def test_passwordFormCheck(self, *_):
        """
        This function tests all conditions of the password form and that
        the correct warning message is displayed
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

        # open login page
        self.open(base_url + '/login')
        # enter an valid email
        self.type("#email", "test@domain.ext")
        # enter an invalid password - too short
        self.type("#password", "P@ss1")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Password format incorrect: Must be greater than 5 characters", "#message")

        # open login page
        self.open(base_url + '/login')
        # enter an valid email
        self.type("#email", "test@domain.ext")
        # enter an invalid password - no upper case
        self.type("#password", "p@ssword1")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Password format incorrect: Must contain an uppercase character", "#message")

        # open login page
        self.open(base_url + '/login')
        # enter an valid email
        self.type("#email", "test@domain.ext")
        # enter an invalid password - no lower case
        self.type("#password", "P@SSWORD1")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Password format incorrect: Must contain a lowercase character", "#message")

        # open login page
        self.open(base_url + '/login')
        # enter an valid email
        self.type("#email", "test@domain.ext")
        # enter an invalid password - no special symbol
        self.type("#password", "pAssword1")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Password format incorrect: Must contain a special character", "#message")
