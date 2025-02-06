
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class SaucedemoTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver and open the browser
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_add_items_to_cart(self):
        driver = self.driver
        # Login to the application using the LoginPage method
        self.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to the cart
        bike_light_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        bike_light_button.click()

        # Add 'Fleece Jacket' to the cart
        fleece_jacket_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        fleece_jacket_button.click()

        # Verify the cart badge displays '2'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "2", "Cart badge must display '2'")

    def login(self, username, password):
        driver = self.driver
        # Use the LoginPage class to login
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

if __name__ == "__main__":
    unittest.main()
