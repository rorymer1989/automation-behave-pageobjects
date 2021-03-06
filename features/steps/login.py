from behave import given, when, then
from config import USER
from features.lib.pages.loginpage import LoginPage


@given(u'"{user_type}" user navigates to page "landing-page"')
def visit_login(context, user_type):
    context.browser.visit('#')


@when(u'the "{user_type}" user logs in')
def login(context, user_type):
    login = context.login.signin(USER[user_type]['email'], USER[user_type]['pass'])
    assert login


@then(u'a login error message should display')
def step_impl(context):
    message = context.browser.contains_content(
        LoginPage.locator_dictionary['error_message'], 5)
    assert message



@then(u'the user should be redirected to homepage')
def homepage(context):
    home = context.browser.contains_content(USER['valid']['username'], 10)
    assert home