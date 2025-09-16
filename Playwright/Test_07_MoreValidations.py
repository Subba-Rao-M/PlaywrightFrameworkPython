import time

from playwright.sync_api import Page, expect


def test_uicheck(page: Page):
    #Check visible, hide assertion and placeholder locator
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alerts are not visible in html code and driven by java script events
    page.on("dialog", lambda dialog:dialog.accept()) # refer difference with open child window page.expect_popup()
    page.get_by_role("button", name="Confirm").click()
    # there is a chance of triggering alert window
    # Use method on - which takes 2 arguments - what type of event and on event what happens
    # add the on method before which happens
    # lambda is anonymous function it is used when there is no need of function name and write one liner codes
    time.sleep(3)

    # Handling Frames
    # Frames are embedded within same page and can have tag iframe, frame which may have properties like id, name class
    # cannot use page.locator instead use frame_locator
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link", name="All Access plan").click() ## access fields inside frame
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers")#Search from entire html body

    #To switch back to main page use page.

    # Mouse Hovers
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()