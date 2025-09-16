import json
import os
import pytest
from playwright.sync_api import Playwright

from PlaywrightFramework.pageobjects.LoginPage import LoginPage
from PlaywrightFramework.utils.ApiUtils import ApiUtils

# ------------------------------------------------------------------
# ✅ Load test data from JSON file
# This allows data-driven testing by feeding credentials as test input
# JSON structure: { "user_credentials": [ { "user_email": "...", "user_password": "..." }, ... ] }
# ------------------------------------------------------------------

# Dynamically determine path to credentials.json (makes it OS and project-structure agnostic)
current_dir = os.path.dirname(__file__)  # This test file's directory
file_path = os.path.join(current_dir, '..', 'data', 'credentials.json')

with open(os.path.abspath(file_path)) as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']  # List of dictionaries


# ------------------------------------------------------------------
# ✅ Parametrize test with multiple sets of user credentials
# Use `indirect=True` when passing test data to a fixture (e.g., user_credentials)
# This will call the fixture and pass the param into it (as done in conftest.py)
# ------------------------------------------------------------------
@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
def test_e2e_web_api(playwright: Playwright, browser_instance, user_credentials):
    """
    End-to-End Web + API Integration Test:
    - Creates an order via API
    - Logs in via UI using Playwright
    - Navigates to Order History
    - Verifies the order exists in UI
    """

    # ✅ Step 1: Use API to create order and get order ID
    api_utils = ApiUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    # ✅ Extract credentials for login
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    print(f"🔄 Running test for user: {user_email} | Created Order ID: {order_id}")

    # ✅ Step 2: Log in using LoginPage (Page Object)
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    dashboard_page = login_page.do_login(user_email, user_password)

    # ✅ Step 3: Navigate to Order History
    order_history_page = dashboard_page.navigate_to_orders_page()

    # ✅ Step 4: View the specific order using Order ID
    order_details_page = order_history_page.click_view_for_order_id(order_id)

    # ✅ Step 5: Verify the confirmation message
    order_details_page.verify_order_message()

    # ✅ Optional: Add cleanup steps if needed (e.g., cancel order, logout)
    print(f"✅ Running test completed for user: {user_email} | Created Order ID: {order_id}")