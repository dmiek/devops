Feature: Input
  The player input to the game.


  Scenario: Input function returns only valid values
    Given player is prompted for input
    When OK input provided
    Then input is returned

  Scenario: Keep prompting until valid values are given
    Given game waiting for input
    When invalid input given
    Then game waiting for input

  Scenario: 