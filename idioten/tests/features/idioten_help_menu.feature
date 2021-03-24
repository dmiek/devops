Feature: Help menu
  Idioten has a dynamic help menu, which changes dynamically depending on game state.


  Scenario Outline: Verify correct content is shown
    Given current <valid_input>
    When help menu is called
    Then <menu_content> is shown

    Examples:
    | valid_input   | menu_content  |
    | e             | end_game_in   |
    | n             | new_game_in   |
    #| ne            | end_game_in   |


