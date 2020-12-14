import pytest
from seleniumbase import BaseCase
import qa327.backend as bn
from qa327_test.conftest import base_url


# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).

@pytest.mark.usefixtures('server')
class Registered(BaseCase):

    def buy_ticket(self):
        self.type("#buy_form form div #name", "test_ticket")
        self.type("#buy_form form div #quantity", 9)
        self.click("#buy_form form div input[type='submit']")

    def sell_ticket(self):
        if(bn.get_ticket("test_ticket")):
            bn.delete_ticket("test_ticket")
        self.type("#sell_form form div #name", "test_ticket")
        self.type("#sell_form form div #quantity", 10)
        self.type("#sell_form form div #price", 10)
        self.type("#sell_form form div #date", "20200901")
        self.click("#sell_form form div input[type='submit']")
    
    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "hello@gamil.com")
        self.type("#name", "hello")
        self.type("#password", "PassWord1@")
        self.type("#password2", "PassWord1@")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.type("#email", "hello@gamil.com")
        self.type("#password", "PassWord1@")
        self.click('input[type="submit"]')

    def test_purchasing_ticket(self):
        """ This test checks the implemented login/logout feature """
        if (bn.get_user("hello@gamil.com")):
            bn.delete_user("hello@gamil.com")
        
        self.register()
        self.login()
        self.open(base_url)

        # Check if the login and register work
        self.assert_element("#welcome-header")
        self.assert_text("Welcome hello", "#welcome-header")

        self.sell_ticket()

        # Check if the ticket was sold properly 
        self.assert_element("#welcome-header")
        self.assert_text("Welcome hello", "#welcome-header")
        self.assert_element("#message")
        self.assert_text("Sell Successful","#message")

        self.buy_ticket()

        # Check if the ticket was purchased properly 
        self.assert_element("#welcome-header")
        self.assert_text("Welcome hello", "#welcome-header")
        self.assert_element("#message")
        self.assert_text("Buy Successful","#message")
        
        
        