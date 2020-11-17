import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R2.2.
R2.2 - otherwise, show the user registration page
"""

class FrontEndRegistrationR2(BaseCase):

    def test_showRegisterPage(self, *_):
        """
        This function tests that if the user is not logged in, that they are
        brought to the registration page
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # test if the registration page loads correctly
        self.assert_element("h1")
        self.assert_text("Register", "h1")
        self.assert_element("form")