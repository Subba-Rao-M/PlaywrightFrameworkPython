import requests
import utilities.resources

from apitesting.PayLoad import addBookPayload
from apitesting.utilities.resources import ApiResources

from utilities.configurations import getConfig

endpoint = getConfig()['API']['endpoint'] # read the endpoint value from properties file
headers = {"Content-Type": "application/json"}
## call api resources class to get the resource url
addbook_response =requests.post(endpoint+ApiResources.addBook, json = addBookPayload("PM730", "8001"), headers= headers,)

response_json = addbook_response.json()
print(response_json)

book_id = response_json['ID']

deletebook_response =requests.post(endpoint+ApiResources.deleteBook, json = {
    "ID":book_id,
}, headers= headers,)

print(deletebook_response)

assert deletebook_response.status_code == 200

delete_response_json = deletebook_response.json()
print(delete_response_json)
assert delete_response_json['msg'] == "book is successfully deleted"