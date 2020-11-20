import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User,Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R3.5.
R3.5 - If the user is logged in, all availible tickets on the 
homepage
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
    def test_checkShownTickets(self, *_):
        """
        This function tests that if the user is logged in and they are on the 
        homepage, all of the avalible tickets are shown on the screen
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
        
        # test if the page that available tickets are shown on the homepage

        # look for tickets div
        self.assert_element("#tickets")

        # test if the ticket's quantity is there
        self.assert_element("#tickets div h5 #ticket_quantity")
        self.assert_text(test_tickets[0].quantity, "#tickets div h5 #ticket_quantity")

        # test if the ticket's email is there
        self.assert_element("#tickets div h4 #ticket_email")
        self.assert_text(test_tickets[0].owner, "#tickets div h4 #ticket_email")

        # test if the ticket's price is there
        self.assert_element("#tickets div h5 #ticket_price")
        self.assert_text(test_tickets[0].price, "#tickets div h5 #ticket_price")


        self.open(base_url +'/logout')