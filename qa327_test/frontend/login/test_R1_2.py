import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

"""
This file defines all requirement tests for R1.2
R1.2 - Login page has a default message that says please login
"""

class FrontEndLoginR1(BaseCase):

    def test_loginMessageCheck(self, *_):
        """
        This function tests that the /login page has a default message 
        which says 'Please login'
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # make sure the page is /login
        self.assert_element("#header")
        self.assert_text("Log In", "#header")
        # check that the message is displayed 
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

