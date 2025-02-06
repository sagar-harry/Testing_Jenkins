
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class UIAutomationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://example.com')  # Replace with the actual URL
        self.login_page = LoginPage(self.driver) 

    def login(self, username, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()
        
    def test_checkout_payment_information(self):
        driver = self.driver
        
        # Step 1: Login
        self.login_page.login('your_username', 'your_password')  # Add correct username and password 

        # Step 2: Add 'Bike Light' to the cart
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()

        # Step 3: Add 'Fleece Jacket' to the cart
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()
        
        # Step 4: Proceed to checkout
        driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').click()
        driver.find_element(By.ID, 'checkout').click()

        # Step 5: Enter user information
        driver.find_element(By.ID, 'first-name').send_keys('somename')
        driver.find_element(By.ID, 'last-name').send_keys('lastname')
        driver.find_element(By.ID, 'postal-code').send_keys('123456')

        # Step 6: Continue to the next page
        driver.find_element(By.ID, 'continue').click()

        # Step 7: Verify that the 'Payment Information' section is visible
        payment_info_label = driver.find_element(By.CSS_SELECTOR, "[data-test='payment-info-label']")
        self.assertTrue(payment_info_label.is_displayed(), "Payment Information is not visible")

    def tearDown(self):
        self.driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

if __name__ == '__main__':
    unittest.main()
