import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAmazon:

    testdata = ('dress','shoes','bags','hats','gloves')

    driver = ''
    def setup_method(self):
        # specify the path of the driver
        service = Service('/Users/chiaradigi/Documents/python_selenium_automation_testing/chromedriver')
        # create a new instance of the driver
        self.driver = webdriver.Chrome(service=service)

        self.driver.get('https://www.amazon.com/')

    @pytest.mark.parametrize('search_query', testdata)
    def test_amazon_search_dress(self, search_query):   
        # wait for the search bar to be loaded
        wait = WebDriverWait(self.driver, 10)
        # find the search bar
        search = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
        # input text and click enter
        search.send_keys(search_query,Keys.ENTER)

        expected_text = f'\"{search_query}\"' 
        actual_text = self.driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text

        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    

    def teardown_method(self):
        # close the browser
        self.driver.quit()