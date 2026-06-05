import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

"""
Selenium Locators: ID, Name, CSS, XPATH, classname, linktext, tagname, partiallinktext
driver.find_element(By.ID, "elementID")
driver.find_element(By.NAME, "elementName")
driver.find_element(By.CLASS_NAME, "className")
driver.find_element(By.TAG_NAME, "tagName")
driver.find_element(By.LINK_TEXT, "Visible Text")
driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Text")
driver.find_element(By.XPATH, "//tag[@attribute='value']")
driver.find_element(By.CSS_SELECTOR, "tag[attribute='value'] antoherattribute")
"""
driver.find_element(By.NAME, "name").send_keys("Subba")
driver.find_element(By.NAME, "email").send_keys("subba1@span.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234@Abcd")
driver.find_element(By.ID, "exampleCheck1").click()

#Static drop down

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male") # Refer dropdown. for different methods available

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

time.sleep(2)