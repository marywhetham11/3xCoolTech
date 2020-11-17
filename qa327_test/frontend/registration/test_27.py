import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R2.7.
R2.7 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

class FrontEndRegistrationR7(BaseCase):

    def test_userNameEmpty(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the name input box is empty
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", "") # name: empty
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
        self.assert_text("User name format is incorrect: Cannot be empty", "#message")
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

    def test_userNameNonAlphanumeric(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the name entered is not alphanumeric
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", "test_name^") # name: non-alphanumeric
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
        self.assert_text("User name format is incorrect: Must be alphanumeric", "#message")
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

    def test_userNameFirstCharSpace(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the name entered starts with a space as the first character
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", " test_name") # name: space as first character
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
        self.assert_text("User name format is incorrect: Cannot have space as first character", "#message")
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

    def test_userNameLastCharSpace(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the name entered ends with a space as the last character
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", "test_name ") # name: space as last character
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
        self.assert_text("User name format is incorrect: Cannot have space as last character", "#message")
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