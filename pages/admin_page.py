"""
pages/admin_page.py

This module contains the AdminPage class, which defines methods for interacting with the Admin page of the OrangeHRM application.
The methods include navigation to the Admin section, retrieving the page title, checking element visibility, fetching element text, 
and validating the visibility of expected options in the Admin menu.

Purpose:
- To provide a clear and reusable interface for test automation on the Admin page of the OrangeHRM application.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from locators.locators_test import AdminPageLocators

class AdminPage:
    def __init__(self, driver):
        """Initialize the AdminPage with the given WebDriver instance.

        Args:
            driver: A Selenium WebDriver instance used to interact with the web page.
        """
        self.driver = driver

    def navigate_to_admin(self):
        """Navigate to the Admin tab.

         This method waits for the Admin tab to become clickable, then clicks it to navigate to the Admin section.
         It also waits for the URL to contain the expected path to confirm successful navigation.
         """
        # Wait for the Admin tab to be clickable and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AdminPageLocators.ADMIN_TAB)
        ).click()

        # Wait for the URL to contain the expected path after navigation
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/web/index.php/admin/viewSystemUsers")
        )
    def get_title(self):
        """Get the title of the current page.

        Returns:
            str: The title of the current web page.
        """
        return self.driver.title

    def is_element_visible(self, xpath):
        """Check if an element specified by the XPath is visible on the page.

        Args:
            xpath: The XPath locator for the element to check.

        Returns:
            bool: True if the element is visible, False otherwise.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False

    def get_element_text(self, xpath):
        """Get the text of an element specified by the XPath.

        Args:
            xpath: The XPath locator for the element.

        Returns:
            str: The text of the element if found, None if not found or not visible.
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element.text  # Get the text of the element
        except Exception as e:
            print(f"Error finding element at '{xpath}': {e}")
            return None  # Return None if the element is not found or not visible

    def validate_visible_options(self, expected_options):
        """Validate the visibility of expected options in the Admin menu.

        Args:
            expected_options: A list of expected options that should be visible.

        Returns:
            list: A list of options that are actually visible on the page.
        """
        visible_options = []
        for option in expected_options:
            option_xpath = f"//span[text()='{option}'] | //a[span[text()='{option}']]"
            if self.is_element_visible(option_xpath):
                visible_options.append(option)
        return visible_options