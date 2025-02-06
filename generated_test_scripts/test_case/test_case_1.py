
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class TestLoginAndPurchaseFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_complete_purchase_flow(self):
        driver = self.driver

        # Login to the application
        self.login_to_application("standard_user", "secret_sauce")

        # Add items to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

        # Proceed to checkout
        driver.find_element(By.ID, "checkout").click()

        # Enter information and continue
        driver.find_element(By.ID, "first-name").send_keys("somename")
        driver.find_element(By.ID, "last-name").send_keys("lastname")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Finish the purchase
        driver.find_element(By.ID, "finish").click()

        # Verify the user can return to homepage
        driver.find_element(By.ID, "back-to-products").click()

        # Log out
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "logout_sidebar_link").click()

    def login_to_application(self, username, password):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
