# Usage

## Requirements
- Chrome Webdriver for your current browser version (https://chromedriver.chromium.org/downloads)
- Python 3.* (https://www.python.org/downloads/)
- Behave (after installing python, run `pip install behave`)
- Selenium (after installing python, run `pip install selenium`)

## Running the tests
To run all the tests in the project, navigate to the automation folder and run the command `behave`

To run only certain tagged scenarios, run `behave -t "@tag"`

# Adding tests

## Adding features
New feature files should be added in the `features` folder and each feature file should have an equivalent steps class in the `steps` folder

## Page object model
Each page of the app should have its own class containing selectors and functions for that page, e.g. the login page has a class `pages/login_page.py` containing selectors for each element on the page and functions for navigating through the page

## Best practices
- Try to keep the code in each step as short as possible, if you find yourself repeating the same code over in multiple steps then this can probably be moved out into the relevant page class
- When writing scenarios, check if there's another scenario that uses the same steps so they can be reused
- When writing selectors for elements, try to use element and automation IDs over css styling classes
- Where possible, only load the browser once for each feature, this greatly speeds up execution of the tests. This is not possible though for some features that need the browser to be in a clean state for each scenario