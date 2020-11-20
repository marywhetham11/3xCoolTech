import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User,Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R3.7.
R3.7 - The homepage has a form for buying tickets 
with fields name, quantity
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

class FrontEndHomepageR3(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_buyForm(self, *_):
        """
        This function tests that if the user is logged in and is on the homepage,
        there is a form for buying tickets with fields name, quantity
        """
        # logout to invalidate any logged-in sessions that may exist
        self.open(base_url +'/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click enter button
        self.click('input[type="submit"]')
        
        # test if the page that loads is the home page and that it has 
        # a form that has the id "buy_form" and has the fields name, quantity
        self.assert_element("#buy_form")
        self.assert_element("#buy_form label[for='name']")
        self.assert_text('Name',"#buy_form label[for='name']")
        self.assert_element("#buy_form label[for='quantity']")
        self.assert_text('Quantity',"#buy_form label[for='quantity']")
        self.open(base_url +'/logout')