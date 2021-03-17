Feature: Gameplay
  Game is started by dealing four cards from the deck.

  Scenario: Initiate game
    Given deck is complete
    When new game is started
    Then four cards are dealt from the deck