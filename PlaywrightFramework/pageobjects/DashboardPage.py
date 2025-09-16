from playwright.sync_api import Page
from PlaywrightFramework.pageobjects.OrderHistoryPage import OrderHistoryPage


class DashboardPage:
    """Page Object for the Dashboard Page."""

    def __init__(self, page: Page):
        self.page = page
        # Define locators once for reusability
        self.orders_button = self.page.get_by_role("button", name="ORDERS")

    def navigate_to_orders_page(self) -> OrderHistoryPage:
        """Navigate to the Orders page and return the OrderHistoryPage object."""
        self.orders_button.click()
        return OrderHistoryPage(self.page)
