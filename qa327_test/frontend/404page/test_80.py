import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User,Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R3.1.
R3.1 - If the user is not logged in, redirect to login page
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
    @patch('qa327.backend.sell_ticket', return_value=test_user)
    def test_checkShownTickets(self, *_):
        """
        This function tests that if the user is not logged in they are redirected 
        to the login page
        """
        # logout to invalidate any logged-in sessions that may exist
        self.open(base_url +'/logout')
        # open a page that does not exist 
        self.open(base_url + '/abc')
        self.assert_element("h1")
        self.assert_text("404 Page Not Found" , "h1")
        

        

 

