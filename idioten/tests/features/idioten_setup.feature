Feature: Set up idioten
  Sets up the initial board and deck of idioten.


  Scenario Outline: Verify deck is set up regardless of state
    Given different types of <start_deck>
    When game is set up
    Then <end_deck> contains 52 cards

    Examples:
    | start_deck  | end_deck  |
    | deck_empty  | full_deck |
    | 1_card      | full_deck |
    | 2_cards     | full_deck |
    | 3_cards     | full_deck |
    | 4_cards     | full_deck |
    | 5_cards     | full_deck |
    | full_deck   | full_deck |


  Scenario Outline: Game setup clears boards
    Given <board_start>
    When game is set up
    Then <board_end>

    Examples:
    | board_start             | board_end           |
    | empty_board_double      | empty_board_single  |
    | void                    | empty_board_single  |
    | populated_single_OK_pre | empty_board_single  |
    | populated_double_OK_pre | empty_board_single  |
    | populated_triple_OK_pre | empty_board_single  |
    | populated_single_NOK    | empty_board_single  |
    | populated_double_NOK    | empty_board_single  |
    | populated_triple_NOK    | empty_board_single  |
    | scramble_1              | empty_board_single  |
    | scramble_2              | empty_board_single  |
    | scramble_3              | empty_board_single  |
    | scramble_4              | empty_board_single  |
    | scramble_5              | empty_board_single  |
    | scramble_6              | empty_board_single  |
    | scramble_7              | empty_board_single  |
    | scramble_8              | empty_board_single  |
    | scramble_9              | empty_board_single  |
    | scramble_10             | empty_board_single  |


  Scenario: Game setup can initiated already empty board
    Given board already empty
    When game is set up
    Then board is empty