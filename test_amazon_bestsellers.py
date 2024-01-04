from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAmazonCart:

    driver = ''
    def setup_method(self):
        # specify the path of the driver
        service = Service('/Users/chiaradigi/Documents/python_selenium_automation_testing/chromedriver')
        # create a new instance of the driver
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        #open amazon.com
        self.driver.get('https://www.amazon.com/')
    
    def test_amazon_bestsellers_links(self):
        # click best sellers link
        self.driver.find_element(By.XPATH,"//div[@id='nav-xshop']/a[contains(@href,'gift-cards')]").click()

        # verify there is 5 links
        actual_links = self.driver.find_elements(By.XPATH,"//div[@id='nav-xshop']//a")
        assert len(actual_links) == 6, f'Expected 6 links, but got {len(actual_links)}'

    def teardown_method(self):
        # close the browser
        self.driver.quit()