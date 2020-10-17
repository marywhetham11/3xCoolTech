##Summary of Test Cases

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

| Specification                                                 | Test Case ID | Purpose                                                                                |
|---------------------------------------------------------------|:------------:|----------------------------------------------------------------------------------------|
|Valid ticket input is accepted by the /sell Post|R4|Test to ensure a correct ticket only name is accepted|
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