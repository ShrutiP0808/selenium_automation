import time
import random
import string
import unittest
from library.common import get_chrome_webdriver
from library.login import login_user
from library.cart import add_to_cart, delete_from_cart
from locators.cart import ADDED_PRODUCT_TITLE_LAYER_LOCATOR, CART_DETAIL_LOCATOR


class TestCart(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = get_chrome_webdriver()
        
        URL="http://automationpractice.com/index.php"

        self.driver.maximize_window()
        self.driver.get(URL)

        self.email = "VnEDjTK@gmail.com"
        self.password = "PKR@PKR"
        login_user(driver=self.driver, email=self.email, password=self.password)
    
    def test_add_to_cart(self):

        product_title = add_to_cart(driver=self.driver)

        time.sleep(3)

        expected_product_title = self.driver.find_element(*ADDED_PRODUCT_TITLE_LAYER_LOCATOR).text

        self.assertEqual(product_title, expected_product_title)

    def test_delete_from_cart(self):
        product_title = add_to_cart(driver=self.driver)

        time.sleep(3)

        expected_product_title = self.driver.find_element(*ADDED_PRODUCT_TITLE_LAYER_LOCATOR).text

        self.assertEqual(product_title, expected_product_title)

        delete_from_cart(driver=self.driver)

        time.sleep(3)

        empty_cart_text = self.driver.find_element(*CART_DETAIL_LOCATOR).text

        self.assertEqual("(empty)", empty_cart_text)
