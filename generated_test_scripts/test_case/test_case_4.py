
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")

    def tearDown(self):
        self.driver.quit()

    def test_payment_information_display(self):
        driver = self.driver

        # Assuming LoginPage class and its login method exist
        login_page = LoginPage(driver)
        login_page.login(username="your_username", password="your_password")

        # Add 'Bike Light' to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Add 'Fleece Jacket' to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Verify items are added to the cart
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").is_displayed()

        # Proceed to checkout
        driver.find_element(By.ID, "checkout").click()

        # Enter First Name, Last Name, and Zip Code
        driver.find_element(By.ID, "first-name").send_keys("somename")
        driver.find_element(By.ID, "last-name").send_keys("lastname")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Click 'Continue'
        driver.find_element(By.ID, "continue").click()

        # Verify 'Payment Information' label is visible
        payment_info_label = driver.find_element(By.CSS_SELECTOR, "[data-test='payment-info-label']")
        assert payment_info_label.is_displayed(), "Payment Information label is not visible"

if __name__ == "__main__":
    unittest.main()
```

Note: You need to implement the `LoginPage` class with its `login` method separately. Make sure to replace `your_username`, `your_password`, and `https://example.com` with the actual values for your test environment.