from utilities.configurations import *

def addBookPayload(isbn, aisle):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }
    return body


#dynamically build payload based on values in DB
def buildPayLoadFromDB(query):

    add_body = {}
    row_value = getQuery(query) # get the values in tuple format and get column values based on index
    add_body['name'] = row_value[0]
    add_body['isbn'] = row_value[1]
    add_body['aisle'] = row_value[2]
    add_body['author'] = row_value[3]
    return add_body