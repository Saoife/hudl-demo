from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class WebDriverHelper():
    def __init__(self, timeout):
        self.timeout = timeout
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(self.timeout)

    def get_by_qa_id(self, id):
        return self.driver.find_element(By.CSS_SELECTOR, f'[data-qa-id="{id}"]')

    def element_is_displayed(self, selector):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, selector).is_displayed()
        except NoSuchElementException:
            return False
    
    def get_current_element(self):
        return self.driver.switch_to.active_element
        
    def input_to_current_element(self, key):
        self.get_current_element().send_keys(key)

    def is_alert_displayed(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def dispose(self):
        self.driver.quit()