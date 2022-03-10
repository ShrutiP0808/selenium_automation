from locators.login import LOGIN_IN_BUTTON_LOCATOR, LOGIN_EMAIL_LOCATOR, LOGIN_PASSWORD_LOCATOR, LOGIN_SUBMIT_LOCATOR

def login_user(driver, email=None, password=None):
    # Click on Sign in
    driver.find_element(*LOGIN_IN_BUTTON_LOCATOR).click()
    
    if email:
        driver.find_element(*LOGIN_EMAIL_LOCATOR).send_keys(email)

    if password:
        driver.find_element(*LOGIN_PASSWORD_LOCATOR).send_keys(password)

    driver.find_element(*LOGIN_SUBMIT_LOCATOR).click()