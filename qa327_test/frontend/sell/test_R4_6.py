import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R4.6
R4.6 -  For any errors, redirect back to / and show an error message
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)

# Mock an account balance
test_account_balance = Account_Balance(
    email='test_frontend@test.com',
    balance=5000.00
)

# Mock a sample ticket
test_tickets = [
    Ticket(
        owner='test_frontend@test.com',
        name='test_ticket_yo',
        quantity=10,
        price=10,
        date='20200901'
    )
]


class FrontendSellR4(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_sellInvalid(self, *_):
        """
        This function tests that upon error the user is directed to 
        the main page and an error message is 
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
        # enter invalid name
        self.assert_element("#sell_form form div label[for='name']")
        self.type("#sell_form form div #name", "b@dName")
        # enter invalid ticket quantity
        self.assert_element("#sell_form form div label[for='quantity']")
        self.type("#sell_form form div #quantity", "10000")
        # enter invalid ticket price
        self.assert_element("#sell_form form div label[for='price']")
        self.type("#sell_form form div #price", "5000000")
        # enter invalid ticket date
        self.assert_element("#sell_form form div label[for='date']")
        self.type("#sell_form form div #date", "20201214")
        # submit the form
        self.click("#sell_form form div input[type='submit']")

        # test that the post was unsuccessful
        # test main page displays with error
        self.assert_element("#welcome-header")
        self.assert_element("#message")
        self.assert_text("Ticket name format is incorrect: Must be alphanumeric","#message")

        # cleanup 
        self.open(base_url + '/logout')
