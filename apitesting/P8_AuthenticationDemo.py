#Authentication
import requests

from apitesting.utilities.configurations import getPassword
#Importance of session management
se = requests.session()
se.auth = auth=('Subba-Rao-M',getPassword())

#verify = False is used to ignore SSL certificate warnings
url1 = "https://api.github.com/user"
github_response = requests.get(url1,verify=False,auth=('Subba-Rao-M',getPassword()))
print(github_response.status_code)



url2 = "https://api.github.com/user/repos"
response= se.get(url2) # se will autheticate for all requests can be reused for multiple requests
print(response.status_code)

##Upload files

