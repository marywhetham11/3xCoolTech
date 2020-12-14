import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R4.3
R4.3 -  The quantity of the tickets has to be more than 0, and less than or equal to 100
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)


class BackendSellR4(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_sellQuantityBelow(self, *_):
        """
        This function tests that the user cannot submit a ticket
        with a quantity below 1
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter users email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # check we are in the homepage and login is successful
        self.assert_element("#sell_form")
        # enter the ticket information
        # enter valid name
        self.assert_element("#sell_form form div label[for='name']")
        self.type("#sell_form form div #name", "testName")
        # enter invalid ticket quantity - below 1
        self.assert_element("#sell_form form div label[for='quantity']")
        self.type("#sell_form form div #quantity", "0")
        # enter valid ticket price
        self.assert_element("#sell_form form div label[for='price']")
        self.type("#sell_form form div #price", "10")
        # enter valid ticket date
        self.assert_element("#sell_form form div label[for='date']")
        self.type("#sell_form form div #date", "20201214")
        # submit the form
        self.click("#sell_form form div input[type='submit']")

        # test that the post was unsuccesfull
        self.assert_element("#message")
        self.assert_text("Quantity format is incorrect: Cannot be less than or equal to 0","#message")

        # cleanup 
        self.open(base_url + '/logout')


    @patch('qa327.backend.login_user', return_value=test_user)
    def test_sellQuantityAbove(self, *_):
        """
        This function tests that the user cannot submit a ticket
        with a quantity above 100
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter users email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # check we are in the homepage and login is successful
        self.assert_element("#sell_form")
        # enter the ticket information
        # enter valid name
        self.assert_element("#sell_form form div label[for='name']")
        self.type("#sell_form form div #name", "testName")
        # enter invalid ticket quantity - above 100
        self.assert_element("#sell_form form div label[for='quantity']")
        self.type("#sell_form form div #quantity", "101")
        # enter valid ticket price
        self.assert_element("#sell_form form div label[for='price']")
        self.type("#sell_form form div #price", "10")
        # enter valid ticket date
        self.assert_element("#sell_form form div label[for='date']")
        self.type("#sell_form form div #date", "20201214")
        # submit the form
        self.click("#sell_form form div input[type='submit']")

        # test that the post was unsuccesfull
        self.assert_element("#message")
        self.assert_text("Quantity format is incorrect: Cannot be greater than 100","#message")

        # cleanup 
        self.open(base_url + '/logout')
