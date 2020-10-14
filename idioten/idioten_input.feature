Feature: Input
  The player input to the game.


  Scenario: Input function returns only valid values
    Given player is prompted for input
    When OK input provided
    Then input is returned
