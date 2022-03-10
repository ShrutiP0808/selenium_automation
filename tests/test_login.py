import random
import string
import unittest
from library.common import get_chrome_webdriver
from library.login import login_user
from locators.login import LOGGED_IN_USER_LOCATOR, LOGIN_IN_FIRST_ERROR_LOCATOR

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = get_chrome_webdriver()
        
        URL="http://automationpractice.com/index.php"

        self.driver.maximize_window()
        self.driver.get(URL)

        self.email = "VnEDjTK@gmail.com"
        self.password = "PKR@PKR"

    def test_login_success(self):
        login_user(self.driver, email=self.email, password=self.password)

        self.driver.implicitly_wait(5)

        user_name = self.driver.find_element(*LOGGED_IN_USER_LOCATOR).text

        self.assertEqual("SHRUTI PATHAK", user_name)
    
    def test_login_failure_with_missing_email(self):
        login_user(self.driver, password=self.password)

        self.driver.implicitly_wait(5)

        email_error=self.driver.find_element(*LOGIN_IN_FIRST_ERROR_LOCATOR).text

        self.assertEqual("An email address required.", email_error)
    
    def test_login_failure_with_missing_password(self):
        login_user(self.driver, email=self.email)

        self.driver.implicitly_wait(5)

        password_error=self.driver.find_element(*LOGIN_IN_FIRST_ERROR_LOCATOR).text

        self.assertEqual("Password is required.", password_error)
    
    def test_login_failure_with_invalid_email(self):
        login_user(self.driver, email="invalid_email", password=self.password)

        self.driver.implicitly_wait(5)

        email_error=self.driver.find_element(*LOGIN_IN_FIRST_ERROR_LOCATOR).text

        self.assertEqual("Invalid email address.", email_error)
    
    def test_login_failure_with_invalid_password(self):
        login_user(self.driver, email=self.email, password="invalid_password")

        self.driver.implicitly_wait(5)

        email_error=self.driver.find_element(*LOGIN_IN_FIRST_ERROR_LOCATOR).text

        self.assertEqual("Authentication failed.", email_error)
