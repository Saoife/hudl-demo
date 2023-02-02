I tried to keep this to around 3-4 hours total so here's some areas I think could be improved with more time:

- Separate element locators from functions in each page class, right now they're all combined and adding multiple functions for a single element is going to cause repetition
- Set webdriver timeout and browser from a config file instead of hardcoding them
- Move test data (email and password) into another class to cut down on blocks of text in the steps file
- Add a class to handle keyboard inputs instead of doing it in the steps
- More scenarios :)