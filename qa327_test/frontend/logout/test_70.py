import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User,Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R7
R7 - If the user logsout, the user can't access the homepage 
without logging in again.
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

    
    def test_logoutRestriction(self, *_):
        """
        If the user logsout, the user can't access the homepage 
        without logging in again.
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

        # Test that if a user accesses the homepage not logged in, is redirected to the login page
        # by looking for the Log In heading and the form
        self.assert_element("h1")
        self.assert_text("Log In", "h1")

        # Looking for the form
        self.assert_element("form")

        # Looking for the email field
        self.assert_element('form label[for="email"]')
        self.assert_text("Email", 'form label[for="email"]')
        self.assert_element("form #email")

         # Looking for the password field
        self.assert_element('form label[for="password"]')
        self.assert_text("Password", 'form label[for="password"]')
        self.assert_element("form #password")

        # Looking for the submit button
        self.assert_element("form #btn-submit")

        # Try to open the homepage
        self.open(base_url + '/')

        # Test that if a user accesses the homepage not logged in, is redirected to the login page
        # by looking for the Log In heading and the form
        self.assert_element("h1")
        self.assert_text("Log In", "h1")

        # Looking for the form
        self.assert_element("form")

        # Looking for the email field
        self.assert_element('form label[for="email"]')
        self.assert_text("Email", 'form label[for="email"]')
        self.assert_element("form #email")
        
         # Looking for the password field
        self.assert_element('form label[for="password"]')
        self.assert_text("Password", 'form label[for="password"]')
        self.assert_element("form #password")

        # Looking for the submit button
        self.assert_element("form #btn-submit")

 

