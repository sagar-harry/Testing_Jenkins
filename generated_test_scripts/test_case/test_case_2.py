
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestShoppingCartBadge(unittest.TestCase):
    
    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")  # Replace with the correct URL
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()
    
    def test_cart_badge(self):
        driver = self.driver
        
        # Use the LoginPage class to log in
        login_page = LoginPage(driver)
        login_page.login("testuser", "password123")  # Replace with valid credentials
        
        # Add 'Bike Light' to the cart
        bike_light_add_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        bike_light_add_to_cart.click()
        
        # Add 'Fleece Jacket' to the cart
        fleece_jacket_add_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        fleece_jacket_add_to_cart.click()
        
        # Verify the cart badge shows '2'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "2", "Cart badge should display '2'")
        
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

if __name__ == "__main__":
    unittest.main()
