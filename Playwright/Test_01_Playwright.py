#Fixture is used to setup or receive the data
#playwright fixture is global and is present in pytest-playwright package no need to write any other fixture
#Chromium and launch are different methods
#By default playwright executes code in headless mode

from playwright.sync_api import Page
def test_playwrightbasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # all browser activities are isolated and handled here login action and logout
    #Each browser will have its own data and it will not interact with other browsers if multiple browsers created
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#Shortcut of above function using page fixture
#If customization required use above playwright fixture only
# Page fixture is implemented using chromium in headless mode using single context
# 90% of the time this method is used
#when performing api testing we need to switch between contexts in that case also page fixture cannot be direclty used
# To get suggestions use import playwright options
## In modify run configuration give arguments
# In terminal goto directory playwright and run using file name :: function name --headed

#The new_context() method in Playwright indeed creates a new temporary browsing session, which allows you to test different scenarios in isolation by managing cookies and storage separately. This capability is crucial for ensuring that tests do not interfere with one another, helping you maintain accurate and reliable testing results.

def test_playwrightpagefixture(page:Page):
    page.goto("https://rahulshettyacademy.com")



#Record and Playback using Playwright
# Go To Terminal and give below command
# playwright codegen baseurl

