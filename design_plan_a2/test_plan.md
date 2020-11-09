## Test Plan

#### 1. How test cases of different levels (frontend, backend units, integration) are organized.

There will be a folder for each level of test cases. So, there will be a folder for each of the following: requirements, unit, integration, system and acceptance. Within the requirement testing folder, there will be subfolder for each requirement group and within the unit testing folder, there will be a folder for the frontend and for the backend. In each folder/subfolder, there will a file for each requirement to test at this level.

#### 2. The order ot the test cases (which level first which level second).  

The order of the test cases would be:

Level One - All test cases on the registration of a user
Level Two - All test cases on the login of a user
Level Three - All the test cases on the selling of the ticket
Level Four - All the test cases on the buying and updating of tickets

#### 3. Techniques and tools used for testing.

Pytest and Selenium will be used to test each component each time the code is modified on git. Each component R1-R7 will have a .py test file which will be ran through pytest. Each group member who programed thier component will be responsible for the corresponding .py test file. Selenium then takes the tests from our code environment and testing them on the chrome browser.

#### 4. Environemnts (all the local environment and the cloud environment) for the testing.

This program will be tested on local environments. It will be tested on the chrome browser with the python environment and pytest powering the program. These tests will take place on Windows, Linux and Mac environment. Although, all team members own Windows computers, so the Mac and Linux environment will take extra planning to test on.

#### 5. Responsibility (who is responsible for which test case, and in case of failure, who should you contact)

All test cases for requirement 1 and requirement 4 are Joshua's responsibility. 
All test cases for requirement 2 and requirement 5 are Mary's responsibility.
All test cases for requirement 3, requirement 6, requirement 7 and requirement 8 are Graeme's responsibility. 

#### 6. Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unncessary cost)

To ensure the system is meeting the requirments, pytest is ran upon each change to a branch. Changes will be made globaly only when deemed as complete. Therefore, we will doing regression testing. This will be produce unnecessary cost or time because our project is very small.