Feature: Setup idioten board
  Set up the initial board of idioten.

  Scenario: Verify board setup and empty when initiated
    Given board not setup
    When setup is called
    Then board is setup