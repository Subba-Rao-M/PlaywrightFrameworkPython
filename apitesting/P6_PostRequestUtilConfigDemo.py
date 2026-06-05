import requests
import configparser # used to read the properties file data

from apitesting.PayLoad import addBookPayload


from utilities.configurations import getConfig

endpoint = getConfig()['API']['endpoint'] # read the endpoint value from properties file

addbook_response =requests.post(endpoint+"/Library/Addbook.php", json = addBookPayload("PM730"), headers= {"Content-Type": "application/json"},)

response_json = addbook_response.json()
print(response_json)

book_id = response_json['ID']

deletebook_response =requests.post(endpoint+"/Library/DeleteBook.php", json = {
    "ID":book_id,
}, headers= {"Content-Type": "application/json"},)

print(deletebook_response)

assert deletebook_response.status_code == 200

delete_response_json = deletebook_response.json()
print(delete_response_json)
assert delete_response_json['msg'] == "book is successfully deleted"