Feature: Input
  The player input to the game.


  Scenario: Input function returns only valid values
    Given player is prompted for input
    When OK input provided
    Then input is returned

  Scenario: Keep prompting until valid values are given
    Given game is waiting for input
    When invalid input given
    Then game is still waiting for input

  Scenario: Keep asking for input intil valid input is given
    Given game is waiting for input
    When invalid input is given "["
    Then game is still waiting for input
