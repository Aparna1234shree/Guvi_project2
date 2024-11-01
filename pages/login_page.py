"""
pages/login_page.py

This module contains the LoginPage class, which provides methods for interacting with the login page of the OrangeHRM application.
The class includes functionality for logging in, as well as handling the 'Forgot Password' link.

Purpose:
- To encapsulate the actions that can be performed on the login page, facilitating test automation for login functionalities.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_test import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        """Initialize the LoginPage with the given WebDriver instance.

               Args:
                   driver: A Selenium WebDriver instance used to interact with the web page.
               """
        self.driver = driver

    def login(self, username, password):
        """Perform login action using the provided username and password.

        This method waits for the username and password fields to be present, enters the credentials,
        and then clicks the login button.

        Args:
            username: The username to be entered in the login field.
            password: The password to be entered in the password field.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.USERNAME_FIELD)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

    def click_forgot_password(self):
        """Click on the 'Forgot Password' link.

               This method waits for the 'Forgot Password' link to be clickable and then clicks it.
               """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        ).click()
