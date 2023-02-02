from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def input_email(self, email):
        self.driver.find_element(By.ID, 'email').send_keys(email)

    def input_password(self, password):
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def submit(self):
        self.driver.find_element(By.ID, 'logIn').click()

    def get_error_message(self):
        return self.webdriver_helper.get_by_qa_id('error-display').text
