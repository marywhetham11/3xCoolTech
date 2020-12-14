import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.models import db, User, Ticket
from unittest.mock import patch
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R4
R4 - The postive case for login is tested
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)

# mock the ticket
test_ticket = Ticket(
    owner='test@test.com',
    name='testTicket',
    quantity=10,
    price=10,
    date='20201214'
)

class BackendSellR4(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.sell_ticket', return_value=test_ticket)
    def test_sellPositive(self, *_):
        """
        This function tests that the user can submit a ticket to sell
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
        # ticket name
        self.assert_element("#sell_form form div label[for='name']")
        self.type("#sell_form form div #name", test_ticket.name)
        # ticket quantity
        self.assert_element("#sell_form form div label[for='quantity']")
        self.type("#sell_form form div #quantity", str(test_ticket.quantity))
        # ticket price
        self.assert_element("#sell_form form div label[for='price']")
        self.type("#sell_form form div #price", str(test_ticket.price))
        # ticket date
        self.assert_element("#sell_form form div label[for='date']")
        self.type("#sell_form form div #date", test_ticket.date)
        # submit the form
        self.click("#sell_form form div input[type='submit']")

        # test that the post was succesfull
        self.assert_element("#message")
        self.assert_text("Sell Successful","#message")

        # cleanup 
        self.open(base_url + '/logout')
