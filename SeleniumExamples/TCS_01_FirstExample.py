import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)

"""

Installing Selenium
pip install selenium
or use pip3 if multiple versions

pip install --upgrade selenium # to upgrade selenium versions

python -m pip show selenium # to check selenim version

"""

