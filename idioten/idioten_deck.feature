Feature: Deck
    The Deck is the foundation of the game.

    Scenario: Deck only contains allowed colours
        Given existing deck
        When deck shuffled
        Then deck contains only allowed colours

    Scenario: Deck only contains allowed ranks
        Given existing deck
        When deck shuffled
        Then deck contains only allowed ranks
