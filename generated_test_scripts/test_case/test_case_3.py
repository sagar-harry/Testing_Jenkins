
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestCartFunctionality(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")  # Replace with your application URL
        self.login()

    def login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("your_username")
        driver.find_element(By.ID, "password").send_keys("your_password")
        driver.find_element(By.ID, "login-button").click()

    def test_add_items_to_cart(self):
        driver = self.driver
        
        # Add 'Bike Light' to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        
        # Add 'Fleece Jacket' to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Verify cart badge displays '2'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, '2', "Cart badge should display '2'")

        # Reset the cart
        driver.find_element(By.ID, "reset_sidebar_link").click()

        # Verify cart is empty
        cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(cart_badges), 0, "Cart should be empty")

        # Add 'Bolt T-Shirt' to the cart after reset
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Verify cart badge displays '1'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, '1', "Cart badge should display '1'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
