from playwright.sync_api import Page, expect

# api call from browser - > api calls contacts server and server return back response - > browser use response to generate data
#fulfill method helps in tweaking the response for mocking the different data in UI
fakePayLoadOrders = { "data": [], "message": "No Orders" }

#normal function without test key in function name
def intercept_response(route):
    route.fulfill(
        json = fakePayLoadOrders
    )

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=621661f884b053f6765465b6")

# To intercept network response route - fulfill is used
def test_networkfulfill(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    #playwright script keep on checking for below request url
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.co").fill("subbaraw@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Span@1234")
    page.get_by_role("button", name="Login").click()
    ## Go to order history page and verify the order id created
    page.get_by_role("button", name="ORDERS").click()
    message = page.locator(".mt-4").text_content()
    print(message)
    expect(page.locator(".mt-4")).to_contain_text("You have No Orders")


# To intercept network request route - > continue is used
def test_networkcontinue(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.co").fill("subbaraw@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Span@1234")
    page.get_by_role("button", name="Login").click()
    ## Go to order history page and verify the order id created
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")