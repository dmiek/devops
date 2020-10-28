"""
Module for testing Idioten input functionality.
The input module takes input of length "1" only.
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


@scenario('features/idioten_input.feature', 'Flag invalid when characters valid but length is too long')
def test_reject_ok_long_values():
    """Test that valid but too long values are rejected. """


@given('status of input is unknown')
def game_waiting_for_input(input_fixture):
    """ Given game is waiting for input. """
    assert len(input_fixture) == 2
    assert len(input_fixture["keyboard"]) == 0
    assert input_fixture["status"] == 'unknown'


@when('valid input is given')
def valid_input_given(monkeypatch, input_fixture):
    """ When invalid input is given. """
    number_inputs = StringIO('n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    temp_input = kb_input()
    input_fixture["keyboard"] = temp_input["keyboard"]
    input_fixture["status"] = temp_input["status"]


@when('invalid input is given')
def invalid_input_given(monkeypatch, input_fixture):
    """ When invalid input is given. """
    number_inputs = StringIO('5\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    temp_input = kb_input()
    input_fixture["keyboard"] = temp_input["keyboard"]
    input_fixture["status"] = temp_input["status"]


@when('valid but too long input is given')
def valid_long_input(monkeypatch, input_fixture):
    """ When valid but too long input is given. """
    char_inputs = StringIO('ee\n')
    monkeypatch.setattr('sys.stdin', char_inputs)
    temp_input = kb_input()
    input_fixture["keyboard"] = temp_input["keyboard"]
    input_fixture["status"] = temp_input["status"]


@then('game flags input as valid')
def game_flags_input_as_valid(input_fixture):
    """ Then game flags input as valid. """
    assert input_fixture["status"] == 'OK'


@then('game flags input as invalid')
def game_flags_input_as_invalid(input_fixture):
    """ Then game flags input as invalid. """
    assert input_fixture["status"] == 'NOK'



@scenario(
    "features/idioten_input.feature",
    "Outlined given, when, thens",
    example_converters=dict(start=str, eat=str, left=str)
)
def test_outlined():
    pass


@given("there are <startstate> cucumbers", target_fixture="start_input")
def start_input(startstate, input_fixture):
    """ Given game is waiting for input. """
    assert len(input_fixture) == 2
    assert len(input_fixture["keyboard"]) == 0
    assert input_fixture["status"] == 'unknown'
    assert input_fixture["keyboard"] == ''
    assert isinstance(startstate, str)
    return dict(start=startstate)


@when("I eat <inputvalue> cucumbers")
def eat_cucumbers(input_fixture, inputvalue, monkeypatch):
    """ When valid but too long input is given. """
    char_inputs = StringIO(inputvalue + '\n')
    monkeypatch.setattr('sys.stdin', char_inputs)
    temp_input = kb_input()
    input_fixture["keyboard"] = temp_input["keyboard"]
    input_fixture["status"] = temp_input["status"]
    assert isinstance(inputvalue, str)


@then("I should have <endstate> cucumbers")
def should_have_left_cucumbers(input_fixture, startstate, inputvalue, endstate):
    assert isinstance(endstate, str)
    assert input_fixture["status"] == endstate
