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
    assert game_is_active == True

@when('keyboard input given')
def keyboard_input(kb_input):
    """Keyboard input"""
    pass

@then('input is of correct type')
def input_type():
    """"""
    pass
