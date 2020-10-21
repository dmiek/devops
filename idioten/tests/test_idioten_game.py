from pytest_bdd import scenario, given, when, then


@scenario('idioten_game.feature', 'Run game')
def test_run_game():
    """ Scenario for testing the running of game. """
    pass

@given('game is installed')
def game_installed():
    """ Placeholder for game installed. """
    pass

@when('game is started')
def game_is_started():
    """ Simulate game is started. """
    pass

@then('game frontpage is shown')
def game_frontpage_shown():
    """ Display the game frontpage. """
    pass
