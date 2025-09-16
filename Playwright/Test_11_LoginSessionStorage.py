import pytest
from playwright.sync_api import Playwright, expect

from utils.apibase import APIUtils

@pytest.mark.smoke
def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    gettoken = api_utils.gettoken(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #script to inject token into browser storage. Java script needs to be injected using triple quotes
    page.add_init_script(f""" localStorage.setItem('token', '{gettoken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()