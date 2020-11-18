import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R2.3.
R2.3 - the registration page shows a registration form requesting: email, user name, password, password2
"""

class FrontEndRegistrationR3(BaseCase):

    def test_checkRegisterPage(self, *_):
        """
        This function tests if the email, name, password, and password2 elements
        show up on the register page 
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # test if the registration page loads correctly
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the name element loads correctly
        self.assert_element('form div label[for="name"]')
        self.assert_text("Name", 'form div label[for="name"]')
        self.assert_element("form div #name")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the password2 element loads correctly
        self.assert_element('form div label[for="password2"]')
        self.assert_text("Confirm Password", 'form div label[for="password2"]')
        self.assert_element("form div #password2")
        # test if the register button loads correctly
        self.assert_element('form div input[type="submit"]')