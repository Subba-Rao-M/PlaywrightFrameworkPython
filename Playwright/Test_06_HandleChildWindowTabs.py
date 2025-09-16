from playwright.sync_api import Page, expect


def test_handlechildwindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #page.locator(".blinktext").click()
    #above line opens new tab and page object will not have access to its contents in new page
    with page.expect_popup() as newPage_info:
        #step1
        #step n
        page.locator(".blinkingText").click()
        childwindow = newPage_info.value # pass the object of new page to child window
        text = childwindow.locator(".red").text_content() # print the content in logs / output
        print(text)#Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")
        #words[0] = Please email us
        # words[1] = mentor@rahulshettyacademy.com with below template to receive response
        #email = words[1].split(" ")[1] # split based on space since first one also space take index 1 or use strip
        email = words[1].strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"