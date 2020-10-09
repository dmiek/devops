Feature: Deck
    The Deck is the foundation of the game.

    Scenario: Deck only contains allowed colours
        Given new round started
        When new deck is generated
        Then deck contains only allowed colours

    Scenario: Deck only contains allowed ranks
        Given new round started
        When new deck is generated
        Then deck contains only allowed ranks

    Scenario: Deck is shuffled again at the start of each round
        Given no active round
        When new round started
        Then deck is shuffled