"""
Request Library Demo
pip install requests



"""
import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'},)
print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(dict_response[0]['isbn'])


## Above same code can be written as below using json() method of response object which will directly convert json string to dictionary
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the book details with ISBN PM730
for actualBook in json_response:
    if actualBook['isbn'] == 'PM730':
        print(actualBook)
        break

expectedBook = {"book_name":"API","isbn":"PM730","aisle":"227"}

assert actualBook == expectedBook
