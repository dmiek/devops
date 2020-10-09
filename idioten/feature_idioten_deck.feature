Feature: Deck
    The Deck is the foundation of the game.

    Scenario: Deck only contains allowed colours
        Given no active round
        When new deck generated
        Then deck contains only allowed colours

    Scenario: Deck only contains allowed ranks
        Given no active round
        When new deck generated
        Then deck contains only allowed ranks

    Scenario: Deck is shuffled again at the start of each round
        Given no active round
        When new deck generated
        Then new deck is different from previous deck