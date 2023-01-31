from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LandingPage(BasePage):
    def go_to(self):
        self.driver.get('https://hudl.com')

    def open_login_page(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-qa-id="login"]').click()