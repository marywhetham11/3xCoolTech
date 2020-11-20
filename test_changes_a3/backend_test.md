## Backend Test - get_user

We chose to use output coverage by partitioning to test the get_user method in backend.py. We found that there were two partitions:

1. The method returns a User instance

If the email entered is the email of a user in the database, then the method will return an instance of that User.

Object:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

Actions to test:

- if test_user does not exist, 
  - open /register page
  - enter test_user's email into the `#email` element 
  - enter test_user's name into the `#name` element 
  - enter test_user's password into the `#password` element 
  - reenter test_user's password into the `#password2` element 
  - click `input[type="submit"]` element
- call get_user using test_user's email
- validate that the result is a User instance
- validate that the result's email matches test_user's email
- validate that the result's name matches test_user's name
- validate that the result's password matches test_user's password


2. The method returns None

If the email entered is not the email of a user in the database, then the method will return None.

Actions to test:

- call get_user using the email `"not_an_email@test.com"` (there is not a user with this email)
- validate that the result is None