Feature: Help menu
  Idioten has a dynamic help menu, which changes dynamically depending on game state.


  Scenario Outline: Verify correct content is shown
    Given current <valid_input>
    When help menu is called
    Then <menu_content> is shown and <not_in_menu> not shown

    Examples:
    | valid_input | menu_content  | not_in_menu |
    | d           | deal_cards    | x           |
    | e           | end_game      | deal_cards  |
    | m           | move_card     | x           |
    | n           | new_game      | deal_cards  |
    | en          | end_new       | deal_cards  |
    | den         | deal_end_new  | x           |
    | 1           | positions     | x           |
