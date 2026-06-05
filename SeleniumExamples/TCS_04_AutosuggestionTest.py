#Dropdown dont have select tags and drop down suggests value based on text entered
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2) # wait for drop down to open

#Get all values of drop down using findelements and store in list
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    print(country.text) # to get the text of web element retrieved
    if country.text == "India":
        country.click()
        break

time.sleep(2)

# text will check only the value present during load of page
print("text method ", driver.find_element(By.ID, "autosuggest").text)
#get attribute will check and give the values entered to input fields
print("get attribute", driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"