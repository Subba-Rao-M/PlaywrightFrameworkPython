from playwright.sync_api import Page

def test_locatorslabelsandrole(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()


#role mouse over to know different roles
#select option is using value available in option tag not text displayed in ui
#To use label field should have label tag
# for input text box to use label, input tag is wrapped inside label tag then only it will work
# or one more scenario field label should be linked using for attribute reference
# else use different mechanism identify the field
# button class can have reference btn and further filtering using name option to identify uniquely

## CSS Selectors
# Using ID #idoffield
# Using Class .classnameoffield
# Using tag names
# for css use page.locator()
