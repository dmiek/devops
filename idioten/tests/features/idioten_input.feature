Feature: Input
  The player input to the game. Module for testing Idioten input functionality.
  The input module takes input of length "1" only.


  Scenario Outline: Tests different input and asserts corresponding assessment returned
    Given there are <startstate> cucumbers
    When I eat <inputvalue> cucumbers
    Then I should have <endstate> cucumbers

    Examples: Input values
    | startstate  | inputvalue  | endstate  |
    |   unknown   |     e       |   OK      |
    |   unknown   |     b       |   NOK     |
    |   unknown   |     .       |   NOK     |
    |   unknown   |     [       |   NOK     |
    |   unknown   |     d       |   OK      |
    |   unknown   |     dd      |   NOK     |
    |   unknown   |     5       |   NOK     |
    |   unknown   |     ee      |   NOK     |