import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
import qa327.backend as bn
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines an integration test for a example user signing up for the 
service, then posting a ticket to the site. Use the browser.
"""

# Mock a sample user for 
test_user = User(
    email='test_integration@test.com',
    name='test_integration',
    password=generate_password_hash('test_integration')
)

test_ticket = Ticket(
    owner='test_integration@test.com',
    name='integrationTicket',
    quantity=10,
    price=10,
    date='00001122'
)

@pytest.mark.usefixtures('server')
class integrationTestSignupPost(BaseCase):

    def test_register(self):
        """
        This tests that the user register as a new user
        """
        # first check that the user does not exsist 
        if(bn.get_user(test_user.email)):
            bn.delete_user(test_user.email)

        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # check that the user is redirected to the login page
        self.assert_element("h1")
        self.assert_text("Log In", "h1")

    def test_login(self):
        """
        This tests that the user can log in
        """
        self.open(base_url + '/login')
        # check that the user is in the login page
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # enter users email and password
        self.type("#email", test_user.email)
        self.type("#password", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # check we are in the homepage and login is successful
        self.assert_element("#welcome-header")
        self.assert_text("Welcome " + test_user.name, "#welcome-header")


    def test_integration(self):
        """
        This tests that the user can sign up, log in, and sell
        """
        # preform the full test
        self.test_register()
        self.test_login()
        
        # now test to sell a ticket
        self.open(base_url + '/')
        self.assert_element("#sell_form")

        # check that the ticket does not exsist
        if(bn.get_ticket(test_ticket.name)):
            bn.delete_ticket(test_ticket.name)

        # enter the ticket information
        # ticket name
        self.assert_element("#sell_form form div label[for='name']")
        self.type("#sell_form form div #name", test_ticket.name)
        # ticket quantity
        self.assert_element("#sell_form form div label[for='quantity']")
        self.type("#sell_form form div #quantity", str(test_ticket.quantity))
        # ticket price
        self.assert_element("#sell_form form div label[for='price']")
        self.type("#sell_form form div #price", str(test_ticket.price))
        # ticket date
        self.assert_element("#sell_form form div label[for='date']")
        self.type("#sell_form form div #date", test_ticket.date)
        # submit the form
        self.click("#sell_form form div input[type='submit']")

        # test that the post was succesfull
        self.assert_element("#message")
        self.assert_text("Sell Successful","#message")

        # cleanup 
        self.open(base_url + '/logout')
        