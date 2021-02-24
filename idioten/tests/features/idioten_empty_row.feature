Feature: Empty row
  Function returning a single empty row when needed.

  Scenario: Empty void board
    Given board is completely empty
    When empty row is put on void board
    Then void board is empty and prepared for playing

  Scenario: Empty populated board
    Given board is populated by current row
    When empty row is put on populated board
    Then populated board is empty and prepared for playing
