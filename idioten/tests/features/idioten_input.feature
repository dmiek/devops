Feature: Input
  The player input to the game. Module for testing Idioten input functionality.
  The input module takes input of length "1" only.


  Scenario: Flag valid input as valid
    Given status of input is unknown
    When valid input is given
    Then game flags input as valid

  Scenario: Flag invalid input as invalid
    Given status of input is unknown
    When invalid input is given
    Then game flags input as invalid

  Scenario: Flag invalid when characters valid but length is too long
    Given status of input is unknown
    When valid but too long input is given
    Then game flags input as invalid


  Scenario Outline: Outlined given, when, thens
    Given there are <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers

    Examples: Vertical
    | start | 12 | 2 |
    | eat   | 5  | 1 |
    | left  | 7  | 1 |