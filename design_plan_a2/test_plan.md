## Test Plan

#### 1. How test cases of different levels (frontend, backend units, integration) are organized.

There will be a folder for each level of test cases. So, there will be a folder for each of the following: requirements, unit, integration, system and acceptance. Within the requirement testing folder, there will be subfolder for each requirement group and within the unit testing folder, there will be a folder for the frontend and for the backend. In each folder/subfolder, there will a file for each requirement to test at this level.

#### 2. The order ot the test cases (which level first which level second).

Graeme's Question

#### 3. Techniques and tools used for testing.

Pytest and Selenium will be used to test each component each time the code is modified on git. Each component R1-R7 will have a .py test file which will be ran through pytest. Each group member who programed thier component will be responsible for the corresponding .py test file. Selenium then takes the tests from our code environment and testing them on the chrome browser.

#### 4. Environemnts (all the local environment and the cloud environment) for the testing.

This program will be tested on local environments. It will be tested on the chrome browser with the python environment and pytest powering the program. These tests will take place on Windows, Linux and Mac environment. Although, all team members own Windows computers, so the Mac and Linux environment will take extra planning to test on.

#### 5. Responsibility (who is responsible for which test case, and in case of failure, who should you contact)

Graeme's Question

#### 6. Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unncessary cost)

To ensure the system is meeting the requirments, pytest is ran upon each change to a branch. Changes will be made globaly only when deemed as complete. Therefore, we will doing regression testing. This will be produce unnecessary cost or time because our project is very small.