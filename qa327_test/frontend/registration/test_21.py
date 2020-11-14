import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R2.1.
R2.1 - If the user has logged in, redirect back to the user profile page /
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
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

class FrontEndRegistrationR1(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_loggedIn(self, *_):
        """
        This function tests that if the user is logged in and try to
        go to the register page, they are redirected to the home page
        """
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", generate_password_hash('test_frontend'))
        # click enter button
        self.click('input[type="submit"]')
            
        # open register page
        self.open(base_url + '/register')
        # test if the page that loads is the home page and that it loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome test_frontend", "#welcome-header")
        self.assert_element("#tickets div h4")
        self.assert_text("test_ticket_yo test_frontend@test.com", "#tickets div h4")
        self.assert_element("#tickets div h5")
        self.assert_text("Quantity: 10 Price: 10", "#tickets div h5")