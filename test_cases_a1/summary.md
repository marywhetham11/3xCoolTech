## Summary of Test Cases

| Specification                                                 | Test Case ID | Purpose                                                                                |
|---------------------------------------------------------------|:------------:|----------------------------------------------------------------------------------------|
| If the user hasn't logged in, show the login page             |    R1.1.1    | Checking if the case succeeds when the user is not logged in                           |
| Login page has a default message that says 'please login'     |    R1.2.1    | Checking if default message is displayed                                               |
| If logged in, redirect to the user profile page               |    R1.3.1    | Check if when logged in the page redirects properly                                    |
| The login page provides a login from with two fields          |    R1.4.1    | Testing that two fillable forms can be used on page                                    |
| The login form can be submitted as a POST request             |    R1.5.1    | Test Post with sample form properly filled                                             |
| Email and password both cannot be empty                       |    R1.6.1    | Test with both cases empty to ensure no submission                                     |
| Email and password both cannot be empty                       |    R1.6.2    | Test with only Email empty to ensure no submission                                     |
| Email and password both cannot be empty                       |    R1.6.3    | Test with only password empty to ensure no submission                                  |
| Email has to follow addr-spec defined in RFC 5322             |    R1.7.1    | Test that a valid email can be submitted                                               |
| Email has to follow addr-spec defined in RFC 5322             |    R1.7.2    | Test an invalid Email with two '@' is not accepted                                     |
| Email has to follow addr-spec defined in RFC 5322             |    R1.7.3    | Test an invalid Email with special characters in local is not accepted                 |
| Email has to follow addr-spec defined in RFC 5322             |    R1.7.4    | Test an invalid Email with quotations is not accepted                                  |
| Email has to follow addr-spec defined in RFC 5322             |    R1.7.5    | Test an invalid Email with local greater that 64 char is not accepted                  |
| Email has to follow addr-spec defined in RFC 5322             |    R1.7.6    | Test an invalid Email with underscores in the domain is not accepted                   |
| Password has to meet the required complexity                  |    R1.8.1    | Test that a correct password is accepted                                               |
| Password has to meet the required complexity                  |    R1.8.2    | Test that incorrect password length < 6 is not accepted                                |
| Password has to meet the required complexity                  |    R1.8.3    | Test that incorrect password without an upper case is not accepted                     |
| Password has to meet the required complexity                  |    R1.8.4    | Test that incorrect password without a lower case is not accepted                      |
| Password has to meet the required complexity                  |    R1.8.5    | Test that incorrect password without a special character is not accepted               |
| For any formatting errors, render login page and show message |    R1.9.1    | Checks when the a formatting error is called the message is displayed                  |
| If email/password are correct, redirect to /                  |    R1.10.1   | Checking with a test proper email/password the redirect occurs                         |
| Otherwise, redict to /login and show message                  |    R1.11.1   | Test when the formatting is correct but no match occurs the redirect and message occur |
| If the user has logged in, redirect back to the user profile page / | R2.1 | Check that the user is redirected to the /login page |
| Otherwise, show the user registration page | R2.2 | Check that the user is directed to the /register page and the page is rendered properly |
| The registration page shows a registration form requesting: email, user name, password, assword2 | R2.3 | Check that the register form is shown and that all the elements are rendered properly |
| The registration form can be submitted as a POST request to the current URL (/register) | R2.4.1 | Check that the form is submitted properly during a successful register |
| The registration form can be submitted as a POST request to the current URL (/register) | R2.4.2 | Check that the form is submitted properly during an unsuccessful register |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5.1 | Test for error message when the email field is empty |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5.2 | Test for error message when the email does not follow addr-spec defined in RFC 5322 |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5.3 | Test for error message when the password is empty |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5.4 | Test for error message when the password is less than 6 characters |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5.5 | Test for error message when the password does not hava an uppercase character |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5.6 | Test for error message when the password does not hava a lowercase character |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5.7 | Test for error message when the password does not hava a special character |
| Password and password2 have to be exactly the same | R2.6 | Test for error message when password and password2 do not match |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character | R2.7.1 | Test for error message when user name is empty |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character | R2.7.2 | Test for error message when user name is not alphanumeric |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character | R2.7.3 | Test for error message when user name's first character is a space |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character | R2.7.4 | Test for error message when user name's last character is a space |
| User name has to be longer than 2 characters and less than 20 characters | R2.8.1 | Test for error message when user name is 2 character or less |
| User name has to be longer than 2 characters and less than 20 characters | R2.8.2 | Test for error message when user name is 20 characters or more |
| For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute) | R2.9 | Test for an error message when user enters information with formatting errors |
| If the email already exists, show message 'this email has been ALREADY used' | R2.10 | Test for an error message when user enters an email that already exists |
| If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page | R2.11 | Check that the user is created successfully |
| If the user is not logged in, redirect to login page |R3.1| Tests that if the user has not logged in yet any attempted to go to the homepage will be redirected to the login page|
| This page shows a header 'Hi {}'.format(user.name) |R3.2| Tests that after the user has logged in the h2 header says "Hi" and the user's name|
|This page shows user balance|R3.3| Tests that after the user has logged in their the account balance is shown on the homepage|
|This page shows a logout link, pointing to /logout|R3.4| Tests that after the user has logged in there is a logout link on the homepage, that logs the user out and ends their session|
|This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.|R3.5| Tests that after the user has logged in the page has all the tickets listed and can be clicked on to show with thier information|
|This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date|R3.6| Tests that after the user has logged in they are able to see a form to sell tickets with a name, quantity, price and expiration date|
be clicked on to show with thier information|
|This page contains a form that a user can buy new tickets. Fields: name, quantity|R3.7| Tests that after the user has logged in they are able to see a form to buy tickets with a name, quantity|
|This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date|R3.8| Tests that after the user has logged in they are able to see a form to update tickets with a name, quantity, price, expiration date|
|The ticket-selling form can be posted to /sell|R3.9| Tests that after the user has logged in they are able to fill out the sell form and successfully create a ticket|
|The ticket-buying form can be posted to /buy|R3.10| Tests that after the user has logged in they are able to fill out the buy form and successfully buy a ticket|
|	The ticket-update form can be posted to /update|R3.11| Tests that after the user has logged in they are able to fill out the update form and successfully update a existing ticket|
|Valid ticket input is accepted by the /sell Post|R4.0|Test to ensure a correct ticket only name is accepted|
|The name of the ticket has to be alphanumeric-only|R4.1.1|Test that a name containing special characters is regected|
|The name of the ticket cannot have spaces as the first or last character|R4.1.2|Check that a name with spaces as the first character is not allowed|
|The name of the ticket cannot have spaces as the first or last character|R4.1.3|Check that a name with spaces as the last character is not allowed|
|The name of the ticket cannot have spaces as the first or last character|R4.1.4|Check that a name with spaces as the first and last character is not allowed|
|The name of the ticket is no longer than 60 characters|R4.2.1|Check that a name with more than 60 characters is not allowed|
|The quantity of the tickets has to be more than 0, and less than or equal to 100|R4.3.1|Check that a post with less than 1 ticket quantity is regected|
|The quantity of the tickets has to be more than 0, and less than or equal to 100|R4.3.2|Check that a post with more than 100 ticket quantity is regected|
|Price has to be of range [10, 100]|R4.4.1|Checks that sample post with price less than 10 is regected|
|Price has to be of range [10, 100]|R4.4.2|Checks that sample post with price greater than 100 is regected|
|Date must be given in the format YYYYMMDD|R4.5.1|Check that date with any non-numeric values is rejected|
|Date must be given in the format YYYYMMDD|R4.5.2|Check that date not of length 8 is rejected|
|For any errors, redirect back to / and show an error message|R4.6.1|Check that upon ticket name error the page redirects and displays the message|
|For any errors, redirect back to / and show an error message|R4.6.2|Check that upon ticket quantity error the page redirects and displays the message|
|For any errors, redirect back to / and show an error message|R4.6.3|Check that upon ticket price error the page redirects and displays the message|
|The added new ticket information will be posted on the user profile page |R4.7.1|Check that a given correct sample ticket is posted to the user profile page|
|The added new ticket information will be posted on the user profile page |R4.7.2|Check that a given incorrect sample ticket is not posted and displayed to the user profile page|
| Successfully update of a ticket | R5.0 | Check that the ticket is updated successfully |
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character | R5.1.1 | Test for error message when ticket name is not alphanumeric |
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character | R5.1.2 | Test for error message when ticket name's first character is a space |
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character | R5.1.3 | Test for error message when ticket name's last character is a space |
| The name of the ticket is no longer than 60 characters | R5.2 | Test for error message when ticket name's is longer than 60 characters |
| The quantity of the tickets has to be more than 0, and less than or equal to 100 | R5.3.1 | Test for error message when ticket quantity is equal to 0 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100 | R5.3.2 | Test for error message when ticket quantity is less than 0 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100 | R5.3.3 | Test for error message when ticket quantity is greater than 100 |
| Price has to be of range [10, 100] | R5.4.1 | Test for error message when ticket price is less than 10 |
| Price has to be of range [10, 100] | R5.4.1 | Test for error message when ticket price is greater than 100 |
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R5.5.1 | Test for error message when ticket date has any non-numeric values |
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R5.5.2 | Test for error message when ticket date is not of length 8 |
| The ticket of the given name must exist | R5.6 | Test for error message when ticket does not exist |
| For any errors, redirect back to / and show an error message | R5.7 | Test for error message when ticket information is not of the correct format |
|Succesful buy | R6 | Test that the buy form successfully purchases a ticket|
|The name of the ticket has to be alphanumeric-only| R6.1.1 | Test for error message when the ticket contains non-alphanumberic characters|
|The name of the ticket has space allowed only if it is not the first or the last character| R6.1.2 | Test for error message when the ticket contains spaces that are not the first and last character|
|The name of the ticket is no longer than 60 characters| R6.2 | Test for error message when the name of the ticket contains more then 60 characters by entering 61 characters|
|The quantity of the tickets has to be more than 0, and less than or equal to 100| R6.3.1 | Test for error message when the quantity of the tickets is a negative number|
|The quantity of the tickets has to be more than 0, and less than or equal to 100| R6.3.2 | Test for error message when the quantity of the tickets is 0|
|The quantity of the tickets has to be more than 0, and less than or equal to 100| R6.3.3 | Test for error message when the quantity of the tickets is greater than 100|
|The ticket name exists in the database and the quantity is more than the quantity requested to buy| R6.4.1 | Test for error message when the entered ticket name does not exist in database|
|The ticket name exists in the database and the quantity is more than the quantity requested to buy| R6.4.2 | Test for error message when the entered quantity is less then the avalible quantity of the ticket|
|The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)| R6.5 | Test for error message when the user attempting to buy a ticket does not have sufficent funds in thier balance|
|Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages| R7 | Test for when the user logs out, they are taken back to the login in page, and can not access the buy, sell, and update forms and homepage |
|For any other requests except the ones above, the system should return a 404 error| R9 | Test for if the user attempts to go to any page that does not exist, they are shown a 404 error message|



### Questions

1. All of the documentation for the test cases is stored in a folder called test_cases on our GitHub repo. The files in this folder are:
   - R1.md: Documentation for requirement R1, written by Josh Medves
   - R2.md: Documentation for requirement R2, written by Mary Whetham
   - R3.md: Documentation for requirement R3, written by Graeme Badley
   - R4.md: Documentation for requirement R4, written by Josh Medves
   - R5.md: Documentation for requirement R5, written by Mary Whetham
   - R6.md: Documentation for requirement R6, written by Graeme Badley
   - R7.md: Documentation for requirement R7, written by Graeme Badley
   - R8.md: Documentation for requirement R8, written by Graeme Badley
   - summary.md: Includes table that summarizes the created test cases
2. The chosen testing framework test the frontend by completing the actions of a so called test user on the website. Actions could be clicking a button to entering data. The framework does this by setting up a python environment and running a python program with all of the actions that are wanted to be tested. Using Github actions, these tests will be done after every push command done on the repo.  
3. We will create a test case code file for each requirement set which will all be stored in a single frontend test case code folder. 