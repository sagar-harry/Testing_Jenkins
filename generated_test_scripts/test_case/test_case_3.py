
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

# Set up the LoginPage class
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "#user-name"
        self.password_locator = "#password"
        self.login_button_locator = "#login-button"

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, self.username_locator).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.password_locator).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_locator).click()

# Set up the test case
class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('YOUR_UI_APPLICATION_URL')  # Replace with your application's login URL
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_cart_functionality(self):
        driver = self.driver
        login_page = LoginPage(driver)

        # Step 1: Login
        login_page.login('testuser', 'testpassword')  # Use valid credentials
        time.sleep(2)

        # Step 2: Add 'Bike Light' to the cart
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()

        # Step 3: Add 'Fleece Jacket' to the cart
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)

        # Step 4: Check the cart badge is '2'
        cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        self.assertEqual(cart_badge, '2', "Cart badge should display '2'")

        # Step 5: Reset the cart
        driver.find_element(By.CSS_SELECTOR, "#reset_sidebar_link").click()
        time.sleep(2)

        # Step 6: Check the cart is empty
        cart_badge = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
        self.assertEqual(len(cart_badge), 0, "Cart should be empty after reset")

        # Step 7: Add 'Bolt T-Shirt' to the cart
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)

        # Step 8: Check the cart badge is '1'
        cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
        self.assertEqual(cart_badge, '1', "Cart badge should display '1'")

if __name__ == '__main__':
    unittest.main()
```

Make sure to replace `'YOUR_UI_APPLICATION_URL'` with the actual URL of the login page of the application you want to test. Also, replace `'testuser'` and `'testpassword'` with valid login credentials for the application.