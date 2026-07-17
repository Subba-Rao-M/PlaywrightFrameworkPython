import json
import configparser
from payLoad import *

from apitesting.PayLoad import buildPayLoadFromDB
from utilities.resources import *
from utilities.configurations import *

import requests

url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
query = 'select * from Books'
addBook_response = requests.post(url,json=buildPayLoadFromDB(query),headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)
# Delete Book -
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookId
}, headers={"Content-Type": "application/json"},
                                    )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"







