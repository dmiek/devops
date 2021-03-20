Feature: Set up idioten board
  Set up the initial board of idioten.

  Scenario: Verify board set up and empty when setup
    Given board not set up
    When game is set up
    Then board is empty

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