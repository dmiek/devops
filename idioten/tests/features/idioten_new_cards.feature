Feature: Deal cards
  Module which is pulling cards from the deck and then adds them to the board.

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


  Scenario Outline: Cards are dealt to the correct row, even if columns are uneven
    Given a <start_board>
    When cards are dealt to the board
    Then board looks like <end_board>

    Examples:
    | start_board           | end_board             |
    | single_even_pre       | single_even_post      |
    | single_uneven_1_pre   | single_uneven_1_post  |
    | single_uneven_2_pre   | single_uneven_2_post  |