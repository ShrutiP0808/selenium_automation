
import time
import unittest
from locators.signup import SIGNED_USERNAME_LOCATOR, SIGN_UP_FIRST_ERROR_LOCATOR, \
                            SIGN_UP_SECOND_ERROR_LOCATOR, SIGN_UP_THIRD_ERROR_LOCATOR, SIGN_UP_FORTH_ERROR_LOCATOR
from library.common import get_chrome_webdriver, get_random_email
from library.signup import sign_up_user

class TestSignUp(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = get_chrome_webdriver()
        
        URL="http://automationpractice.com/index.php"

        self.driver.maximize_window()
        self.driver.get(URL)

    def test_signup_success(self):

        sign_up_user(driver=self.driver, email_id=get_random_email(), gender="M", first_name="SHRUTI", last_name="PATHAK",
                    password="PKR@PKR", company="CENTIME", address="Test 81/1,2nd cross", city="PUNE", state="4",
                    postcode="51838", country="United States", phone_number="234567890")

        time.sleep(2)

        user_text=self.driver.find_element(*SIGNED_USERNAME_LOCATOR).text

        self.assertEqual("SHRUTI PATHAK", user_text)
    
    def test_signup_failure_without_first_name_and_last_name(self):
        
        sign_up_user(driver=self.driver, email_id=get_random_email(), gender="M",
                    password="PKR@PKR", company="CENTIME", address="Test 81/1,2nd cross", city="PUNE", state="4",
                    postcode="51838", country="United States", phone_number="234567890")

        time.sleep(4)

        last_name_error=self.driver.find_element(*SIGN_UP_FIRST_ERROR_LOCATOR).text
        first_name_error=self.driver.find_element(*SIGN_UP_SECOND_ERROR_LOCATOR).text

        self.assertEqual("firstname is required.", first_name_error)
        self.assertEqual("lastname is required.", last_name_error)

    def test_signup_failure_without_password(self):

        sign_up_user(driver=self.driver, email_id=get_random_email(), gender="M", first_name="SHRUTI", last_name="PATHAK",
                    company="CENTIME", address="Test 81/1,2nd cross", city="PUNE", state="4",
                    postcode="51838", country="United States", phone_number="234567890")

        time.sleep(4)

        password_error=self.driver.find_element(*SIGN_UP_FIRST_ERROR_LOCATOR).text

        self.assertEqual("passwd is required.", password_error)

    def test_signup_failure_without_address_information(self):

        sign_up_user(driver=self.driver, email_id=get_random_email(), gender="M", first_name="SHRUTI", last_name="PATHAK",
                    password="PKR@PKR", company="CENTIME", country="United States", phone_number="234567890")

        time.sleep(4)

        address_error=self.driver.find_element(*SIGN_UP_FIRST_ERROR_LOCATOR).text
        city_error=self.driver.find_element(*SIGN_UP_SECOND_ERROR_LOCATOR).text
        zip_code_error=self.driver.find_element(*SIGN_UP_THIRD_ERROR_LOCATOR).text
        country_error=self.driver.find_element(*SIGN_UP_FORTH_ERROR_LOCATOR).text

        self.assertEqual("address1 is required.", address_error)
        self.assertEqual("city is required.", city_error)
        self.assertEqual("The Zip/Postal code you've entered is invalid. It must follow this format: 00000", zip_code_error)
        self.assertEqual("This country requires you to choose a State.", country_error)
    
    def test_signup_failure_without_phone_number(self):
        sign_up_user(driver=self.driver, email_id=get_random_email(), gender="M", first_name="SHRUTI", last_name="PATHAK",
                    password="PKR@PKR", company="CENTIME", address="Test 81/1,2nd cross", city="PUNE", state="4",
                    postcode="51838", country="United States")

        time.sleep(4)

        phone_error=self.driver.find_element(*SIGN_UP_FIRST_ERROR_LOCATOR).text

        self.assertEqual("You must register at least one phone number.", phone_error)

