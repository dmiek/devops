import pytest
from pytest_bdd import parsers, scenario, given, when, then
from idioten_input import kb_input


@pytest.fixture
def game_is_active():
    return game_active = True

@scenario('idioten_input.feature', 'Game accepts all correct input values')
def test_ok_input():
    pass

@given('game is running')
def game_running(game_is_active):
    assert game_is_active = True

@when('keyboard input given')
def keyboard_input(kb_input):
    pass

@then('input is of correct type')
def input_type():
    pass