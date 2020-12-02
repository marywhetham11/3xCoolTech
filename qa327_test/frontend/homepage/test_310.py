import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User,Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R3.10.
R3.10 - Buy form posts to /buy
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
    @patch('qa327.backend.set_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.buy_ticket', return_value=test_tickets[0])
    @patch('qa327.backend.get_ticket', return_value=test_tickets[0])
    def test_postBuyForm(self, *_):
        """
        This function tests that the buy form is posted to /buy
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
        
        # submit the test_tickets[0] to the buy form
        # Check for name field and submit test_tickets[0]'s name
        self.assert_element("#buy_form form div label[for='name']")
        self.type("#buy_form form div #name", test_tickets[0].name)

        # Check for quantity field and submit test_tickets[0]'s quantity
        self.assert_element("#buy_form form div label[for='quantity']")
        self.type("#buy_form form div #quantity", test_tickets[0].quantity)

        # Click the submit button
        self.click("#buy_form form div input[type='submit']")

        # test to see if we we redirected to the homepage
        self.assert_element("#welcome-header")

        # see if the post was successful
        self.assert_element("#message")
        self.assert_text("Buy Successful","#message")
        self.open(base_url +'/logout')