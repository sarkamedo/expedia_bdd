Feature: search for hotels

   Scenario: User searches for a hotel by entering location in the search box
    Given I'm on a hotels tab
    When I enter the desired location and click search
    Then I must get 20 hotels as a result
    And if I scroll down it should load another 20 hotels