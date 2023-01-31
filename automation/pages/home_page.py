from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def header_is_displayed(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, '[data-qa-id="webnav-globalnav-home"]').is_displayed()
        except:
            return False