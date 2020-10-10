Feature: Deck
    The Deck is the foundation of the game.

    Scenario: New deck is OK and different from previous one
        Given existing deck
        When deck shuffled
        Then new deck is different from previous deck

    Scenario: Deck only contains allowed colours
        Given no deck
        When deck shuffled
        Then deck contains only allowed colours

    Scenario: Deck only contains allowed ranks
        Given no deck
        When deck shuffled
        Then deck contains only allowed ranks

    Scenario: Deck is of the correct type
        Given no deck
        When deck shuffled
        Then deck is of the correct type

    Scenario: Deck contains no duplications
        Given no deck
        When deck shuffled
        Then deck contains no duplications