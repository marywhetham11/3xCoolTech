import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R1.7
R1.7 - Email has to follow addr-spec defined in RFC 5322
"""

class FrontEndLoginR1(BaseCase):

    def test_emailFormCorrect(self, *_):
        """
        This function tests that if all conditions of the email form are met
        the email may be subbmitted 
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter a valid email
        self.type("#email", "test@test.com")
        # enter a valid password
        self.type("#password", "P@ssw0rd")
        # click enter
        self.click('input[type="submit"]')
        # Check that the error message displays correctly
        self.assert_element("#message")
        self.assert_text("email/password combination incorrect", "#message")

    def test_emailFormCheck2ATs(self, *_):
        """
        This function tests the condition of the email form that
        only one @ symbol may be present in the email
        and theat the correct warning message is displayed
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
        and theat the correct warning message is displayed
        """
        # open /logout to ensure no logged in user
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter an invalid email with special characters
        self.type("#email", "t&$%t@domain.ext")
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
        and theat the correct warning message is displayed
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

    def test_emailFormCheckLessThan64(self, *_):
        """
        This function tests the condition of the email form that
        the email may not be longer than 64 characters
        and theat the correct warning message is displayed
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
        and theat the correct warning message is displayed
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