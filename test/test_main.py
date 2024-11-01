"""
test/test_main.py
"""
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.admin_page import AdminPage
from selenium.webdriver.common.by import By  # Import By
from utils.excel_functions import ExcelFunctions
from datetime import datetime
import os
def capture_screenshot(driver, prefix):
    """Captures a screenshot with a timestamp."""
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)  # Create screenshots directory if it doesn't exist
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Generate a timestamp for uniqueness
    screenshot_path = os.path.join(screenshot_dir, f"{prefix}_{timestamp}.png")  # Define screenshot path
    driver.save_screenshot(screenshot_path)  # Save screenshot
    print(f"Screenshot saved at: {screenshot_path}")  # Log the screenshot path

class TestOrangeHRM:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Open the browser in full window mode
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Initialize page objects and other dependencies
        self.login_page = LoginPage(self.driver)
        self.forgot_password_page = ForgotPasswordPage(self.driver)
        self.admin_page = AdminPage(self.driver)
        self.excel = ExcelFunctions("data/test_plan.xlsx", "Sheet1")

        yield  # This will run the test

        # Teardown: close the browser after tests
        self.driver.quit()

    def test_tc_01_empty_username(self):
        """Tests the behavior when attempting to reset password with an empty username."""

        # Click on Forgot Password link
        self.login_page.click_forgot_password()

        # Click on Reset button without entering username
        self.forgot_password_page.click_reset()

        # Verify "Required" error message
        error_message = self.forgot_password_page.get_required_error_message()
        assert error_message == "Required"

        # Take screenshot if test fails
        if error_message != "Required":
            self.excel.write_data(2, 6, "Fail")
        else:
            capture_screenshot(self.driver, "TC_01_empty_username")
            self.excel.write_data(2, 6, "Pass")

    def test_tc_02_valid_username(self):
        """Tests the behavior when a valid username is provided for password reset."""

        # Click on Forgot Password link
        self.login_page.click_forgot_password()

        # Enter valid username and click Reset button
        self.forgot_password_page.enter_username("Admin")
        self.forgot_password_page.click_reset()

        # Verify success message
        success_message = self.forgot_password_page.get_success_message()
        assert success_message == "Reset Password link sent successfully"
        capture_screenshot(self.driver, "TC_02_valid_username")

        # Record test result
        self.excel.write_data(3, 6, "Pass" if success_message == "Reset Password link sent successfully" else "Fail")

    def test_tc_03_cancel_button(self):
        """Tests the cancel functionality in the forgot password workflow."""

        # Click on Forgot Password link
        self.login_page.click_forgot_password()

        # Click on Cancel button
        self.forgot_password_page.click_cancel()
        capture_screenshot(self.driver, "TC_03_cliked cancel")

        # Verify redirection to the main login page
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.excel.write_data(4, 6,
                              "Pass" if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" else "Fail")

    def test_tc_04_validate_admin_title_positive(self):
        """Tests if the title of the Admin page is correct upon login."""

        # Login with valid credentials and navigate to Admin module
        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()
        actual_title = self.admin_page.get_title()
        expected_title = "OrangeHRM"

        # Validate and record the result
        if actual_title == expected_title:
            self.excel.write_data(5, 6, "Pass")
        else:
            capture_screenshot(self.driver, "TC_04_valid_title")
            self.excel.write_data(5, 6, "Fail")
        assert actual_title == expected_title

    def test_tc_05_validate_admin_title_negative(self):
        """Tests that the Admin page title does not match an incorrect value."""

        # Login with valid credentials and navigate to Admin module
        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()
        actual_title = self.admin_page.get_title()
        expected_title = "orangehrm"  # Incorrect title for negative test

        # Validate and record the result
        if actual_title != expected_title:
            self.excel.write_data(6, 6, "Pass")
        else:
            capture_screenshot(self.driver, "TC_05_invalid_title")
            self.excel.write_data(6, 6, "Fail")
        assert actual_title != expected_title

    def test_tc_06_validate_visible_options(self):
        """Verifies that all expected options are visible in the Admin module."""

        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()

        # List of expected visible options
        expected_options = [
            "User Management",
            "Job",
            "Organization",
            "Qualifications",
            "Nationalities",
            "Corporate Branding",
            "Configuration"
        ]

        actual_options = []

        # Loop through each expected option and use explicit waits to check visibility
        for option in expected_options:
            # Define an XPath for each expected option
            option_xpath = f"//nav/ul/li[span[contains(text(), '{option}')]] | //nav/ul/li[a[contains(text(), '{option}')]]"

            # Use get_element_text to fetch the text if the element is visible
            option_text = self.admin_page.get_element_text(option_xpath)
            if option_text:  # Only add to the list if text is found
                actual_options.append(option_text.strip())

        print("Actual options:", actual_options)  # Debugging output
        print("Expected options:", expected_options)  # Debugging output
        if actual_options == expected_options:
            self.excel.write_data(7, 6, "Pass")  # Update row 5, column 6 for test case 6

        else:
            self.excel.write_data(7, 6, "Fail")  # Update row 5, column 6 for test case 6
            assert actual_options == expected_options, f"Expected options '{expected_options}' but found '{actual_options}'"
        # Check if the actual options match the expected options
        capture_screenshot(self.driver, "TC_06_admin menu_options")
        assert actual_options == expected_options, f"Expected options '{expected_options}' but found '{actual_options}'"

    def test_tc_07_validate_leave_option(self):
        """Verifies that the Leave option is not visible in the Admin module."""

        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()
        # Check that the "Leave" option is not visible
        leave_xpath = "/html/body/div/div/div/header/div[2]/nav/ul/li[9]/span"  # Adjust the index if needed
        leave_visible = self.admin_page.get_element_text(leave_xpath)
        if not leave_visible:
            self.excel.write_data(8, 6, "Pass")  # Update row 6, column 6 for test case 7
        else:
            self.excel.write_data(8, 6, "Fail")  # Update row 6, column 6 for test case 7
            capture_screenshot(self.driver, "TC_07_leave_option_visible")

        assert not self.admin_page.get_element_text(leave_xpath), "Leave option should not be visible"

    def test_tc_08_validate_visible_options(self):
        """Verifies that all expected options are visible in the side menu of the Admin module."""

        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()

        # List of expected visible options
        expected_side_menu = [
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Buzz"
        ]

        actual_side_menu = self.admin_page.validate_visible_options(expected_side_menu)
        print("Actual visible options:", actual_side_menu)

        # Check if the actual options match the expected options
        if sorted(actual_side_menu) == sorted(expected_side_menu):
            self.excel.write_data(9, 6, "Pass")
        else:
            self.excel.write_data(9, 6, "Fail")
        capture_screenshot(self.driver, "TC_08_visible_side_menu")
        assert sorted(actual_side_menu) == sorted(expected_side_menu), f"Expected options '{expected_side_menu}' but found '{actual_side_menu}'"


    def test_tc_09_validate_invisible_options(self):
        """Verifies that a nonexistent option is not visible in the Admin module."""

        self.login_page.login("Admin", "admin123")
        self.admin_page.navigate_to_admin()

        # List of expected visible options including an option that should not be visible
        expected_menu = [
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Buzz",
            "Nonexistent Option"  # This option does not exist, simulating a negative case
        ]

        # Call the method to validate visible options
        actual_menu = self.admin_page.validate_visible_options(expected_menu)
        print("Actual visible options:", actual_menu)

        # Define the expected negative condition: "Nonexistent Option" should not be in the actual options
        assert "Nonexistent Option" not in actual_menu, (
            f"Expected 'Nonexistent Option' to be invisible, but it was found in: {actual_menu}"
        )

        # Log result in Excel for this negative test case
        if "Nonexistent Option" not in actual_menu:
            self.excel.write_data(10, 6, "Pass")  # Update row number accordingly
        else:
            self.excel.write_data(10, 6, "Fail")
            capture_screenshot(self.driver, "TC_09_invisible_option")
