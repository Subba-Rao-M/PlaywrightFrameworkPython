from playwright.sync_api import Playwright

loginPayLoad = {"userEmail": "subbaraw@gmail.com", "userPassword": "Span@1234"}
ordersPayLoad = {"orders":[{"country":"India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}

class APIUtils:

    def gettoken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        loginresponse = api_request_context.post("/api/ecom/auth/login",
                                                 data=loginPayLoad,
                                                 headers={"Content-Type": "application/json"}
                                                 )
        assert loginresponse.ok
        print(loginresponse.json()) #IN python json is like dictionary
        respnsebody = loginresponse.json()
        token = respnsebody["token"]
        return token

    def createorder(self, playwright: Playwright):
        token = self.gettoken(playwright)
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        orderresponse = api_request_context.post("/api/ecom/order/create-order",
                                 data=ordersPayLoad,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"
                                          }
                                 )
        print(orderresponse.json())
        respnsebody = orderresponse.json()
        orderid = respnsebody["orders"][0] #fetch the first value from list
        return orderid