import requests

#http://rahulshettyacademy.com
#'visit-month' -- cookie used in above site
cookie = {'visit-month':'February'} # cookie can be added as a dictionary in below url or pass like values
response = requests.get('http://rahulshettyacademy.com',cookies=cookie)
#301,200
#print(response.history)
print(response.status_code)


#Cookie can be stored in session and can be used in multiple requests
se = requests.session()
se.cookies.update({'visit-month':'February'})

res = se.get("https://httpbin.org/cookies",cookies={'visit-year':'2022'})
print(res.text)










