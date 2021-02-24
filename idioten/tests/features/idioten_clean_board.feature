Feature: Board clean-up
    Cleans the board if empty lines are present.

  Scenario Outline: Remove empty lines from board
    Given an <existing> board
    When empty rows are cleaned from <existing> board larger than 1 row
    Then board is according to <end> board

    Examples:
    | existing                | end                     |
    | void                    | void                    |
    | void2                   | void2                   |
    | empty_board_single      | empty_board_single      |
    | empty_board_double      | empty_board_single      |
    | populated_single_NOK    | populated_single_NOK    |
    | populated_double_NOK    | populated_double_NOK    |
    | populated_triple_NOK    | populated_triple_NOK    |
    | move_single_pop_OK_pre  | move_single_pop_OK_pre  |
    | move_double_pop_OK_pre  | move_double_pop_OK_pre  |
    | move_triple_pop_OK_pre  | move_triple_pop_OK_pre  |
    | move_quad_asym_OK_pre   | move_quad_asym_OK_pre   |
    | clean_double_OK_pre     | clean_double_OK_post    |
    | clean_triple_OK_pre     | clean_triple_OK_post    |
    | clean_quad_OK_pre       | clean_quad_OK_pre       |
