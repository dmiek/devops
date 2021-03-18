Feature: Setup idioten board
  Set up the initial board of idioten.

  Scenario: Verify board setup and empty when setup
    Given board not setup
    When game is set up
    Then board is empty

  Scenario Outline: Verify different types of boards are cleared
    Given <board_start>
    When game is set up
    Then <board_end> is empty

    Examples:
    | board_start             | board_end                 |
    | empty_board_double      | empty_board_double        |
    | void                    | void                      |
    | populated_single_OK_pre | populated_single_OK_post  |
    | populated_double_OK_pre | populated_double_OK_post  |
    | populated_triple_OK_pre | populated_triple_OK_post  |
    | populated_single_NOK    | populated_single_NOK      |
    | populated_double_NOK    | populated_double_NOK      |
    | populated_triple_NOK    | populated_triple_NOK      |