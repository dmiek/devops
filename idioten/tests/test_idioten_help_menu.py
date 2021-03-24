"""
Test module to test help menu.
"""


from pytest_bdd import scenario, given, when, then
from idioten.application.idioten_help_menu import help_menu


@scenario(
    'features/idioten_help_menu.feature',
    'Verify correct content is shown',
    example_converters=dict(valid_input=str, menu_content=str)
)
def test_menu_content():
    """ Tests that different types of decks can be restored and shuffled. """


@given('current <valid_input>')
def current_valid_input(menu_fixture, valid_input):
    """ Given a certain state of the game... """
    menu_fixture["valid_input"] = menu_fixture[valid_input]
    print('valid input: ', menu_fixture["valid_input"])


@when('help menu is called')
def menu_called(menu_fixture):
    """ Call help menu. """
    help_menu(menu_fixture)


@then('<menu_content> is shown and <not_in_menu> not shown')
def menu_content_shown(menu_fixture, menu_content, not_in_menu):
    """ Verify correct menu contents. """
    for i in range(len(menu_fixture[menu_content])):
        assert menu_fixture[menu_content][i] in menu_fixture["menu_output"].lower()
    assert menu_fixture[not_in_menu][0] not in menu_fixture["menu_output"].lower()
