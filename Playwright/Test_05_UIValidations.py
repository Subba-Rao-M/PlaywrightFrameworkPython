from playwright.sync_api import Page, expect


def test_locatorswithfilterlogic(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    #use filter logic with different has options
    iphoneproduct = page.locator("app-card").filter(has_text= "iphone X")
    #page objects chaining
    iphoneproduct.get_by_role("button", name="Add").click()
    nokiaproduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaproduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()#Partial text matching for button with text Checkout (2)
    expect(page.locator(".media-body")).to_have_count(2)