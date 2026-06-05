from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.maximize_window()
driver.implicitly_wait(5)

#Download file
driver.find_element(By.ID, "downloadButton").click()

#Upload file
#To upload file the input tag should have type as file else request developer to add that attribute
driver.find_element(By.ID, "fileinput").send_keys("C:\\Users\\raooosub\\Downloads\\download.xlsx")

wait = WebDriverWait(driver, 30)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(ec.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)