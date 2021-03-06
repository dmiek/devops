Feature: Deck
    The deck is the foundation of the game. The deck consists of 52 cards and is using the French suits, consisting of hearts, clubs, spades and diamonds. The deck is shuffled before every game.
    https://en.wikipedia.org/wiki/Standard_52-card_deck

    Scenario: Deck is of the correct type
        Given an existing deck
        When deck is shuffled
        Then deck components are of correct type (list)

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
