from playwright.sync_api import Playwright

# Define reusable payload for order creation
ORDERS_PAYLOAD = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "68a961719320a140fe1ca57c"
        }
    ]
}


class ApiUtils:
    """Utility class for handling API interactions with the backend."""

    def get_token(self, playwright: Playwright, user_credentials: dict) -> str:
        """
        Authenticates a user and retrieves an access token using the login API.

        Args:
            playwright (Playwright): The Playwright instance.
            user_credentials (dict): Dictionary containing user_email and user_password.

        Returns:
            str: JWT token for authenticated API requests.
        """
        # Create a new API request context
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        # Extract user credentials
        user_email = user_credentials["user_email"]
        user_password = user_credentials["user_password"]

        # Perform login request
        login_response = api_context.post(
            "/api/ecom/auth/login",
            data={
                "userEmail": user_email,
                "userPassword": user_password
            },
            headers={"Content-Type": "application/json"}
        )

        # Assert login was successful
        assert login_response.ok, "❌ Login API failed."

        # Parse response and extract token
        response_body = login_response.json()
        print(f"✅ Login successful. Token: {response_body['token']}")
        return response_body["token"]

    def create_order(self, playwright: Playwright, user_credentials: dict) -> str:
        """
        Creates an order using the authenticated token and returns the order ID.

        Args:
            playwright (Playwright): The Playwright instance.
            user_credentials (dict): Dictionary containing user_email and user_password.

        Returns:
            str: ID of the created order.
        """
        # Step 1: Get user token
        token = self.get_token(playwright, user_credentials)

        # Step 2: Create new API context and send order request
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        order_response = api_context.post(
            "/api/ecom/order/create-order",
            data=ORDERS_PAYLOAD,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )

        assert order_response.ok, "❌ Order creation API failed."

        # Step 3: Extract and return the order ID
        response_body = order_response.json()
        print(f"✅ Order created. Order ID: {response_body['orders'][0]}")
        return response_body["orders"][0]
