from behave import given, when, then
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.keys import Keys

@given('the user is on the login page')
def step_impl(context):
    landing_page = LandingPage(context.webdriver_helper)
    landing_page.go_to()
    landing_page.open_login_page()

    context.login_page = LoginPage(context.webdriver_helper)
    
@when('the user attempts to login with the correct details')
def step_impl(context):
    context.login_page.input_email('saoirse.fenlon@gmail.com')
    context.login_page.input_password('password1')
    context.login_page.submit()
    
@when('the user attempts to login providing only the email')
def step_impl(context):
    context.login_page.input_email('saoirse.fenlon@gmail.com')
    context.login_page.submit()

@when('the user attempts to login providing only the password')
def step_impl(context):
    context.login_page.input_password('password1')
    context.login_page.submit()
    
@when('the user attempts to login providing an incorrect email')
def step_impl(context):
    context.login_page.input_email('incorrect.email@gmail.com')
    context.login_page.input_password('password1')
    context.login_page.submit()
    
@when('the user attempts to login providing an incorrect password')
def step_impl(context):
    context.login_page.input_email('saoirse.fenlon@gmail.com')
    context.login_page.input_password('incorrectPassword')
    context.login_page.submit()
    
@when('the user attempts to login using only the keyboard')
def step_impl(context):
    context.webdriver_helper.input_to_current_element('saoirse.fenlon@gmail.com')
    context.webdriver_helper.input_to_current_element(Keys.TAB)
    context.webdriver_helper.input_to_current_element('password1')
    context.webdriver_helper.input_to_current_element(Keys.ENTER)
    
@when('the user enters a script into the {field} field')
def step_impl(context, field):
    match field:
        case 'email':
            context.login_page.input_email('<script>alert("hi")</script>')
            context.login_page.input_password('incorrectPassword')
        case 'password':
            context.login_page.input_email('saoirse.fenlon@gmail.com')
            context.login_page.input_password('<script>alert("hi")</script>')
        case _:
            raise IndexError(input)
    
@when('the user attempts to login')
def step_impl(context):
    context.login_page.submit()

@then('the home page is displayed')
def step_impl(context):
    home_page = HomePage(context.webdriver_helper)
    assert home_page.header_is_displayed()

@then('the user is not logged in')
def step_impl(context):
    home_page = HomePage(context.webdriver_helper)
    assert not home_page.header_is_displayed()

@then('an error message is displayed')
def step_impl(context):
    assert "We didn't recognize that email and/or password" in context.login_page.get_error_message()

@then('an alert is not displayed')
def step_impl(context):
    assert not context.webdriver_helper.is_alert_displayed()