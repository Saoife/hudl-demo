from behave import fixture
from support.webdriver import WebDriver
from pages.home_page import HomePage

@fixture
def before_all(context):
    context.webdriver = WebDriver(5)

def after_scenario(context, scenario):
    context.webdriver.driver.get('https://hudl.com/logout')

def after_all(context):
    context.webdriver.dispose()