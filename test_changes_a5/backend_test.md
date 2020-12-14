## Backend Test - login_user

We chose to use conditional coverage to test the login_user method in backend.py. 

The following is the code for this method:
```
user = get_user(email)
if not user or not check_password_hash(user.password, password):
    return None
return user
```

This method has two inputs: 
1. `email`
2. `password`

There are two conditions in this method: 
1. `not user`
2. `not check_password_hash(user.password, password)`

Also, there will be a user stored in the database given below:
```
test_user = User(
    email='test_backend@test.com',
    name='test_backend',
    password='Test_Backend_Password'
)
```

So, the test cases are:

| Condition | email input | password input | Test | email | password |
|:---------:|:-----------:|:--------------:|:----:|:-----:|:--------:|
| 1:true | `not_a_user` | `Test_Backend_Password` | T1 | `not_a_user` | `Test_Backend_Password` |
| 1:false | `test_backend@test.com` | `Test_Backend_Password` | T2 | `test_backend@test.com` | `Test_Backend_Password` |
| 2:true | `test_backend@test.com` | `not_correct_password` | T3 | `test_backend@test.com` | `not_correct_password` |
| 2:false | `test_backend@test.com` | `Test_Backend_Password` | T2 | `test_backend@test.com` | `Test_Backend_Password` |