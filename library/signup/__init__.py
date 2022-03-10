import time
from locators.signup import ADDRESS_LOCATOR, CITY_LOCATOR, COMPANY_LOCATOR, COUNTRY_LOCATOR, CUSTOMER_FIRST_NAME_LOCATOR, CUSTOMER_LAST_NAME_LOCATOR, FEMALE_LOCATOR, FIRSTNAME_LOCATOR, LASTNAME_LOCATOR, MALE_LOCATOR, PASSWORD_LOCATOR, PHONE_NUMBER_LOCATOR, POSTCODE_LOCATOR, REGISTER_SUBMIT_BUTTON_LOCATOR, SIGN_IN_BUTTON_LOCATOR, SIGN_UP_EMAIL_LOCATOR, SIGN_UP_SUBMIT_LOCATOR, STATE_LOCATOR
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging

def sign_up_user(driver, email_id, first_name=None, last_name=None, gender=None, 
                                   password=None, company=None, address=None, city=None, 
                                   state=None, postcode=None, country=None, phone_number=None):

        logging.info(f"EmailID: {email_id}")
        # Click on Sign in
        driver.find_element(*SIGN_IN_BUTTON_LOCATOR).click()
        
        # Enter email address
        driver.find_element(*SIGN_UP_EMAIL_LOCATOR).send_keys(email_id)
        
        # Click on "Create an account"
        driver.find_element(*SIGN_UP_SUBMIT_LOCATOR).click()
        
        time.sleep(10)

        if gender == "M":
            driver.find_element(*MALE_LOCATOR).click()
        else:
            driver.find_element(*FEMALE_LOCATOR).click()
        
        if first_name:
            driver.find_element(*CUSTOMER_FIRST_NAME_LOCATOR).send_keys(first_name)
        
        if last_name:
            driver.find_element(*CUSTOMER_LAST_NAME_LOCATOR).send_keys(last_name)
        
        if password:
            driver.find_element(*PASSWORD_LOCATOR).send_keys(password)
        
        driver.find_element(*COMPANY_LOCATOR).send_keys(company)
        
        if address:
            driver.find_element(*ADDRESS_LOCATOR).send_keys(address)
        if city:
            driver.find_element(*CITY_LOCATOR).send_keys(city)
        
        time.sleep(2)

        # Select State
        if state:
            state_dropdown=Select(driver.find_element(*STATE_LOCATOR))
            state_dropdown.select_by_value(state)

        time.sleep(2)

        if postcode:
            driver.find_element(*POSTCODE_LOCATOR).send_keys(postcode)
        
        # Select Country
        countrydropDown=Select(driver.find_element(*COUNTRY_LOCATOR))
        countrydropDown.select_by_visible_text(country)
        
        # Enter Mobile Number
        if phone_number:
            driver.find_element(*PHONE_NUMBER_LOCATOR).send_keys(phone_number)
        
        driver.find_element(by=By.XPATH, value="//input[@name=\"alias\"]").clear()
        driver.find_element(by=By.XPATH, value="//input[@name=\"alias\"]").send_keys("Office")
        driver.find_element(*REGISTER_SUBMIT_BUTTON_LOCATOR).click()
