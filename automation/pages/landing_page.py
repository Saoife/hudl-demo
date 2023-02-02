from pages.base_page import BasePage

class LandingPage(BasePage):
    def go_to(self):
        self.driver.get('https://hudl.com')

    def open_login_page(self):
        self.webdriver_helper.get_by_qa_id('login').click()
