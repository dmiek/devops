Feature: Input
  The player input to the game. Module for testing Idioten input functionality.
  The input module takes input of length "1" only.

  Scenario Outline: No card is removed if board is empty
    Given a board consisting of <a> <b> <c> <d>
    When a card removal is attempted at <x> position
    Then board is according to <end_board>

    Examples: Input values
    | a  | b  | c  | d  | x  |       end_board         |
    | -  | -  | -  | -  | 1  | '- ', '- ', '- ', '- '  |
