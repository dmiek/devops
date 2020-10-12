Feature: Deck
    The Deck is the foundation of the game.


    Scenario: Deck is of the correct type
        Given existing deck
        When deck shuffled
        Then deck is of correct type

    Scenario: Deck only contains allowed colours
        Given existing deck
        When deck shuffled
        Then deck contains only allowed colours

    Scenario: Deck only contains allowed ranks
        Given existing deck
        When deck shuffled
        Then deck contains only allowed ranks

    Scenario: Deck contains correct number of cards
        Given existing deck
        When deck shuffled
        Then deck contains all cards

    Scenario: Deck contains no duplications
        Given existing deck
        When deck shuffled
        Then deck contains no duplications

#    Scenario: Deck is different from previous deck
#        Given existing deck
#        When deck shuffled
#        Then deck is different from previous deck

