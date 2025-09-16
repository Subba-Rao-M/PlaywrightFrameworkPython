from playwright.sync_api import Page, expect


class OrderDetailsPage:
    """Page Object for the Order Details page."""

    def __init__(self, page: Page):
        self.page = page
        self.order_message = self.page.locator(".tagline")

    def verify_order_message(self) -> None:
        """Verify that the order confirmation message is displayed."""
        expect(self.order_message).to_contain_text("Thank you for Shopping With Us")
