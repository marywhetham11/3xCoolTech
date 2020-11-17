import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R2.9.
R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

class FrontEndRegistrationR9(BaseCase):

    def test_errorMessage(self, *_):
        """
        This function tests that if the user registration fails and an error 
        message is returned and the user is brought to the login page
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", "") # error: name is empty
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("format is incorrect", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')