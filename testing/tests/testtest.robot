*** Settings ***
Documentation     Example using the space separated format.
Library           OperatingSystem

*** Variables ***
${ARG1}                 1
${ARG2}                 2

*** Test Cases ***
Run Program
    [Documentation]     Performing simple testing of
    ...                 addtion function.

    [Arguments]    @{arg1}  @{ARG2}
    Run Process    testcode.py    @{arg1}   @{arg2}

Addition: 1+1
    Do Something        1    1
    ${value} =          testcode.py  arg1  arg2
    Should Be Equal     ${value}    3

*** Keywords ***
addition