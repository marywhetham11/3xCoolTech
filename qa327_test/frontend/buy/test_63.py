import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R6.3.
R6.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100.
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

class FrontEndBuyR6(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_quantity0(self, *_):
        """
        This function tests that if the user enters a ticket quantity that is
        equal to 0 into the buy form, then an error message should be displayed
        on the homepage
        """
        # logout to invalidate any logged-in sessions that may exist
        self.open(base_url +'/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click submit button
        self.click('input[type="submit"]')
        
        # test if the page that loads is the home page and that it has the user's 
        # name as the header
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if account balance is displayed correctly
        self.assert_element("#user_balance")
        self.assert_text("Balance: " + str(test_account_balance.balance), "#user_balance")
        # test if the tickets are displayed correctly
        self.assert_element("#tickets div h4")
        self.assert_text(test_tickets[0].name + " " + test_tickets[0].owner, "#tickets div h4")
        self.assert_element("#tickets div h5")
        self.assert_text("Quantity: " + str(test_tickets[0].quantity) + " Price: " + str(test_tickets[0].price), "#tickets div h5")

        # type the name and quantity wanted into the buy form
        self.type("#buy_form form div #name", test_tickets[0].name)
        self.type("#buy_form form div #quantity", "0") # error: quantity is 0
        # click submit button
        self.click('#buy_form form div input[type="submit"]')

        # test if the page that loads is the home page and that it has the user's 
        # name as the header
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if account balance is displayed correctly
        self.assert_element("#user_balance")
        self.assert_text("Balance: " + str(test_account_balance.balance), "#user_balance")
        
        # test if the error message is displayed
        self.assert_element("#message")
        self.assert_text("Quantity format is incorrect: Cannot be less than or equal to 0", "#message")

        # logout
        self.open(base_url +'/logout')

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_quantityLessThan0(self, *_):
        """
        This function tests that if the user enters a ticket quantity that is
        less than 0 into the buy form, then an error message should be displayed
        on the homepage
        """
        # logout to invalidate any logged-in sessions that may exist
        self.open(base_url +'/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click submit button
        self.click('input[type="submit"]')
        
        # test if the page that loads is the home page and that it has the user's 
        # name as the header
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if account balance is displayed correctly
        self.assert_element("#user_balance")
        self.assert_text("Balance: " + str(test_account_balance.balance), "#user_balance")
        # test if the tickets are displayed correctly
        self.assert_element("#tickets div h4")
        self.assert_text(test_tickets[0].name + " " + test_tickets[0].owner, "#tickets div h4")
        self.assert_element("#tickets div h5")
        self.assert_text("Quantity: " + str(test_tickets[0].quantity) + " Price: " + str(test_tickets[0].price), "#tickets div h5")

        # type the name and quantity wanted into the buy form
        self.type("#buy_form form div #name", test_tickets[0].name)
        self.type("#buy_form form div #quantity", "-1") # error: quantity is less than 0
        # click submit button
        self.click('#buy_form form div input[type="submit"]')

        # test if the page that loads is the home page and that it has the user's 
        # name as the header
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if account balance is displayed correctly
        self.assert_element("#user_balance")
        self.assert_text("Balance: " + str(test_account_balance.balance), "#user_balance")
        
        # test if the error message is displayed
        self.assert_element("#message")
        self.assert_text("Quantity format is incorrect: Cannot be less than or equal to 0", "#message")

        # logout
        self.open(base_url +'/logout')

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_quantityGreaterThan100(self, *_):
        """
        This function tests that if the user enters a ticket quantity that is
        greater than 100 into the buy form, then an error message should be 
        displayed on the homepage
        """
        # logout to invalidate any logged-in sessions that may exist
        self.open(base_url +'/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click submit button
        self.click('input[type="submit"]')
        
        # test if the page that loads is the home page and that it has the user's 
        # name as the header
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if account balance is displayed correctly
        self.assert_element("#user_balance")
        self.assert_text("Balance: " + str(test_account_balance.balance), "#user_balance")
        # test if the tickets are displayed correctly
        self.assert_element("#tickets div h4")
        self.assert_text(test_tickets[0].name + " " + test_tickets[0].owner, "#tickets div h4")
        self.assert_element("#tickets div h5")
        self.assert_text("Quantity: " + str(test_tickets[0].quantity) + " Price: " + str(test_tickets[0].price), "#tickets div h5")

        # type the name and quantity wanted into the buy form
        self.type("#buy_form form div #name", test_tickets[0].name)
        self.type("#buy_form form div #quantity", "101") # error: quantity is greater than 100
        # click submit button
        self.click('#buy_form form div input[type="submit"]')

        # test if the page that loads is the home page and that it has the user's 
        # name as the header
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if account balance is displayed correctly
        self.assert_element("#user_balance")
        self.assert_text("Balance: " + str(test_account_balance.balance), "#user_balance")
        
        # test if the error message is displayed
        self.assert_element("#message")
        self.assert_text("Quantity format is incorrect: Cannot be greater than 100", "#message")

        # logout
        self.open(base_url +'/logout')