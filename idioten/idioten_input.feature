Feature: Input
  The player input to the game.


  Scenario: Game accepts all correct input values
    Given game is running
    When player is prompted for keyboard input
    And player inputs accepted value
    Then game accepts input

