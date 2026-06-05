import requests

addbook_response =requests.post('http://216.10.245.166/Library/Addbook.php', json = {
    "name":"Learn Appium Automation with Java",
    "isbn":"PM730",
    "aisle":"227",
    "author":"John foe"
}, headers= {"Content-Type": "application/json"},)



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