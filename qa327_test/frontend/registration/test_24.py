import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R2.4.
R2.4 - The registration form can be submitted as a POST request to the current URL (/register)
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

class FrontEndRegistrationR4(BaseCase):

    @patch('qa327.backend.register_user', return_value=test_user)
    def test_submitSuccessful(self, *_):
        """
        This function tests that the /register POST request works properly
        when the registration form is submitted successfully (with valid 
        information)
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
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

    def test_submitUnsuccessful(self, *_):
        """
        This function tests that the /register POST request works properly
        when the registration form is submitted unsuccessfully (with invalid 
        information)
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "")
        self.type("#name", test_user.name)
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
        self.assert_text("Email format is incorrect", "#message")
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