import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.6
R1.6 - Email and password both cannot be empty
"""

class FrontEndLoginR1(BaseCase):

    def test_loginFormBothEmpty(self, *_):
        """
        This function tests that the user form cannot be empty, if both are
        empty the message warns the user with an error message
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # click enter button with no input
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Cannot be empty", "#message")

    def test_loginFormEmailEmpty(self, *_):
        """
        This function tests that the user form cannot be empty, if email is
        empty the message warns the user with an error message
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter users password
        self.type("#password", generate_password_hash('test_password'))
        # click enter button with only password
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Cannot be empty", "#message")

    def test_loginFormPassEmpty(self, *_):
        """
        This function tests that the user form cannot be empty, if the password is
        empty the message warns the user with an error message
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter users email
        self.type("#email", "test@test.com")
        # click enter button with only email
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Password format incorrect: Cannot be empty", "#message")

