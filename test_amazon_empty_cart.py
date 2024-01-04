import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAmazonCart:

    driver = ''
    def setup_method(self):
        # specify the path of the driver
        service = Service('/Users/chiaradigi/Documents/python_selenium_automation_testing/chromedriver')
        # create a new instance of the driver
        self.driver = webdriver.Chrome(service=service)
        #open amazon.com
        self.driver.get('https://www.amazon.com/')
    
    def test_amazon_empty_cart(self):
        wait = WebDriverWait(self.driver, 10)
        # click cart item
        wait.until(EC.element_to_be_clickable((By.ID, 'nav-cart'))).click()   
        # verify cart is empty
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-active-cart']//h2").text
        expected_text = 'Your Amazon Cart is empty'

        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def teardown_method(self):
        # close the browser
        self.driver.quit()