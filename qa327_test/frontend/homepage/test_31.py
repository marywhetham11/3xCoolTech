import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


"""
This file defines all requirement tests for R3.1.
R3.1 - If the user is not logged in, redirect to login page
"""

class FrontEndHomepageR3(BaseCase):

    def test_redirectLoginPage(self, *_):
        """
        This function tests that if the user is not logged in they are redirected 
        to the login page
        """
        # logout to invalidate any logged-in sessions that may exist
        self.open(base_url +'/logout')
        # open login page
        self.open(base_url + '/')
        
        # Test that if a user accesses the homepage not logged in, is redirected to the login page
        # by looking for the Log In heading and the form
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