from support.webdriver_helper import WebDriverHelper

def before_all(context):
    context.webdriver_helper = WebDriverHelper(5)

def after_scenario(context, scenario):
    context.webdriver_helper.driver.get('https://hudl.com/logout')

def after_all(context):
    context.webdriver_helper.dispose()