
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

class UITestScenario(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_add_items_to_cart(self):
        driver = self.driver
        driver.get('https://www.example.com/login')  # Replace with actual URL

        # Login
        login_page = LoginPage(driver)
        login_page.login("test_user", "test_password")  # Use actual credentials

        # Add Bike Light to cart
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()

        # Add Fleece Jacket to cart
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()

        # Verify that the cart badge displays '2'
        cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        self.assertEqual(cart_badge.text, '2', "Cart badge count does not match expected count.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
