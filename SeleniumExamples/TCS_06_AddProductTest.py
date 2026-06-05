import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(10)# global max wait of 5 seconds for each step

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")# implicit wait will not appear for result even if empty list returned implicit wait will consider it as valid data
count = len(results)
assert count > 0 # number of search result greater than 0

# Get the actual item name and add the item to cart
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click() # locator chaining or chaining of web elements

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt ='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
total_price=0
for price in prices:
    total_price= total_price + int(price.text)
print(total_price)
ui_total_price = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
print(ui_total_price)
assert  int(ui_total_price) == total_price

#Promo Code Apply Logic

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

# Explicit wait
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promotext = driver.find_element(By.CLASS_NAME, "promoInfo").text

discounted_Amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discounted_Amount < int(ui_total_price)