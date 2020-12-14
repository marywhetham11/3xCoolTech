from qa327.models import db, User, Account_Balance, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

"""
This file defines all backend logic that interacts with database and other services
"""

def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user

def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user

def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw)
    # set account balance to 5000
    new_account_balance = Account_Balance(email=email, balance=5000.00)

    db.session.add(new_user)
    db.session.add(new_account_balance)
    db.session.commit()

    return get_user(email)

def get_all_tickets():
    """
    This function returns all of the availible tickets for sale
    """
    # Find today's date and change it to a format we can compare to the database
    today = date.today()
    today = int(today.strftime('%Y%m%d'))

    # Query all of the tickets that dates have not been passed yet
    tickets = Ticket.query.filter(Ticket.date >= today).all()
    return tickets

def get_ticket(name):
    """
    This function returns a the ticket by name
    :param name: the name of the ticket
    """

    # Query the ticket that matches the name given
    ticket = Ticket.query.filter_by(name=name).first()
    return ticket

def sell_ticket(owner, name, quantity, price, date):
    """
    The user is putting up a ticket for sale
    :param owner: the email of the owner of the ticket
    :param name: the name of the ticket
    :param quantity: the amount of ticket availible for sale
    :param price: the price of the ticket
    :param date: the date of the event
    """
    # Creating a new ticket in the database
    new_ticket = Ticket(owner=owner, name=name,
                        quantity=quantity, price=price, date=date)

    db.session.add(new_ticket)
    db.session.commit()

    return new_ticket

def buy_ticket(name, quantity):
    """
    The user is buying a ticket
    :param name: the name of the ticket that is being purchased
    :param quantity: the quantity of tickets that is being purchased
    """
    ticket = Ticket.query.filter_by(name=name).first()
    # Updating the quantity of availible tickets left for sale
    ticket.quantity = ticket.quantity - int(quantity)
    db.session.commit()

    return ticket

def update_ticket(owner, name, quantity, price, date):
    """
    Update a ticket that was already for sale
    :param owner: the email of the owner of the ticket
    :param name: the name of the ticket
    :param quantity: the amount of ticket availible for sale
    :param price: the price of the ticket
    :param date: the date of the event
    """

    # find the ticket
    ticket = Ticket.query.filter_by(name=name).first()

    # if the ticket name exists in the system, then update the ticket
    if ticket:
        ticket.name = name
        ticket.quantity = int(quantity)
        ticket.price = price
        ticket.date = date
        db.session.commit()

    # if the ticket exists then return the ticket, otherwise return None
    # (ticket will be equal to None if ticket doesn't exist)
    return ticket

def get_account_balance(email):
    """
    Get an account balance by a given email
    :param email: the email of the user
    :return: an account balance that has the matched email address
    """
    account_balance = Account_Balance.query.filter_by(email=email).first()
    return account_balance

def set_account_balance(email, balance):
    """
    Set an account balance by a given email
    :param email: the email of the user
    :param balance: the amount to set the balance to
    :return: an account balance that has the matched email address
    """
    account_balance = Account_Balance.query.filter_by(email=email).first()
    account_balance.balance = balance
    db.session.commit()

    return account_balance

def delete_user(email):
    """
    Function used in integration testing to delete a user before the test is preformed
    Removes the given user from the database
    :pram email: the email of the user
    """
    user = User.query.filter_by(email=email).first()
    account_balance = Account_Balance.query.filter_by(email=email).first()
    db.session.delete(user)
    db.session.delete(account_balance)
    db.session.commit()


def delete_ticket(name):
    """
    Function used in integration testing to delete a ticket before the test is preformed
    Removes the given ticket from the database
    :param name: the name of the ticket as a string
    """
    ticket = Ticket.query.filter_by(name=name).first()
    db.session.delete(ticket)
    db.session.commit()