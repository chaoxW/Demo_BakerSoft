# 1. Test cases
- Check the registration link exists (**Priority Blocker**, from user's perspective it is critical the link should exist)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. the registration link is existed  

- Click registration link then sign up form shown (**Priority Blocker**, from user's perspective it is critical the form should exist)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown

- Click register button when the form is empty (**Priority High**, if the user misclick but the form not filled correctly there should be the error message)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown
  3. click the register button --> error message shown to insert all the mandatory input

- Register new user with correct values (**Priority High**, it is the critical positive coverage)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown
  3. insert all the input with correct values
  4. click the register button --> registration is successful

- Register new user with incorrect values (**Priority High**, if the valus type is incorrect there should be the error message)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown
  3. insert first name with numbers, special characters --> the error message should be shown
  4. insert last name with numbers, special characters --> the error message should be shown
  5. insert city with numbers, special characters --> the error message should be shown
  6. insert zip code with letters, special characters, incorrect length of numbers --> the error message should be shown
  7. insert phone number with letters, special characters, incorrect length of numbers --> the error message should be shown
  8. insert username with special characters --> the error message should be shown
  9. insert password with unacceptable length, missing mandatory characters --> the error message should be shown

# 2. Automation tests folder structure
- ## Selenium4, Python, Pytest to build the automation test framework
#### Run test with `pytest Tests/test_LoginPage.py -v --html=./report.html` from command 
#### You can watch the demo1.mov and demo2.mov to see the test execution and test report 

    
    ├── Config
    │   ├── __init__.py
    │   │   └── initiation
    │   ├── config.py
    │   │   └── Manage the class TestData
    ├── Pages
    │   ├── __init__.py
    │   │   └── initiation
    │   ├── BasePage.py
    │   │   └── manage general method (click, send keys, is_visible ect)
    │   ├── LoginPage.py
    │   │   └── manage the method specific for the login page
    ├── Test
    │   ├── __init__.py
    │   │   └── initiation
    │   ├── conftest.py
    │   │   └── webdriver initiation
    │   ├── test_base.py
    │   │   └── call the driver
    │   └── test_LoginPage.py
    │       └── manage the tests for the login page
    ├── report.html
    │   └── test report
    ├── docker-compose.yml
    ├── dockerfile
    └── requirements.txt
    
# 3. Automation tests 
### the tests automated should be always repeatable and guarantee there is no regression issue, we should make automation tests as much as possible to increase the test coverage for the product
    
- test_signup_link_visible
- test_login_page_title
- test_signup_form_visible
- test_signup_form_errors
- test_login_error

# 4. Report bug with old documentation

Hello Developer  
Currently I am testing the registration form, I may find an issue and I want to confirm with you
The issue is that the zipcode input which could accept the *letters, special characters, incorrect length of numbers* as input, I have already checked the documentation we have but I do not find relevant
information about this input restriction  
Here are the steps to reproduce the issue
- Register new user with incorrect values (**Priority High**, if the valus type is incorrect there should be the error message)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown
  3. insert zip code with letters, special characters, incorrect length of numbers --> the error message should be shown
  
If this could be the issue, we would update the current documentation and I will open a defect ticket for this, if there is anything I could help just let me know.

Many thanks  
Shuai
