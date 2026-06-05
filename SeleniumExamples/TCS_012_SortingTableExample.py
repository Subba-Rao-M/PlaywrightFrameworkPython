import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser_sorted_vegetables_list = []



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

#Click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#Get the first column values to a list
vegetables_list = driver.find_elements(By.XPATH, "//tr/td[1]")
for veg in vegetables_list:
    browser_sorted_vegetables_list.append(veg.text)

#Capture original browser sorted list
original_browser_sorted_veg_list = browser_sorted_vegetables_list.copy() ## slice can also be used

# Sort the browser captured list
browser_sorted_vegetables_list.sort()
print(browser_sorted_vegetables_list)
print(original_browser_sorted_veg_list)
#Compare the both lists
assert original_browser_sorted_veg_list == browser_sorted_vegetables_list