
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

class TestUITestScenario:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")
        self.login_page = LoginPage(self.driver)
    
    def teardown_method(self):
        self.driver.quit()

    def test_cart_functionality(self):
        # Login
        self.login_page.login("test_user", "test_password")
        
        # Add 'Bike Light' to the cart
        bike_light_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        bike_light_button.click()

        # Add 'Fleece Jacket' to the cart
        fleece_jacket_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        fleece_jacket_button.click()

        # Assert cart badge shows '2'
        cart_badge = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == '2', f"Expected cart badge to be '2' but got '{cart_badge.text}'"

        # Reset the cart
        reset_cart_button = self.driver.find_element(By.ID, "reset_sidebar_link")
        reset_cart_button.click()

        # Assert cart is empty
        cart_badge_empty = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(cart_badge_empty) == 0, "Cart badge should be empty but is not"

        # Add 'Bolt T-Shirt' to the cart
        bolt_tshirt_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        bolt_tshirt_button.click()

        # Assert cart badge shows '1'
        cart_badge = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == '1', f"Expected cart badge to be '1' but got '{cart_badge.text}'"
