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
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click enter button
        self.click('input[type="submit"]')
        
        # test if the page that loads is the home page and that it has the user's account balance
        self.click("a[href='/logout']")

        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        self.assert_element("form")
        self.assert_element('form label[for="email"]')
        self.assert_text("Email", 'form label[for="email"]')
        self.assert_element("form #email")
        self.assert_element('form label[for="password"]')
        self.assert_text("Password", 'form label[for="password"]')
        self.assert_element("form #password")
        self.assert_element("form #btn-submit")

        self.open(base_url + '/')

        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        self.assert_element("form")
        self.assert_element('form label[for="email"]')
        self.assert_text("Email", 'form label[for="email"]')
        self.assert_element("form #email")
        self.assert_element('form label[for="password"]')
        self.assert_text("Password", 'form label[for="password"]')
        self.assert_element("form #password")
        self.assert_element("form #btn-submit")
        self.open(base_url+'/logout')

 

