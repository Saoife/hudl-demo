from behave import given, when, then
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.home_page import HomePage

@given('the user is on the login page')
def step_impl(context):
    landing_page = LandingPage(context.webdriver)
    landing_page.go_to()
    landing_page.open_login_page()

    context.login_page = LoginPage(context.webdriver)
    
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

@then('the home page is displayed')
def step_impl(context):
    home_page = HomePage(context.webdriver)
    assert home_page.header_is_displayed() is True

@then('the user is not logged in')
def step_impl(context):
    home_page = HomePage(context.webdriver)
    assert home_page.header_is_displayed() is False

@then('an error message is displayed')
def step_impl(context):
    assert "We didn't recognize that email and/or password" in context.login_page.get_error_message()