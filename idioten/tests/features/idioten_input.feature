Feature: Input
  The player input to the game. Module for testing Idioten input functionality.
  The input module takes input of length "1" only.


  Scenario Outline: Tests different input and asserts corresponding assessment returned
    Given there are <startstate> cucumbers
    When I eat <inputvalue> cucumbers
    Then I should have <endstate> cucumbers

    Examples: Vertical
    | startstate  | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
    | inputvalue  | e       | b       |   .     |   [     |   d     |   dd    |   5     |   ee    |
    | endstate    | OK      | NOK     |   NOK   |   NOK   |   OK    |   NOK   |   NOK   |   NOK   |