Feature: Input
  The player input to the game. Module for testing Idioten input functionality.
  The input module takes input of length "1" only.

  Scenario Outline: No card is removed if board is empty
    Given a board consisting of <start_board>
    When a card removal is attempted at <x> position
    Then board is according to <end_board>

    Examples: Input values
    | start_board             | x | end_board                 |
    | empty_board_single      | 1 | empty_board_single        |
    | empty_row_double        | 1 | empty_row_double          |
    | void                    | 1 | void                      |
    | populated_single_OK_pre | 1 | populated_single_OK_post  |
    | populated_double_OK_pre | 1 | populated_double_OK_post  |
    | populated_triple_OK_pre | 1 | populated_triple_OK_post  |
    | populated_single_NOK    | 1 | populated_single_NOK      |
    | populated_double_NOK    | 1 | populated_double_NOK      |
