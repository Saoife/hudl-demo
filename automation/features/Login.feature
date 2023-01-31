Feature: Login page

Background:
Given the user is on the login page

Scenario: User can login
    When the user attempts to login with the correct details
    Then the home page is displayed

Scenario Outline: User must provide an email and password
    When the user attempts to login providing only the <input>
    Then the user is not logged in
    And an error message is displayed

    Examples:
        | input    |
        | email    |
        | password |

Scenario Outline: User cannot login with incorrect details
    When the user attempts to login providing an incorrect <input>
    Then the user is not logged in
    And an error message is displayed

    Examples:
        | input    |
        | email    |
        | password |

Scenario: User can navigate through the page using the keyboard only

Scenario: XSS is not possible for text inputs