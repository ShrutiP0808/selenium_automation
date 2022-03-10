from selenium.webdriver.common.by import By

MENU_LOCATOR = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]")
PRODUCT_TITLE_LOCATOR = (By.XPATH, "//*[@class='product_list grid row']/li[2]/div/div[2]/h5/a")
SECOND_PRODUCT_LOCATOR = (By.XPATH, "//*[@class='product_list grid row']/li[2]")
ADD_TO_CART_LOCATOR = (By.XPATH, "//*[@class='product_list grid row']/li[2]/div/div[2]/div[2]/a[1]")
ADDED_PRODUCT_TITLE_LAYER_LOCATOR = (By.ID, "layer_cart_product_title")
ADDED_PRODUCT_LAYER_CLOSE_BUTTON_LOCATOR = (By.XPATH, "//*[@class='layer_cart_product col-xs-12 col-md-6']/span")
CART_LOCATOR = (By.XPATH, "//*[@class='shopping_cart']/a")
DELETE_PRODUCT_FROM_CART_LOCATOR = (By.XPATH, "//*[@class='products']/dt[1]/span")
CART_DETAIL_LOCATOR = (By.XPATH, "//*[@class='shopping_cart']/a/span[5]")