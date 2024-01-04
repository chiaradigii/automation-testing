from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_amazon_search():   
    # specify the path of the driver
    service = Service('/Users/chiaradigi/Documents/python_selenium_automation_testing/chromedriver')
    # create a new instance of the driver
    driver = webdriver.Chrome(service=service)

    driver.get('https://www.amazon.com/')

    # wait for the search bar to be loaded
    wait = WebDriverWait(driver, 10)
    # find the search bar
    search = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    # input text and click enter
    search.send_keys('dress',Keys.ENTER)

    expected_text = '"dress"'
    actual_text = driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text

    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # close the browser
    driver.quit() 