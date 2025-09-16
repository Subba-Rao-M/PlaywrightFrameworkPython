from playwright.sync_api import Page
from PlaywrightFramework.pageobjects.DashboardPage import DashboardPage


class LoginPage:
    """Page Object Model for the Login Page."""

    def __init__(self, page: Page):
        self.page = page
        # Define locators once for reuse
        self.email_input = page.get_by_placeholder("email@example.co")
        self.password_input = page.get_by_placeholder("enter your passsword")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto("https://rahulshettyacademy.com/client")

    def do_login(self, username: str, password: str) -> DashboardPage:
        """Log in using provided credentials and return DashboardPage object."""
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return DashboardPage(self.page)
