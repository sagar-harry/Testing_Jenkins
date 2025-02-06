
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class TestPurchaseFlow(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def setUp(self):
        self.driver.get('http://example.com/login')  # Replace with the actual login URL
    
    def test_purchase_flow(self):
        # Login to the application
        login_page = LoginPage(self.driver)
        login_page.login('valid_username', 'valid_password')

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()
        
        # Click on the cart icon
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').click()
        
        # Proceed to checkout
        self.driver.find_element(By.ID, 'checkout').click()
        
        # Enter personal details
        self.driver.find_element(By.ID, 'first-name').send_keys('somename')
        self.driver.find_element(By.ID, 'last-name').send_keys('lastname')
        self.driver.find_element(By.ID, 'postal-code').send_keys('123456')
        
        # Continue to the next step and complete the purchase
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.ID, 'finish').click()
        
        # Verify that user can return to the homepage
        back_button = self.driver.find_element(By.ID, 'back-to-products')
        back_button.click()
        self.assertTrue(back_button.is_displayed(), 'Failed to return to homepage')
        
        # Log out
        self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
        self.driver.find_element(By.ID, 'logout_sidebar_link').click()

        # Verify that user is logged out by checking the login page URL
        self.assertIn('login', self.driver.current_url, 'Logout was not successful')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

if __name__ == '__main__':
    unittest.main()
