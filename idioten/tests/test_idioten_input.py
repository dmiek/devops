"""
Module for testing Idioten input functionality
"""


from io import StringIO
from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_input import kb_input, INPUTS


@scenario('features/idioten_input.feature', 'Flag invalid input as invalid')
def test_reject_nok_values():
    """ Test that invalid values are detected. """


@scenario('features/idioten_input.feature', 'Flag valid input as valid')
def test_accept_ok_values():
    """Test that valid values are returned"""


# @scenario('idioten_input.feature', 'Keep prompting until valid values are given')
# def test_valid_values():


@given('status of input is unknown')
def game_waiting_for_input(input_fixture):
    """ Given game is waiting for input. """
    assert len(input_fixture) == 2
    assert len(input_fixture["keyboard"]) == 0
    assert input_fixture["status"] == 'unknown'


@when('invalid input is given')
def invalid_input_given(monkeypatch, input_fixture):
    """ When invalid input is given. """
    number_inputs = StringIO('1234\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    input_fixture["keyboard"] = kb_input()


@when('valid input is given')
def valid_input_given(monkeypatch, input_fixture):
    """ When invalid input is given. """
    number_inputs = StringIO('n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    input_fixture["keyboard"] = kb_input()


@then('game flags input as invalid')
def game_flags_input_as_invalid(input_fixture):
    """ Then game flags input as invalid. """
    assert input_fixture["keyboard"] == 'NOK'


@then('game flags input as valid')
def game_flags_input_as_valid(input_fixture):
    """ Then game flags input as valid. """
    assert input_fixture["keyboard"] == 'OK'


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
