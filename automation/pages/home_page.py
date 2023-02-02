from pages.base_page import BasePage

class HomePage(BasePage):
    def header_is_displayed(self):
        return self.webdriver_helper.element_is_displayed('[data-qa-id="webnav-globalnav-home"]')