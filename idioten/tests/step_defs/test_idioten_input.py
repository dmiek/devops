"""
Module for testing Idioten input functionality
"""


import pytest
from pytest_bdd import scenario, given, when, then
from _pytest.monkeypatch import MonkeyPatch

MONKEYPATCH = MonkeyPatch()


@pytest.fixture
def allowed_values():
    """ Fixture for allowed values. """
    allowed_input = ('d', 'e', 'n', '1', '2', '3', '4')
    return allowed_input


# @scenario('idioten_input.feature', 'Input function returns only valid values')
# def test_return_ok_values():
#     """Test that valid values are returned"""
#     pass

@scenario('idioten_input.feature', 'Keep prompting until valid values are given')
def test_valid_values():
    pass


@given('game waiting for input')
def game_waiting_for_input():
    pass


@when('invalid input given')
def invalid_input_given():
    pass


@then('game waiting for input')
def game_still_waiting_for_input():
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
