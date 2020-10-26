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
    example_converters=dict(start=int, eat=float, left=str)
)
def test_outlined():
    pass


@given("there are <start> cucumbers", target_fixture="start_input")
def start_input(start):
    assert isinstance(start, int)
    return dict(start=start)


@when("I eat <eat> cucumbers")
def eat_cucumbers(start_input, eat):
    assert isinstance(eat, float)
    start_input["eat"] = eat


@then("I should have <left> cucumbers")
def should_have_left_cucumbers(start_input, start, eat, left):
    assert isinstance(left, str)
    assert start - eat == int(left)
    assert start_input["start"] == start
    assert start_input["eat"] == eat


# @scenario(
#     "features/idioten_input.feature",
#     "Outlined given, when, thens",
#     example_converters=dict(keyboard=str, status=str)
# )
# def test_outlined():
#     pass
#
#
# @given("status of input is unknown", target_fixture="start_cucumbers")
# def start_cucumbers():
#     pass
#
#
# @when("I enter <keyboard> input with <status> status")
# def eat_cucumbers(input_fixture, keyboard, status, monkeypatch):
#     input_fixture["keyboard"] = keyboard
#     input_fixture["status"] = status
#     print(keyboard)
#     sling = str(keyboard) + '\n'
#     assert isinstance(keyboard, str)
#     monkeypatch.setattr('sys.stdin', sling)
#     temp_input = kb_input(INPUTS)
#     input_fixture["keyboard"] = temp_input["keyboard"]
#     input_fixture["status"] = temp_input["status"]
#
#
# @then("game flags the <status> accordingly")
# def should_have_left_cucumbers(input_fixture, keyboard, status):
#     assert input_fixture["status"] == status
#     assert input_fixture["keyboard"] == keyboard
