from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class WebDriver():
    def __init__(self, timeout):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(timeout)

    def dispose(self):
        self.driver.quit()