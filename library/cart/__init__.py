from locators.cart import ADD_TO_CART_LOCATOR, ADDED_PRODUCT_LAYER_CLOSE_BUTTON_LOCATOR, CART_LOCATOR, \
                          DELETE_PRODUCT_FROM_CART_LOCATOR, MENU_LOCATOR, PRODUCT_TITLE_LOCATOR, SECOND_PRODUCT_LOCATOR
from selenium.webdriver.common.action_chains import ActionChains


def add_to_cart(driver):
    driver.find_element(*MENU_LOCATOR).click()
    
    driver.implicitly_wait(50)

    product_title = driver.find_element(*PRODUCT_TITLE_LOCATOR).text

    driver.find_element(*SECOND_PRODUCT_LOCATOR).click()
    driver.implicitly_wait(50)

    driver.find_element(*ADD_TO_CART_LOCATOR).click()

    return product_title

def delete_from_cart(driver):
    driver.find_element(*ADDED_PRODUCT_LAYER_CLOSE_BUTTON_LOCATOR).click()

    hover = ActionChains(driver)
    hover.move_to_element(driver.find_element(*CART_LOCATOR)).perform()
        
    driver.implicitly_wait(50)

    driver.find_element(*DELETE_PRODUCT_FROM_CART_LOCATOR).click()