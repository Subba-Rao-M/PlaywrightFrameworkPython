import requests


# all common codes related to befor and after scenario should be added in environment.py file
# Refer official documentation of behave for more details
def after_scenario(context, scenario):
    #if after scenario to be executed for particulat scenario
    if "library" in scenario.tags:
        response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

            "ID": context.bookId
        }, headers={"Content-Type": "application/json"},
                                            )

        assert response_deleteBook.status_code == 200
        res_json = response_deleteBook.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"


#behave apitesting/features/BookAPI.feature --no-capture --tags=library
# --no-capture is used to see the print statements in console
# use only behave to run all test cases or to generate the step definitions file
#pip install behave
# pip install allure-beahve
#bbehave apitesting/features/BookAPI.feature --no-capture --tags=library -f allure_behave.formatter:AllureFormatter -o AllureReports
#configure to open allure report in browser using official allure doucmentation