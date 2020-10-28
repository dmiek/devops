Feature: Function returning empty rows.

  Scenario: Setup void board
    Given board is completely empty
    When empty row is put on board
    Then board is empty and prepared for playing
