# Selenium Automation Project

## Overview

This project implements automated testing for a web application using Selenium and Python. It includes modules for handling login, admin functionalities, and password recovery, along with utility functions for Excel file management. The goal is to ensure the application's functionality through a series of automated tests.

## Table of Contents

- [Requirements](#requirements)
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Test cases](#test-cases)

## Requirements

- Python 3.x
- Selenium
- openpyxl
- pytest-html
- pytest
- webdriver-manager

## Prerequisites

1. **Python Installation**: Ensure Python 3.x is installed on your system.
2. **WebDriver**: Download the appropriate WebDriver for your browser (e.g., [ChromeDriver](https://chromedriver.chromium.org/downloads) for Chrome). Ensure it's accessible in your system's PATH.

## Features
- **Page Object Model (POM)** for modular and reusable components.
- **Data-Driven Testing (DDTF)** using excel file for multiple test cases. 
- Exception Handling and Explicit Waits instead of time.sleep().
- **Detailed Test Report** generated with pytest-html.
- **Screenshots** of test cases saved in case of failure for debugging.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   
## Usage
Open the project in your preferred IDE (e.g., PyCharm, VSCode).

_Run the tests using the following command:_

   ```bash
   pytest -v
   ```

* -v means verbose

_To get a HTML report , run using the following command:_
   ```bash
    pytest test/test_main.py --html=reports/reports.html --self-contained-html
```
* Runs the tests located in test/test_main.py.
* Generates an HTML report named report.html inside a reports folder (the folder will be created if it doesn’t exist).
* Uses --self-contained-html to make the report standalone, embedding all necessary resources (like CSS) within it.
* Modify the configurations in the test files as necessary for your specific testing scenarios.


## Project Structure

**Guvi_project2/**

1. locators/
   * locators_test.py
   * __init__.py

2. pages/
   * admin_page.py
   * login_page.py
   * forgot_password_page.py

3. utils/
   * excel_functions.py

4. tests/
   *   test_main.py
   * __init__.py

5. data/
    * test_plan.xlsx
   
6. reports
    * reports.html
   
7. screenshots

* requirements.txt
* README.md
* cmd_screen_shot.png (screenshot of command prompt)

## Test Cases
1. [TC_01 : Empty Username for Password Reset](#tc_01-empty-username-for-password-reset)
2. [TC_02 : Valid Username for Password Reset](#tc_02-valid-username-for-password-reset)
3. [TC_03 : Cancel Button in Password Reset](#tc_03-cancel-button-in-password-reset)
4. [TC_04 : Validate Admin Page Title (Positive)](#tc_04-validate-admin-page-title-positive)
5. [TC_05 : Validate Admin Page Title (Negative)](#tc_05-validate-admin-page-title-negative)
6. [TC_06 : Validate Visible Options in Admin Module](#tc_06-validate-visible-options-in-admin-module)
7. [TC_07 : Validate Absence of Leave Option](#tc_07-validate-absence-of-leave-option)
8. [TC_08 : Validate Visible Side Menu Options](#tc_08-validate-visible-side-menu-options)
9. [TC_09 : Validate Invisible Options](#tc_09-validate-invisible-options)

### TC_01 : Empty Username for Password Reset
- **Description**: Verify the error message when attempting to reset password with an empty username.
- **Precondition**: User is on the login page.
- **Steps**:
  1. Click on the "Forgot Password" link.
  2. Click on the "Reset" button without entering a username.
- **Expected Result**: "Required" error message is displayed.
- **Postcondition**: Record result in Excel; capture screenshot if test fails.

---

### TC_02 : Valid Username for Password Reset
- **Description**: Verify the behavior when a valid username is provided for password reset.
- **Precondition**: User is on the "Forgot Password" page.
- **Steps**:
  1. Click on the "Forgot Password" link.
  2. Enter "Admin" as the username.
  3. Click on the "Reset" button.
- **Expected Result**: "Reset Password link sent successfully" message is displayed.
- **Postcondition**: Record result in Excel.

---

### TC_03 : Cancel Button in Password Reset
- **Description**: Verify that clicking the "Cancel" button redirects back to the login page.
- **Precondition**: User is on the "Forgot Password" page.
- **Steps**:
  1. Click on the "Forgot Password" link.
  2. Click on the "Cancel" button.
- **Expected Result**: User is redirected to the main login page.
- **Postcondition**: Record result in Excel.

---

### TC_04 : Validate Admin Page Title (Positive)
- **Description**: Verify the title of the Admin page upon successful login.
- **Precondition**: User is on the login page.
- **Steps**:
  1. Log in with valid credentials ("Admin", "admin123").
  2. Navigate to the "Admin" module.
  3. Verify the title.
- **Expected Result**: Title should be "OrangeHRM".
- **Postcondition**: Record result in Excel; capture screenshot if test pass/fails.

---

### TC_05 : Validate Admin Page Title (Negative)
- **Description**: Verify that the Admin page title does not match an incorrect value.
- **Precondition**: User is on the login page.
- **Steps**:
  1. Log in with valid credentials ("Admin", "admin123").
  2. Navigate to the "Admin" module.
  3. Verify the title.
- **Expected Result**: Title should not be "orangehrm".
- **Postcondition**: Record result in Excel; capture screenshot if test pass/fails.

---

### TC_06 : Validate Visible Options in Admin Module
- **Description**: Verify that all expected options are visible in the Admin module.
- **Precondition**: User is on the Admin page.
- **Steps**:
  1. Log in and navigate to the Admin module.
  2. Verify the presence of each expected option (User Management, Job, Organization, Qualifications, Nationalities, Corporate Branding, Configuration).
- **Expected Result**: All expected options are visible.
- **Postcondition**: Record result in Excel; capture screenshot if test pass/fails.

---

### TC_07 : Validate Absence of Leave Option
- **Description**: Verify that the "Leave" option is not visible in the Admin module.
- **Precondition**: User is on the Admin page.
- **Steps**:
  1. Log in and navigate to the Admin module.
  2. Check for the absence of the "Leave" option.
- **Expected Result**: "Leave" option should not be visible.
- **Postcondition**: Record result in Excel; capture screenshot if test pass/fails.

---

### TC_08 : Validate Visible Side Menu Options
- **Description**: Verify that all expected options are visible in the Admin module's side menu.
- **Precondition**: User is on the Admin page.
- **Steps**:
  1. Log in and navigate to the Admin module.
  2. Verify the presence of each expected option in the side menu (Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard, Directory, Maintenance, Buzz).
- **Expected Result**: All expected options are visible in the side menu.
- **Postcondition**: Record result in Excel; capture screenshot if test pass/fails.

---

### TC_09 : Validate Invisible Options
- **Description**: Verify that a nonexistent option ("Nonexistent Option") is not visible in the Admin module.
- **Precondition**: User is on the Admin page.
- **Steps**:
  1. Log in and navigate to the Admin module.
  2. Verify that the "Nonexistent Option" is not visible.
- **Expected Result**: "Nonexistent Option" should not be visible.
- **Postcondition**: Record result in Excel; capture screenshot if test pass/fails.

---

**Note**: Each test captures screenshots upon failure, and results are recorded in an Excel file as specified.