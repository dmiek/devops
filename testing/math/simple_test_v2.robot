*** Settings ***
Documentation     Check arithmetic operations
Resource        ${EXEC_DIR}/resources/keywords.txt

# currently only prints to output.xml
Suite Setup  math.setup
Suite Teardown  math.teardown

*** Variables ***



*** Test Cases ***

T1: Adding two integers
        Verify addition of ${20} and ${5} is ${25}

T2: Subtracting two integers
        Verify subtraction of ${20} and ${5} is ${15}

T3: Multiplying two integers
        Verify multiplication of ${20} and ${5} is ${100}

T4: Dividing two integers -- integer result
        Verify division of ${20} and ${5} is ${4}

T5: Dividing two integers -- confirm round down to integer
        Verify division of ${20} and ${6} is ${3}

T6: Subracting two integers that results in negative number
        Verify subtraction of ${5} and ${20} is ${-15}