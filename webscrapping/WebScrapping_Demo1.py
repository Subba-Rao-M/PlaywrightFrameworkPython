"""
Web Scrapping is a technique used to extract data from websites.
It involves fetching the HTML content of web pages
and parsing it to retrieve specific information.
This can be done using various programming languages and libraries,
such as Python with BeautifulSoup or Scrapy.

pip install bs4
using requests library service call is made

"""

import requests
from bs4 import BeautifulSoup

li=[]
data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, 'html.parser') # convert response data to html

print(soup.prettify()) # print the html in readable format
#if java script is returned web scrapping cannot be done example where java script used to render html

moviesTable = soup.find('table',{'class':'findList'}) ## narrow down search to find table with attributes in  {}
print(moviesTable.prettify())
#search with in movies table
rows = moviesTable.findAll('tr')

for row in rows:
    rowData = row.findAll('td')
    title = rowData[1].a.text
    print(title)

for row in rows:
    rowdataa = row.findAll('td')
    print(rowdataa[1].a.text)
    #Get href attribute
    subUrl =rowdataa[1].a['href']
    #navigate to sub url
    subdata = requests.get("https://www.imdb.com"+subUrl)
    childSoup = BeautifulSoup(subdata.content, 'html.parser')
    # to aoid nontype object error add if condition
    if childSoup.find('div',{'class':'see-more inline canwrap'}):
        genre =childSoup.find('div',{'class':'see-more inline canwrap'})
        if genre.a.text == " Documentary":
            print(rowdataa[1].a.text)
            print(genre.a.text)
            li.append(rowdataa[1].a.text)

print(li)