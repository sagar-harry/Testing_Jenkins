
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com") # Replace with the actual URL

    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

    def test_shopping_cart_scenario(self):
        driver = self.driver
        self.login("standard_user", "secret_sauce")  # Replace with the actual credentials

        # Add Bike Light to cart
        bike_light = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        bike_light.click()

        # Add Fleece Jacket to cart
        fleece_jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        fleece_jacket.click()

        # Verify cart badge displays '2'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, '2')

        # Reset the cart
        reset_cart = driver.find_element(By.ID, "reset_sidebar_link")
        reset_cart.click()

        # Verify cart is empty
        cart_items = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(cart_items), 0)

        # Add Bolt T-Shirt to cart
        bolt_tshirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        bolt_tshirt.click()

        # Verify cart badge displays '1'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, '1')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
