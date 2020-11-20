import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User,Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R8.
R8 - For any other requests except the ones above, 
the system should return a 404 error
"""

class FrontEndHomepageR3(BaseCase):

    def test_logout(self, *_):
        """
        This function tests that if a page is access that doesn't exist 
        a 404 error page is shown
        """
        # logout to invalidate any logged-in sessions that may exist
        self.open(base_url +'/logout')
        # open a page that does not exist 
        self.open(base_url + '/abc')
        self.assert_element("h1")
        self.assert_text("404 Page Not Found" , "h1")
        

        

 

