import time

from playwright.sync_api import Playwright, expect

from utils.apibase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order and get Order ID
    api_utils = APIUtils()
    orderid = api_utils.createorder(playwright)

    #Login using web
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.co").fill("subbaraw@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Span@1234")
    page.get_by_role("button", name="Login").click()

    ## Go to order history page and verify the order id created
    page.get_by_role("button", name="ORDERS").click()
    page.locator("tr").filter(has_text=orderid).get_by_role("button", name="View").click() # Chaining or split with row
    #row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping")
    time.sleep(3)
    context.close() #Optional for free up space and playwright automatically does this
