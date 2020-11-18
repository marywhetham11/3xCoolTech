import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all requirement tests for R2.5.
R2.5 - Email, password, password2 all have to satisfy the same required as defined in R1
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

class FrontEndRegistrationR5(BaseCase):

    def test_emailEmpty(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email input box is empty
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "") # email: empty
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Cannot be empty", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_emailLocalTooLong(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because the local is longer than 64 characters
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test_frontend012345678901234567890123456789012345678901234567890123456789@test.com") #email: local is too long
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_emailDomainTooLong(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because the domain is longer than 255 characters
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test_frontend@test012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789.com") #email: domain is too long
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_emailPeriodFirstChar(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because a period is the first character in the local
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", ".test_frontend@test.com") #email: period is first character of local
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')  

    def test_emailPeriodLastChar(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because a period is the last character in the local
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test_frontend.@test.com") #email: period is last character of local
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')  

    def test_emailConsecutivePeriods(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because it contains consecutive periods in the local
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test...frontend@test.com") #email: consecutive periods in local
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')  

    def test_emailHypenFirstChar(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because a hypen cannot be the first character in the domain
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test_frontend@-test.com") #email: hypen is first character of domain
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')  

    def test_emailHypenLastChar(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because a hypen cannot be the last character in the domain
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test_frontend@test.com-") #email: hypen is last character of domain
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]') 

    def test_emailMultipleAtSymbols(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because it cannot contain multiple @ symbols
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test@frontend@test.com") #email: multple @ symbols
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]') 

    def test_emailSpecialCharDomain(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because it cannot contain special characters in the domain
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test_frontend@test#.com") #email: special character in domain
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_emailNonPrintableChar(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the email entered does not follow addr-spec defined in RFC 5322
        because it cannot contain non-printable characters
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", "test_\"frontend\"@test.com") #email: contains non-printable characters
        self.type("#name", test_user.name)
        self.type("#password", test_user.password)
        self.type("#password2", test_user.password)
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Email format is incorrect: Not a valid email", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_passwordEmpty(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the password input box is empty
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", "") # password: empty
        self.type("#password2", "")
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Password format is incorrect: Cannot be empty", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_passwordTooShort(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the password entered is less than 6 characters
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", "Test@") # password: too short
        self.type("#password2", "Test@")
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Password format is incorrect: Cannot be less than 6 characters", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_passwordNoUppercase(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the password entered has no uppercase letter
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", "test_password@") # password: no uppercase letter
        self.type("#password2", "test_password@")
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Password format is incorrect: Does not contain an uppercase character", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_passwordNoLowercase(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the password entered has no lowercase letter
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", "TEST_PASSWORD@") # password: no lowercase letter
        self.type("#password2", "TEST_PASSWORD@")
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Password format is incorrect: Does not contain a lowercase character", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')

    def test_passwordNoSpecialCharacter(self, *_):
        """
        This function tests that the user registration fails and an error message
        is returned if the password entered has no special character
        """
        # open logout page
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')
        # fill email, user name and password
        self.type("#email", test_user.email)
        self.type("#name", test_user.name)
        self.type("#password", "Testpassword") # password: no special characters
        self.type("#password2", "Testpassword")
        # click enter button
        self.click('input[type="submit"]')

        # test if the login page loads correctly
        # test if the login title loads correctly
        self.assert_element("h1")
        self.assert_text("Log In", "h1")
        # test if the error message loads correctly
        self.assert_element("#message")
        self.assert_text("Password format is incorrect: Does not contain a special character", "#message")
        # test if the login form loads correctly
        self.assert_element("form")
        # test if the email element loads correctly
        self.assert_element('form div label[for="email"]')
        self.assert_text("Email", 'form div label[for="email"]')
        self.assert_element("form div #email")
        # test if the password element loads correctly
        self.assert_element('form div label[for="password"]')
        self.assert_text("Password", 'form div label[for="password"]')
        self.assert_element("form div #password")
        # test if the login button loads correctly
        self.assert_element('form div input[type="submit"]')