import requests

from apitesting.PayLoad import addBookPayload

addbook_response =requests.post('http://216.10.245.166/Library/Addbook.php', json = addBookPayload("PM730", "9005"), headers= {"Content-Type": "application/json"},)



response_json = addbook_response.json()
print(response_json)

book_id = response_json['ID']

deletebook_response =requests.post('http://216.10.245.166/Library/DeleteBook.php', json = {
    "ID":book_id,
}, headers= {"Content-Type": "application/json"},)

print(deletebook_response)

assert deletebook_response.status_code == 200

delete_response_json = deletebook_response.json()
print(delete_response_json)
assert delete_response_json['msg'] == "book is successfully deleted"