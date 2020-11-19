import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

"""
This file defines all requirement tests for R1.1
R1.1 - If the user hasn`t logged in, show the login page
"""

class FrontEndLoginR1(BaseCase):

    def test_notLoggedIn(self, *_):
        """
        This function tests that if the user is not logged in then 
        the /login page is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # make sure the login header is displayed
        self.assert_element("#header")
        self.assert_text("Log In", "#header")
