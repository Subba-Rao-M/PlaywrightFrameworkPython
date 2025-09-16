from playwright.sync_api import Page, expect


def test_uitable(page: Page):
    global pricecolvalue
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # check the price of rice is 37
    # Go to price column and check the price
    # identify column header using locator th and use for loop to navigate each column headers
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0: # Check if the Price column count becomes 1
            pricecolvalue = index
            print(f"index column value of rice is {pricecolvalue}") # use f to pass the value inside print statement variable
            break # come out of for loop if Price column searched

    #Now capture the row where Rice is available
    ricerow = page.locator("tr").filter(has_text="Rice")

    #Check the price of Rice value
    expect(ricerow.locator("td").nth(pricecolvalue)).to_have_text("37")

