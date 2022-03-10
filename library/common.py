import random
import string
from selenium import webdriver


def get_chrome_webdriver():
    return webdriver.Chrome(executable_path="C:\\Users\\Shruti.pathak\\SeleniumProject\\chromedriver.exe")

def get_random_email(domain="gmail.com"):
    return ''.join(random.choice(string.ascii_letters) for x in range(7))+"@"+domain
