import requests


cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com',allow_redirects=False,cookies=cookie,timeout=1)
#301,200 redirection happens from one url to another url and gets response from the final url
# allow_redirects = False will not allow redirection to happen and we will get response from the initial url
#timeout = 1 will wait for 1 second to get response from the server if it does not get response within 1 second it will throw an exception
print(response.history) # to know if any redirection happened it will be tracked in history
print(response.status_code)







