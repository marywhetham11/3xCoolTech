import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R5.0.
R5.0 - Successfully update of a ticket
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

# Mock the updated ticket
updated_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=20,
    price=10.01,
    date='20200902'
)

class FrontEndUpdateR0(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_account_balance', return_value=test_account_balance)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.update_ticket', return_value=updated_ticket)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticketSuccess(self, *_):
        """
        This function tests that if the user is logged in and try to
        go to the register page, they are redirected to the home page
        """
        # open logout page
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click enter button
        self.click('input[type="submit"]')
            
        # test if the page that loads is the home page and that it loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if the tickets show up
        self.assert_element("#tickets div h4")
        self.assert_text(test_tickets[0].name + " " + test_tickets[0].owner, "#tickets div h4")
        self.assert_element("#tickets div h5")
        self.assert_text("Quantity: " + str(test_tickets[0].quantity) + " Price: " + str(test_tickets[0].price), "#tickets div h5")

        # change the test_tickets variable to reflect the updates to the first 
        # ticket, so get_all_tickets will return the updated ticket information
        test_tickets[0].quantity = updated_ticket.quantity
        test_tickets[0].price = updated_ticket.price
        test_tickets[0].date = updated_ticket.date

        # fill in name, quantity, price and date in the update form
        self.type("#update_form form div #name", updated_ticket.name)
        self.type("#update_form form div #quantity", int(test_tickets[0].quantity))
        self.type("#update_form form div #price", float(test_tickets[0].price))
        self.type("#update_form form div #date", updated_ticket.date)
        self.click('#update_form form div input[type="submit"]')

        # test if the page that loads is the home page and that it loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")
        # test if the tickets show up
        self.assert_element("#tickets div h4")
        self.assert_text(test_tickets[0].name + " " + test_tickets[0].owner, "#tickets div h4")
        self.assert_element("#tickets div h5")
        self.assert_text("Quantity: " + str(test_tickets[0].quantity) + " Price: " + str(test_tickets[0].price), "#tickets div h5")

        # logout
        self.open(base_url + '/logout')