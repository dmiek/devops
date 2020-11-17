Feature: Input
  The player input to the game. Module for testing Idioten input functionality.
  The input module takes input of length "1" only.

  Scenario Outline: Cards can only be moved to an empty location
    Given a board consisting of <start_board>
    When moving a card is attempted from <fr> position to <to> position
    Then board is according to <end_board>

    Examples: Input values
    | start_board             | fr  | to  |   end_board                 |
    | empty_board_single      |  1  | 1   |   empty_board_single        |
    | empty_board_single      |  2  | 1   |   empty_board_single        |
    | empty_board_double      |  1  | 1   |   empty_board_double        |
    | empty_board_double      |  2  | 1   |   empty_board_double        |
    | void                    |  2  | 1   |   void                      |
    | void2                   |  2  | 1   |   void2                     |
    | move_single_pop_NOK     |  2  | 1   |   move_single_pop_NOK       |
    | move_double_pop_NOK     |  4  | 1   |   move_double_pop_NOK       |
    | move_triple_pop_NOK     |  4  | 1   |   move_triple_pop_NOK       |
    | move_single_pop_OK_pre  |  1  | 1   |   move_single_pop_OK_pre    |
    | move_single_pop_OK_pre  |  2  | 1   |   move_single_pop_OK_post2  |
    | move_single_pop_OK_pre  |  3  | 1   |   move_single_pop_OK_post3  |
    | move_single_pop_OK_pre  |  4  | 1   |   move_single_pop_OK_post4  |
    | move_double_pop_OK_pre  |  1  | 4   |   move_double_pop_OK_post1  |
    | move_double_pop_OK_pre  |  2  | 4   |   move_double_pop_OK_post2  |
    | move_double_pop_OK_pre  |  3  | 4   |   move_double_pop_OK_post3  |

