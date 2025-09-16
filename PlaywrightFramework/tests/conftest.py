import pytest

# All global configuration items passed from terminals or run time should be added here
# These options allow us to dynamically pass browser type and base URL when running tests
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",  # Command-line argument name
        action="store",    # Store the value in config
        default="chrome",  # Default value if not specified
        help="browser selection: chrome or firefox"
    )
    parser.addoption(
        "--url_name",
        action="store",
        default="https://rahulshettyacademy.com/client",
        help="server selection: default is production URL"
    )


# This fixture is used to fetch test data via parametrize (like credentials list from a JSON)
# It runs once per test iteration and returns the current test case's data (user_credentials)
# Used with: @pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param  # Access the parameter passed from @pytest.mark.parametrize


# This fixture provides a new browser page for each test
# Removed session scope to allow **fresh page instance per test**, useful when running multiple tests
# This ensures test isolation and prevents issues caused by session reuse
@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("browser_name")  # --browser_name firefox
    url_name = request.config.getoption("url_name")           # --url_name https://staging-url.com

    # Browser selection based on CLI input
    if browser_name == "chrome":
        browser = playwright.chromium.launch()  # Set headless=False for visible execution
    elif browser_name == "firefox":
        browser = playwright.firefox.launch()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}. Use 'chrome' or 'firefox'.")

    # Create isolated browser context and new page for test
    context = browser.new_context()
    page = context.new_page()

    # Optional: navigate to base URL here if desired (currently handled inside test or page object)
    # page.goto(url_name)

    yield page  # Provide the page object to the test case

    # Clean up resources after test completes
    context.close()
    browser.close()


# --------------------------------------------
# ✅ HOW TO USE THESE OPTIONS FROM TERMINAL
# --------------------------------------------

# Run a specific test case in Firefox browser:
# ▶ pytest PlaywrightFramework/tests/TestCase_01_E2E_WebApiTesting.py --browser_name firefox

# Run all tests with custom base URL and browser:
# ▶ pytest --browser_name chrome --url_name https://staging.rahulshettyacademy.com

# Run all tests with tags like smoke or regression
# ▶ pytest -m smoke

# Run all tests with keywords used in test case name
# ▶ pytest -k Api

# Run all tests with parallel mode
# ▶ pip install pytest-xdist
# ▶ pytest -n 3 # 3 tests in parallel


# Generate html report
# ▶ pip install pytest-html
# ▶ pytest -n 2 --html=reports.html

# playwright trace viewer
# ▶ pytest --browser_name chrome -n 2 --tracing on --html=reports.html
# go to trace.playwright.dev site and upload the file to view the traces
# use retain on failure in place of on above for only failed tracing

# To install pytest-bdd for bdd framework
# pip install pytest-bdd