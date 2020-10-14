"""
Module for testing Idioten input functionality
"""

import pytest
from pytest_bdd import scenario, given, when, then
from idioten_input import kb_input


GAME_ACTIVE = None

@pytest.fixture
def game_is_active():
    """Flag to indicate game active"""
    game_active = 1
    return game_active

@pytest.fixture
def game_is_not_active():
    """Flag to indicate game not active"""
    game_active = 0
    return game_active

@pytest.fixture
def allowed_values():
    """ Fixture for allowed values. """
    allowed_input = ('d', 'e', 'n', '1', '2', '3', '4')
    return allowed_input

@scenario('idioten_input.feature', 'Input function returns only valid values')
def test_return_ok_values():
    """Test that valid values are returned"""
    pass

@given('player is prompted for input', game_is_active)
def game_running(game_is_active):
    """_"""
    #game_active = game_is_active
    #kb_input(game_active)

@when('OK input provided')
def keyboard_input():
    """Keyboard input"""
    pass

@when('player inputs accepted value')
def accepted_values(input):
    """Accepted values inserted"""
    input = monkeypatch.setattr('builtins.input', lambda _: "n")
    assert input == 'n'

@then('input is returned')
def input_type():
    """Input is accepted by game"""
    pass
