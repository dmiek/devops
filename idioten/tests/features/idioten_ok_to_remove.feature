Feature: Feature keeping track of valid removal of cards.

  Scenario Outline: Test if card is OK to remove or not
    Given a <start_row> of cards
    When a card at <pos> position is requested to be removed
    Then the <end_status> is set accordingly

    Examples:
    | start_row       | pos | end_status |
    | void            | 1   |     0      |
    | empty_row       | 1   |     0      |
    | populated_OK_1  | 1   |     1      |
    | populated_OK_2  | 2   |     1      |
    | populated_NOK_1 | 1   |     0      |
    | populated_NOK_4 | 4   |     0      |
    | position_empty_2| 2   |     0      |