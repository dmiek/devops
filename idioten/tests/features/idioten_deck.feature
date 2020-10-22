Feature: Deck
    The deck is the foundation of the game. The deck contains 52 cards, consisting of hearts, clubs, spades and diamonds, and is shuffled every round.

    Scenario: Deck is of the correct type
        Given an existing deck
        When deck is shuffled
        Then deck is of correct type

    Scenario: Deck only contains allowed colours
        Given an existing deck
        When deck is shuffled
        Then deck contains only allowed colours

    Scenario: Deck only contains allowed ranks
        Given an existing deck
        When deck is shuffled
        Then deck contains only allowed ranks

    Scenario: Deck contains correct number of cards
        Given an existing deck
        When deck is shuffled
        Then deck contains all cards

    Scenario: Deck contains no duplications
        Given an existing deck
        When deck is shuffled
        Then deck contains no duplications

    Scenario: Deck is different from previous deck
        Given an existing deck
        When deck is shuffled
        Then new deck is different from previous deck
