Feature: Deal cards

  Scenario: Cards drawn from the deck no longer exists in the deck
    Given an existing deck
    When cards are drawn from the deck
    Then cards can no longer be found in the deck

  Scenario: Exactly four cards are drawn from the deck
    Given an existing deck
    When cards are drawn from the deck
    Then deck size is decreased by four

    Scenario: Exactly four cards are to be dealt
    Given an existing deck
    When cards are drawn from the deck
    Then cards to be dealt are four

  Scenario: Cards are drawn in a specific order
    Given an existing deck
    When cards are drawn from the deck
    Then the first four cards in the deck are drawn
