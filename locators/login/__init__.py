from selenium.webdriver.common.by import By

LOGIN_IN_BUTTON_LOCATOR = (By.LINK_TEXT, "Sign in")
LOGIN_EMAIL_LOCATOR = (By.CSS_SELECTOR, "label[for='email'] + input")
LOGIN_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#passwd")
LOGIN_SUBMIT_LOCATOR = (By.CSS_SELECTOR, "#SubmitLogin")
LOGGED_IN_USER_LOCATOR = (By.CSS_SELECTOR, ".account")
LOGIN_IN_FIRST_ERROR_LOCATOR = (By.XPATH, "//*[@class='alert alert-danger']/ol/li[1]")
