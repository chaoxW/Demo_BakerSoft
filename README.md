# 1. Test cases
- Check the registration link exists (**Priority Highest**, from user's perspective it is critical the link should exist, it is the positive coverage)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. the registration link is existed  

- Click registration link then sign up form shown (**Priority Highest**, from user's perspective it is critical the form should exist, it is the positive coverage)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown

- Click register button when the form is empty (**Priority High**, if the user misclick but the form not filled correctly there should be the error message, it is the negative coverage)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown
  3. click the register button --> error message shown to insert all the mandatory input

- Register new user with correct values (**Priority High**, it is the critical positive coverage)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown
  3. insert all the input with correct values
  4. click the register button --> registration is successful

- Register new user with incorrect values (**Priority High**, if the valus type is incorrect there should be the error message, it is the negative coverage)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. click the registration link --> the sign up form is shown
  3. insert first name with numbers, special characters --> the error message should be shown
  4. insert last name with numbers, special characters --> the error message should be shown
  5. insert city with numbers, special characters --> the error message should be shown
  6. insert zip code with letters, special characters, incorrect length of numbers --> the error message should be shown
  7. insert phone number with letters, special characters, incorrect length of numbers --> the error message should be shown
  8. insert username with special characters --> the error message should be shown
  9. insert password with unacceptable length, missing mandatory characters --> the error message should be shown

- Login with wrong username and password (**Priority High**, it is the negative coverage)
  1. Open the [base url](https://parabank.parasoft.com/parabank/index.htm) --> the hompage is shown
  2. insert wrong username --> username inserted
  3. insert wrong password --> password inserted
  4. click the login button --> the error message should be shown

# 2. Automation tests folder structure
- ## Selenium4, Python, Pytest to build the automation test framework
- ## we can also evaluate Cypress, WebdriverIO, Playwright to build the automation test framework depends on the requirments from the product.
#### Run test with `pytest Tests/test_LoginPage.py -v --html=./report.html` from command 
#### You can watch the `demo1.mov` and `demo2.mov` to see the test execution and test report

[![Demo1](https://res.cloudinary.com/marcomontalbano/image/upload/v1673859721/video_to_markdown/images/google-drive--1di3UbU4RAerOHgCRTcN68tUl-g3gkQoT-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1di3UbU4RAerOHgCRTcN68tUl-g3gkQoT/view?usp=share_link "Demo1")

[![Demo2](https://res.cloudinary.com/marcomontalbano/image/upload/v1673859786/video_to_markdown/images/google-drive--1SOkIN7m5pYAonTLBRy28hMxuhyt6RjKT-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://drive.google.com/file/d/1SOkIN7m5pYAonTLBRy28hMxuhyt6RjKT/view?usp=share_link "Demo2")
#### You can also check the report `report.html`

<img width="1658" alt="image" src="https://user-images.githubusercontent.com/38011268/212568539-815ec183-b8a0-470a-bd48-02b9ad79e3b6.png">


    
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
