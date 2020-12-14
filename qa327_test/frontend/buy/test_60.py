import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R6.0.
R3.0 - A ticket is successfully bought
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
# Mock an updated ticket
updated_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=5,
    price=10,
    date='20200901'
)

class FrontEndBuyR6(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.buy_ticket', return_value=updated_ticket)
    @patch('qa327.backend.set_account_balance', return_value=test_account_balance)
    def test_buySuccessful(self, *_):
        """
        This function tests that if the user can successfully buy a ticket
        through the buy form
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

        # update the ticket quantity and account balance to reflect the changes
        # from buying the ticket
        test_tickets[0].quantity = updated_ticket.quantity
        test_account_balance.balance = test_tickets[0].price * (test_tickets[0].quantity - updated_ticket.quantity) * 1.4

        # type the name and quantity wanted into the buy form
        self.type("#buy_form form div #name", test_tickets[0].name) 
        self.type("#buy_form form div #quantity", (test_tickets[0].quantity - updated_ticket.quantity))
        # click submit button
        self.click('#buy_form form div input[type="submit"]')

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

        # logout
        self.open(base_url +'/logout')