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
| logout | /logout | Logsout the user and redirects them to the login page. |
| sell_post | /sell | This function posts all of the information in the sell form and creates a new ticket |
| buy_post | /buy | This function posts all of the information in the buy form and buys a ticket |
| update_post | /update | This function posts all of the information in the update form and updates the corresponding ticket |
| authenticate | N/A | Wrap any python function and check the current session to see if the user has logged in. If login, it will call the inner_function with the logged in user object. |
| profile | / |  Renders index.html with all availible tickcets and the account balance |
| page_not_found | '/<path:text>' | Returns the 404 error page when a non defined path is entered |


### backend.py
### Handles interactions with the database (backend)

#### Methods

| Method Name | Parameter | Description |
|-------------|:---------:|-------------|
| get_user | email | gets the user object with the specified email from the database |
| login_user | email, password | gets the user object given the email and password if password-hash maches password in database, returning None otherwise |
| register_user | email, name, password, password2 | creates a new user instance in the database with the specified email, user name and password and creates a new account instance in the database with the specified email and a balance of 5000.00 |
| get_all_tickets | N/A | This function returns all of the availible tickets for sale according to the current date |
| sell_ticket | owner, name, quantity, price, date | This function creates a ticket in the database that is to be sold |
| buy_ticket | name, quantity | This function purchases a ticket and updates the database for that ticket |
| update_ticket | owner, name, quantity, price, date | This function updates a tickets attributes in the database |
| get_account_balance| email | Get an account balance by a given email |
| set_account_balance| email, balance | Set an account balance by a given email |

### Models
### The classes stored in the database

| Model Name | Variables/Columns | Description |
|------------|:-----------------:|-------------|
| User | id, email, password, name | defines a sql table that represents a person's account information on the website |
| Account_Balance | id, email, balance | defines a sql table that represents a person's account balance on the website |
| Account_Balance | id, owner, name, quantity, price, date | defines a sql table that represents an availible ticket being sold |

