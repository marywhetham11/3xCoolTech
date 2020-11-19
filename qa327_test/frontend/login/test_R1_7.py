import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.7
R1.7 - Email has to follow addr-spec defined in RFC 5322
"""

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='test_user',
    password=generate_password_hash('test_password')
)

class FrontEndLoginR1(BaseCase):

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_emailFormCorrect(self, *_):
        """
        This function tests that if all conditions of the email form are met
        the email may be subbmitted and the page redirects
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter a valid email
        self.type("#email", test_user.email)
        # enter a valid password
        self.type("#password", test_user.password)
        # click enter
        self.click('input[type="submit"]')
        # check the current page has redirected
        self.assert_element("#welcome-header")
        self.assert_text("Welcome ", "#welcome-header")

    def test_emailFormCheck2ATs(self, *_):
        """
        This function tests the condition of the email form that
        only one @ symbol may be present in the email
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with 2 @ symbols
        self.type("#email", "test@test@domain.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")

    def test_emailFormCheckNoSpecial(self, *_):
        """
        This function tests the condition of the email form that
        no special character may be present
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with special characters
        self.type("#email", "t^|$]t@domain.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")

    def test_emailFormCheckNoQuotation(self, *_):
        """
        This function tests the condition of the email form that
        no quotation marks may be present
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with quotation marks
        self.type("#email", "t\"es\"t@domain.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")

    def test_emailFormCheckLessThan255(self, *_):
        """
        This function tests the condition of the email form that
        the email domain may not be longer than 255 characters
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with more than 255 characters in domain
        self.type("#email", "test@domainOfLenghtGreaterThan255000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")

        
    def test_emailFormCheckLessThan64(self, *_):
        """
        This function tests the condition of the email form that
        the email address may not be longer than 64 characters
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with more than 64 characters
        self.type("#email", "thisLocalIsOfLenghtGreaterThanSistyFourCharactersWhichIsCompletlyIlligal@domain.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")


    def test_emailFormCheckUnderscore(self, *_):
        """
        This function tests the condition of the email form that
        no underscore may be present in the domain
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with underscore in the domain
        self.type("#email", "test@domain_place.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")


    def test_emailFormFirstCharacterPeriod(self, *_):
        """
        This function tests the condition of the email form that
        no period may be the first character
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with period as first char
        self.type("#email", ".test@domain.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")


    def test_emailFormLastCharacterPeriod(self, *_):
        """
        This function tests the condition of the email form that
        last char of the local may not be a period
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with period as last char of local
        self.type("#email", "test.@domain.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")


    def test_emailFormTwoPeriodsLocal(self, *_):
        """
        This function tests the condition of the email form that
        the local may not have two periods in a row
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with two periods in a row in the local
        self.type("#email", "loc..al@domain.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")


    def test_emailFormNoSpecialCharDomian(self, *_):
        """
        This function tests the condition of the email form that
        the domain may not contain any special characters
        and that the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with special character in the domain
        self.type("#email", "local@d+m@|n.ext")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("Email format incorrect: Not a valid email", "#message")