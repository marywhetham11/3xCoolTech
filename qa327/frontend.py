from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
import re

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder.
"""

@app.route('/register', methods=['GET'])
def register_get():
    # direct to home page if the user is logged in
    if 'logged_in' in session:
        return redirect('/')
    # templates are stored in the templates folder
    return render_template('register.html', message='')

@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    # ALL POSSIBLE ERRORS
    # email is empty
    if len(email) < 1:
        error_message = "Email format is incorrect: Cannot be empty"

    # email does not follow addr-spec defined in RFC 5322
    elif not (re.match("^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]{1,64}(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9]+(?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)$", email) and re.search("@[a-zA-Z0-9-.]{1,255}$", email)):
        error_message = "Email format is incorrect: Not a valid email"

    # password is empty
    elif len(password) < 1:
        error_message = "Password format is incorrect: Cannot be empty"

    # password is less than 6 characters
    elif len(password) < 6:
        error_message = "Password format is incorrect: Cannot be less than 6 characters"

    # password does not have an uppercase character
    elif not re.search("[A-Z]+", password):
        error_message = "Password format is incorrect: Does not contain an uppercase character"

    # password does not have a lowercase character
    elif not re.search("[a-z]+", password):
        error_message = "Password format is incorrect: Does not contain a lowercase character"

    # password does not have a special character
    elif not re.search("[\"'!@#$%^&*()-+?_=,<>/'\"]+", password):
        error_message = "Password format is incorrect: Does not contain a special character"

    # password and password2 have to be exactly the same
    elif password != password2:
        error_message = "Password format is incorrect: The passwords do not match"

    # user name is empty
    elif len(name) < 1:
        error_message = "User name format is incorrect: Cannot be empty"

    # user name is non-alphanumeric
    elif not all(x.isalnum() or x.isspace() or x == "_" for x in name):
        error_message = "User name format is incorrect: Must be alphanumeric"

    # user name has space as first character
    elif re.search("^ ", name):
        error_message = "User name format is incorrect: Cannot have space as first character"

    # user name has space as last character
    elif re.search(" $", name):
        error_message = "User name format is incorrect: Cannot have space as last character"

    # user name is 2 characters or shorter
    elif len(name) <= 2:
        error_message = "User name format is incorrect: Cannot be 2 characters or shorter"

    # user name is 20 characters or more
    elif len(name) >= 20:
        error_message = "User name format is incorrect: Cannot be 20 characters or more"

    else:
        user = bn.get_user(email)
        if user:
            error_message = "This email has been ALREADY used"
        elif not bn.register_user(email, name, password, password2):
            error_message = "Failed to store user info."

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('login.html', message=error_message)
    else:
        return redirect('/login')

@app.route('/login', methods=['GET'])
def login_get():
    # If user is already logged in, redirect to home page
    if 'logged_in' in session:
        return redirect('/')
    return render_template('login.html', message='Please login')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = None
    error_message = None

    # Preform email checks
    # Email cannot be empty
    if len(email) < 1:
        error_message = "Email format incorrect: Cannot be empty"
    # email does not follow addr-spec defined in RFC 5322
    elif not (re.match("^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]{1,64}(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9]+(?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)$", email) and re.search("@[a-zA-Z0-9-.]{1,255}$", email)):
        error_message = "Email format incorrect: Not a valid email"
    # Preform password checks
    # Password cannot be empty
    elif len(password) < 1:
        error_message = "Password format incorrect: Cannot be empty"
    # Password must be greater than length 5
    elif len(password) < 6:
        error_message = "Password format incorrect: Must be greater than 5 characters"
    # Password must contain a special character
    elif not re.search("[\"'!@#$%^&*()-+?_=,<>/'\"]+", password):
        error_message = "Password format incorrect: Must contain a special character"
    # Password must contain a capital letter
    elif not re.search("[A-Z]+", password):
        error_message = "Password format incorrect: Must contain an uppercase character"
    # Password must contain a lower case letter
    elif not re.search("[a-z]+", password):
        error_message = "Password format incorrect: Must contain a lowercase character"
    # Once the conditions are correct get the user
    else:
        user = bn.login_user(email, password)

    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        if error_message:
            return render_template('login.html', message=error_message)
        # If no error_message exists then email/password combination must be incorrect
        else:
            return render_template('login.html', message='email/password combination incorrect')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')

@app.route('/sell', methods=['POST'])
# This function posts all of the information in the sell form and creates a new ticket
def sell_post():

    message = ""
    # All of the information entered by the user

    # The owner of the ticket's email
    owner = session['logged_in']

    # The name of the ticket
    name = request.form.get('name')

    # The amount of tickets availible for sale
    quantity = request.form.get('quantity')

    # The price of a ticket
    price = request.form.get('price')

    # The date that the event is happening
    date = request.form.get('date')

    if not bn.sell_ticket(owner, name, quantity, price, date):
        print("Failed to store sell info.")
        # Return to the homepage after the post
        return redirect('/')
    else:
        user = bn.get_user(owner)
        tickets = bn.get_all_tickets()
        account_balance = bn.get_account_balance(user.email)
        # Return to the homepage after the post
        return render_template('index.html', message="Sell Successful", user=user, tickets=tickets, account_balance=account_balance)


@app.route('/buy', methods=['POST'])
# This function posts all of the information in the buy form and buys a ticket
def buy_post():

    # The name of the ticket that is being bought
    name = request.form.get('name')

    # The amount of tickets that want to be purchased
    quantity = request.form.get('quantity')

    if not bn.buy_ticket(name, quantity):
        print("Failed to store buy info.")
        # Return to the homepage after the post
        return redirect('/')
    else:
        user = bn.get_user(session['logged_in'])
        tickets = bn.get_all_tickets()
        account_balance = bn.get_account_balance(user.email)
        # Return to the homepage after the post
        return render_template('index.html', message="Buy Successful", user=user, tickets=tickets, account_balance=account_balance )


@app.route('/update', methods=['POST'])
# This function posts all of the information in the update form and updates the corresponding ticket
def update_post():
    # All of the information entered by the user

    # The owner of the ticket's email
    owner = session['logged_in']

    # The name of the ticket
    name = request.form.get('name')

    # The amount of tickets availible for sale
    quantity = request.form.get('quantity')

    # The price of a ticket
    price = request.form.get('price')

    # The date that the event is happening
    date = request.form.get('date')

    error_message = None

    # find if there is any errors in the info provided
    # ticket name is non-alphanumeric
    if not all(x.isalnum() or x.isspace() or x == "_" for x in name):
        error_message = "Ticket name format is incorrect: Must be alphanumeric"

    # ticket name has space as first character
    elif re.search("^ ", name):
        error_message = "Ticket name format is incorrect: Cannot have space as first character"

    # ticket name has space as last character
    elif re.search(" $", name):
        error_message = "Ticket name format is incorrect: Cannot have space as last character"

    # ticket name is longer than 60 characters
    elif len(name) > 60:
        error_message = "Ticket name format is incorrect: Cannot be longer than 60 characters"

    # quantity of the tickets is less than or equal to 0
    elif int(quantity) <= 0:
        error_message = "Quantity format is incorrect: Cannot be less than or equal to 0"
    
    # quantity of the tickets is greater than 100
    elif int(quantity) > 100:
        error_message = "Quantity format is incorrect: Cannot be greater than 100"

    # price is less than 10
    elif float(price) < 10:
        error_message = "Price format is incorrect: Cannot be less than 10"
        
    # price is greater than 100
    elif float(price) > 100:
        error_message = "Price format is incorrect: Cannot be greater than 100"

    # date has any non-numeric values 
    elif not date.isnumeric():
        error_message = "Date format is incorrect: Must be numeric"

    # date is not of length 8
    elif len(date) != 8:
        error_message = "Date format is incorrect: Must be 8 digits long"

    # the ticket does not exist in the database
    if not bn.update_ticket(owner, name, quantity, price, date):
        error_message = "Error when saving: Failed to store update info"

    # get info needed to render the homepage
    user = bn.get_user(session['logged_in'])
    tickets = bn.get_all_tickets()
    account_balance = bn.get_account_balance(user.email)

    # if there is an error in the info provided, return to the homepage and display the error message
    if error_message:
        return render_template('index.html', message=error_message, user=user, tickets=tickets, account_balance=account_balance)
    
    # otherwise, return to the homepage after the post and display a success message
    else:    
        return render_template('index.html', message="Update Successful", user=user, tickets=tickets, account_balance=account_balance)

def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner

@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    account_balance = bn.get_account_balance(user.email)
    return render_template('index.html', user=user, tickets=tickets, account_balance=account_balance)

@app.route('/<path:text>', methods=['GET', 'POST'])
def page_not_found(text):
    # Returns the 404 error page when a non defined path is entered
    return render_template('404.html')
