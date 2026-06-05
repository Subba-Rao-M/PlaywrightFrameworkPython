## in browser console enter window. and see the different options available which supports in java script executor
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") ## to bottom of page
# enter different value for y coordinate value
driver.get_screenshot_as_file("screen.png")


time.sleep(3)