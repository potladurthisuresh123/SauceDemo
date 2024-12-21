from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
import time
import os


# Senario: 1 Successful Login
@given("I am on the Demo Login Page")
def step_open_login_page(context):
    context.driver = webdriver.Chrome()  # Replace with your browser driver
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account "{username}" into the Username field and the Password field')
def step_fill_login_form(context, username):
    credentials = {
        "standard_user": "secret_sauce",
        "locked_out_user": "secret_sauce"
    }
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(credentials[username])

@when("I click the Login Button")
def step_click_login_button(context):
    context.driver.find_element(By.ID, "login-button").click()

@then("I am redirected to the Demo Main Page")
def step_verify_main_page(context):
    assert "inventory.html" in context.driver.current_url

@then("I verify the App Logo exists")
def step_verify_logo(context):
    assert context.driver.find_element(By.CLASS_NAME, "app_logo").is_displayed()

# Senario: 2 Failed Login
@then('I verify the Error Message contains the text "Sorry, this user has been banned."')
def step_verify_error_message(context):
    error_message = context.driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Sorry, this user has been locked out." in error_message

# Senario: 3 Extract Data
@given('I am logged in')
def step_impl(context):
    # Navigate to the login page
    context.driver.get('https://www.saucedemo.com/')

    # Find and enter username and password, then click login button
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID, 'login-button').click()

    # Ensure we are on the inventory page after logging in
    assert "inventory" in context.driver.current_url, f"Failed to log in. Current URL: {context.driver.current_url}"


# steps/inventory_steps.py
from selenium.webdriver.common.by import By
from behave import when, then
import time


@when('I am on the inventory page')
def step_impl(context):
    # Ensure we are on the inventory page
    assert "inventory" in context.driver.current_url, f"Current URL is not the inventory page. URL: {context.driver.current_url}"


@then('I extract content from the web page')
def step_impl(context):
    # Extract data from the inventory page (e.g., item names)
    items = context.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    # Save the extracted data in the context object for later use
    context.extracted_content = [item.text for item in items]
    print(f"Extracted items: {context.extracted_content}")


@then('Save it to a text file')
def step_impl(context):
    # Save the extracted data to a text file
    if not hasattr(context, 'extracted_content') or not context.extracted_content:
        raise Exception("No content to save. Ensure content is extracted first.")

    with open("extracted_inventory.txt", "w") as file:
        for item in context.extracted_content:
            file.write(item + "\n")

    print("Data has been saved to extracted_inventory.txt")


@then("I log out")
def step_log_out(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "logout_sidebar_link").click()

@then("I verify I am on the Login page again")
def step_verify_logout(context):
    assert "login.html" in context.driver.current_url

def after_all(context):
    context.driver.quit()
