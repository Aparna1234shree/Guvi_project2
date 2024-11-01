"""
pages/forgot_password_page.py

This module contains the ForgotPasswordPage class, which provides methods for interacting with the "Forgot Password"
page of the OrangeHRM application. It includes functionality for entering a username, clicking the reset button,
canceling the process, and retrieving relevant messages.

Purpose:
- To encapsulate the actions that can be performed on the forgot password page, facilitating test automation
  for the forgot password functionalities.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_test import ForgotPasswordPageLocators


class ForgotPasswordPage:
    def __init__(self, driver):
        """Initialize the ForgotPasswordPage with the given WebDriver instance.

                Args:
                    driver: A Selenium WebDriver instance used to interact with the web page.
                """
        self.driver = driver

    def enter_username(self, username):
        """Enter the username in the username field.

                This method waits for the username field to be present and inputs the provided username.

                Args:
                    username: The username to be entered in the forgot password field.
                """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ForgotPasswordPageLocators.USERNAME_FIELD)
        ).send_keys(username)

    def click_reset(self):
        """Click the 'Reset' button.

        This method waits for the reset button to be clickable and then clicks it.
        """

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.RESET_BUTTON)
        ).click()

    def click_cancel(self):
        """Click the 'Cancel' button.

        This method waits for the cancel button to be clickable and then clicks it.
        """

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.CANCEL_BUTTON)
        ).click()

    def get_required_error_message(self):
        """Retrieve the required error message.

               This method waits for the required error message element to be present and returns its text.

               Returns:
                   str: The text of the required error message.
               """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ForgotPasswordPageLocators.REQUIRED_ERROR_MESSAGE)
        ).text

    def get_success_message(self):
        """Retrieve the success message after a successful reset request.

                This method waits for the success message element to be visible and returns its text.

                Returns:
                    str: The text of the success message.
                """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ForgotPasswordPageLocators.SUCCESS_MESSAGE)
        ).text
