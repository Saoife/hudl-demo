class BasePage:
    def __init__(self, webdriver):
        self.webdriver_helper = webdriver
        self.driver = self.webdriver_helper.driver
