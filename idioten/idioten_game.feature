Feature: Gameplay
    Play the game

    Scenario: Run game
        Given game is installed
        When game is started
        Then game frontpage is shown
