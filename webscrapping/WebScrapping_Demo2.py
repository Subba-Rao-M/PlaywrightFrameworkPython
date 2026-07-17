import requests
from bs4 import BeautifulSoup

data = requests.get("https://rahulshettyacademy.com/AutomationPractice/")
soup = BeautifulSoup(data.content,'html.parser')
print(soup.prettify())

#Search based on string visible in screen
appium = soup.find('a',string='Appium')
print(appium['href'])


