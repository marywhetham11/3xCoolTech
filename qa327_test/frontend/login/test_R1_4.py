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

class FrontEndLoginR1(BaseCase):

    def test_loginForm(self, *_):
        """
        This function tests that the user can type into the two
        forms 'email' and 'password'
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')

        # test if the email form loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password form loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")

        # enter users email and password into the forms
        self.type("#email", "test@test.com")
        self.type("#password", generate_password_hash('test_password'))
