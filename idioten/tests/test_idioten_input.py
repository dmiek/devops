"""
Module for testing Idioten input functionality
"""

import sys
import pytest
from pytest_bdd import scenario, given, when, then
from _pytest.monkeypatch import MonkeyPatch
from idioten.application.idioten_input import kb_input, VALID_INPUT

# MONKEYPATCH = MonkeyPatch()


@scenario('features/idioten_input.feature', 'Keep asking for input intil valid input is given')
def test_return_ok_values():
    """Test that valid values are returned"""
    pass


# @scenario('idioten_input.feature', 'Keep prompting until valid values are given')
# def test_valid_values():
#     pass


@given('game is waiting for input')
def game_waiting_for_input(capsys):
    """ Given game is waiting for input. """
    kb_input()
    d = ["Waiting for input\n", "world"]
    captured = capsys.readouterr()
    print(captured)
    assert captured.out in d
    return

@when('invalid input is given "["')
def invalid_input_given():
    """ When invalid input is given. """
    pass


@then('game is still waiting for input')
def game_still_waiting_for_input():
    """ Then game is still waiting for valid input. """
    pass


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
