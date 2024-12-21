Feature: Login functionality and data extraction

  Scenario: Successful Login
    Given I am on the Demo Login Page
    When I fill the account information for account "standard_user" into the Username field and the Password field
    And I click the Login Button
    Then I am redirected to the Demo Main Page
    And I verify the App Logo exists

  Scenario: Failed Login
    Given I am on the Demo Login Page
    When I fill the account information for account "locked_out_user" into the Username field and the Password field
    And I click the Login Button
    Then I verify the Error Message contains the text "Sorry, this user has been banned."

  Scenario: Extract data
    Given I am logged in
    When I am on the inventory page
    Then I extract content from the web page
    And Save it to a text file
    Then I log out
    And I verify I am on the Login page again
