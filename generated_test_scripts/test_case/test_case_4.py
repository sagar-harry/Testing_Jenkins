
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

class UITestScenario(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='path/to/chromedriver')
        cls.driver.get("http://example.com/login")
        cls.driver.maximize_window()
        
    def test_order_checkout_flow(self):
        login_page = LoginPage(self.driver)

        # Step 1: Login as a user
        login_page.login("testuser", "testpass")

        # Step 2: Add 'Bike Light' and 'Fleece Jacket' to the cart
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()

        # Verify items added to cart
        cart_badge = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
        self.assertEqual(cart_badge.text, "2", "Cart badge should display 2 items")

        # Step 3: Proceed to checkout
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        # Step 4: Enter checkout details
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("somename")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("lastname")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

        # Step 5: Verify 'Payment Information' label is visible
        payment_info_label = self.driver.find_element(By.CSS_SELECTOR, "[data-test='payment-info-label']")
        self.assertTrue(payment_info_label.is_displayed(), "'Payment Information' label should be visible")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
