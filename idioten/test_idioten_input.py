"""
Module for testing Idioten input functionality
"""

import pytest
from pytest_bdd import parsers, scenario, given, when, then
from idioten_input import kb_input


@pytest.fixture
def game_is_active():
    """Flag to indicate game active"""
    game_active = True
    return game_active

@scenario('idioten_input.feature', 'Game accepts all correct input values')
def test_ok_input():
    """Test that correct input is accpeted"""
    pass

@given('game is running')
def game_running(game_is_active):
    """Game active-flag set to True"""
    assert game_is_active == True

@when('player is prompted for keyboard input')
def keyboard_input(kb_input):
    """Keyboard input"""
    pass

@when('player inputs accepted value')
def accepted_values():
    """Accepted values inserted"""
    pass

@then('game accepts input')
def input_type():
    """Input is accpeted by game"""
    pass
