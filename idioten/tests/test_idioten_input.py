"""
Module for testing Idioten input functionality
"""

import sys
import pytest
from io import StringIO
from pytest_bdd import scenario, given, when, then
from _pytest.monkeypatch import MonkeyPatch
from idioten.application.idioten_input import kb_input, VALID_INPUT

# MONKEYPATCH = MonkeyPatch()


@scenario('features/idioten_input.feature', 'Keep asking for input intil valid input is given')
def test_return_ok_values():
    """Test that valid values are returned"""


# @scenario('idioten_input.feature', 'Keep prompting until valid values are given')
# def test_valid_values():


@given('game is waiting for input')
def game_waiting_for_input(input_fixture):
    """ Given game is waiting for input. """
    assert len(input_fixture) == 1
    assert len(input_fixture["keyboard"]) == 0


@when('invalid input is given "["')
def invalid_input_given(monkeypatch, input_fixture):
    """ When invalid input is given. """
    number_inputs = StringIO('1234\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    input_fixture["keyboard"] = kb_input()




@then('game is still waiting for input')
def game_still_waiting_for_input(input_fixture):
    """ Then game is still waiting for valid input. """
    assert input_fixture["keyboard"] == 'NOK'


# @given('player is prompted for input')
# def game_running():
#     """_"""
#
#
# @when('OK input provided')
# def accepted_values():
#     """Accepted values inserted"""
#     inp = MONKEYPATCH.setattr('builtins.input', lambda _: "n")
#     assert inp == 'n'
#
#
# @then('input is returned')
# def input_type():
#     """Input is accepted by game"""
#     pass
