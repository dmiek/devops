Feature: Input
  The player input to the game.


  Scenario: Input function returns only valid values
    Given player is prompted for input
    When OK input provided
    Then input is returned

  Scenario: Flag valid input as valid
    Given status of input is unknown
    When valid input is given
    Then game flags input as valid

  Scenario: Flag invalid input as invalid
    Given status of input is unknown
    When invalid input is given
    Then game flags input as invalid
