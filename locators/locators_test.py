"""
locators/locators.test.py

This module contains locator definitions for the various elements 
in the login and admin pages of the OrangeHRM application. 
Using Selenium's By class, locators are defined for easy access 
to web elements during automation testing.
"""
from selenium.webdriver.common.by import By

class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")

class ForgotPasswordPageLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    RESET_BUTTON = (By.XPATH, "//button[contains(@class, 'orangehrm-forgot-password-button--reset')]")
    REQUIRED_ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'oxd-input-field-error-message')]")
    SUCCESS_MESSAGE = (By.XPATH, "//h6[normalize-space()='Reset Password link sent successfully']")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(@class, 'orangehrm-forgot-password-button--cancel')]")

class AdminPageLocators:
    ADMIN_TAB = (By.XPATH, "//span[text()='Admin']")