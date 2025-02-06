
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class CheckoutTest:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_items_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        
    def proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()
        self.driver.find_element(By.ID, "checkout").click()
        
    def enter_checkout_details(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        
    def verify_payment_information(self):
        payment_info_label = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='payment-info-label']"))
        )
        assert payment_info_label.is_displayed(), "Payment Information label is not visible"

def test_checkout_scenario():
    driver = webdriver.Chrome()  # Or any other WebDriver you are using
    driver.get("https://www.example.com/")  # Replace with the actual URL

    try:
        login_page = LoginPage(driver)
        login_page.login("your_username", "your_password")

        checkout_test = CheckoutTest(driver)
        checkout_test.add_items_to_cart()
        checkout_test.proceed_to_checkout()
        checkout_test.enter_checkout_details("somename", "lastname", "123456")
        checkout_test.verify_payment_information()
    finally:
        driver.quit()

test_checkout_scenario()
