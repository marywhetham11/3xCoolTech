import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.5
R1.5 - The login form can be submitted as a POST request to the current URL (/login)
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)


class FrontEndLoginR1(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_loginConfirmPost(self, *_):
        """
        This function tests that the user can summit the forms to the 
        backend using the /login to post
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter users email and password
        self.type("#email", "test@test.com")
        self.type("#password", test_user.password)
        # check if the login button exsists
        self.assert_element('form div input[type="submit"]')
        # click enter button
        self.click('input[type="submit"]')

        # cleanup 
        self.open(base_url + '/logout')
