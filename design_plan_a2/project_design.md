## Design Document

### frontend.py 
### Handles http requests from the brower and renders the html templates (frontend)

#### Methods

| Method Name | Route | Description |
|-------------|:-----:|-------------|
| register_get | /register - get | renders the register.html template if the user is not logged in |
| register_post | /register - post | registers a user in the database, sets the account balance to 5000 and redirects to the /login page if there are no errors in the information given |
| login_get | /login - get | renders the login.html only when the user is not logged in |
| login_post | /login - post  | changes the session to 'logged_in' and redirects to home if the user input is correct and the there are no errors |
| logout | /logout | FOR GRAEME |
| authenticate | N/A | FOR GRAEME |
| profile | / |  FOR GRAEME |

-- ADD ANY METHODS YOU ADDED TO frontend.py --

### backend.py
### Handles interactions with the database (backend)

#### Methods

| Method Name | Parameter | Description |
|-------------|:---------:|-------------|
| get_user | email | gets the user object with the specified email from the database |
| login_user | email, password | gets the user object given the email and password if password-hash maches password in database, returning None otherwise |
| register_user | email, name, password, password2 | creates a new user instance in the database with the specified email, user name and password and creates a new account instance in the database with the specified email and a balance of 5000.00 |
| get_all_tickets | N/A | FOR GRAEME |

-- ADD ANY METHODS YOU ADDED TO backend.py --

### Models
### The classes stored in the database

| Model Name | Variables/Columns | Description |
|------------|:-----------------:|-------------|
| User | id, email, password, name | defines a sql table that represents a person's account information on the website |
| Account_Balance | id, email, balance | defines a sql table that represents a person's account balance on the website |

-- ADD ANY MODELS YOU ADDED TO models.py --