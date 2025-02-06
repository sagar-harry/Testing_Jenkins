
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        
class UICartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("your_application_url_here")
        self.driver.implicitly_wait(10)
        
    def test_add_items_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")  # Username and password for an example

        # Add Bike Light to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        
        # Add Fleece Jacket to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        
        # Verify cart badge displays '2'
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, "2", "Cart badge does not display '2'")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
