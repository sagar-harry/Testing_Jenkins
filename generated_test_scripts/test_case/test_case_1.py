
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class PurchaseFlowTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")
        self.login_page = LoginPage(self.driver)

    def test_complete_purchase_flow(self):
        # Login
        self.login_page.login("valid_username", "valid_password")
        
        # Add items to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        
        # Proceed to Cart
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        
        # Checkout
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("somename")
        self.driver.find_element(By.ID, "last-name").send_keys("lastname")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()
        
        # Complete Purchase
        self.driver.find_element(By.ID, "finish").click()
        
        # Back to homepage
        self.driver.find_element(By.ID, "back-to-products").click()
        
        # Verify back to homepage
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://example.com/home", "Failed to return to homepage")
        
        # Log out
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        
        # Verify logout 
        login_page_url = self.driver.current_url
        self.assertEqual(login_page_url, "https://example.com/login", "Failed to log out")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
