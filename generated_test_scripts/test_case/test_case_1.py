
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class TestPurchaseFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://example.com/login-page-url")
        self.login_page = LoginPage(self.driver)

    def test_complete_purchase_flow(self):
        driver = self.driver

        # Log in with valid credentials
        self.login_page.login("valid_username", "valid_password")

        # Add 'Bike Light' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Add 'Fleece Jacket' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Click on the cart icon
        driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

        # Proceed to checkout
        driver.find_element(By.ID, "checkout").click()

        # Enter checkout information
        driver.find_element(By.ID, "first-name").send_keys("somename")
        driver.find_element(By.ID, "last-name").send_keys("lastname")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Click 'Continue' and complete the purchase
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        # Return to homepage
        driver.find_element(By.ID, "back-to-products").click()

        # Log out
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()

        # Validate URL or Page Title to confirm return to homepage (just an example)
        # self.assertEqual(driver.current_url, "http://example.com/homepage-url")
        # self.assertEqual(driver.title, "Home Page Title")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
