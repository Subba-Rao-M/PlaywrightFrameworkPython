import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from PlaywrightFramework.pageobjects.LoginPage import LoginPage
from PlaywrightFramework.utils.ApiUtils import ApiUtils

scenarios('OrderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}
# above fixture is created with empty dictionary return value
# in below step definitions the data which needs to be shared across steps are mapped with key and value pair
# Data is assigned and retrieved using fixture name

#parser.parse class is used if step definition has data in it and read the data inside {variable} else it will be considered as string
@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["user_email"] = username
    user_credentials["user_password"] = password
    api_utils = ApiUtils()
    order_id = api_utils.create_order(playwright, user_credentials)
    shared_data['order_id'] = order_id # Assign data to dictionary key


@given('the user is on landing page')
def user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data['login_page'] = login_page


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.do_login(username, password)
    shared_data['dashboard_page'] = dashboard_page


@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page'] # Retrieve data using dictionary
    order_history_page = dashboard_page.navigate_to_orders_page()
    shared_data['orderhistory_page'] = order_history_page


@when('select the orderId')
def select_order_id(shared_data):
    order_history_page = shared_data['orderhistory_page']
    order_id = shared_data['order_id']
    order_details_page = order_history_page.click_view_for_order_id(order_id)
    shared_data['orderdetails_page'] = order_details_page


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    order_details_page = shared_data['orderdetails_page']
    order_details_page.verify_order_message()