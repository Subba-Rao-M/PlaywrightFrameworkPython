from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

#ActionChains class helps to perform certain actions on element like drag & drop, right click, double click etc
#Actions should end with .perform
actions = ActionChains(driver)
#actions.click_and_hold() # for long press on element
#actions.context_click() # for right click on element
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform() ## move to particular element
#actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform() ## different actions can be performed before perform
actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).click().perform()