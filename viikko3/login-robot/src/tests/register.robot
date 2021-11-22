*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  kalle321
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  pekka  kalle321
    Input New Command
    Input Credentials  pekka  salakka32
    Output Should Contain  User with username pekka already exists

Register With Too Short Username And Valid Password
    Input Credentials  bo  password123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  pekka  wall32
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pekka  password
    Output Should Contain  Password must have numbers

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command