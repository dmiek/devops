Feature: Input
  The player input to the game.

  Scenario: Input is of the correct type
    Given game is active
    When player selects input value
    Then value is of valid type
