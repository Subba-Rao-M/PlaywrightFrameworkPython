from playwright.sync_api import Page
from PlaywrightFramework.pageobjects.OrderDetailsPage import OrderDetailsPage


class OrderHistoryPage:
    """Page Object for the Order History page."""

    def __init__(self, page: Page):
        self.page = page

    def click_view_for_order_id(self, order_id: str) -> OrderDetailsPage:
        """
        Clicks the 'View' button for the given order ID and navigates to the Order Details page.

        Args:
            order_id (str): The order ID to find in the order history table.

        Returns:
            OrderDetailsPage: The page object representing the Order Details page.
        """
        row = self.page.locator("tr").filter(has_text=order_id)
        view_button = row.get_by_role("button", name="View")
        view_button.click()
        return OrderDetailsPage(self.page)
