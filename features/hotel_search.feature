Feature: As a user I want to search for hotels so that I can book a room on expedia website

    Scenario Outline: User searches for a hotel by entering location in the search box
        Given I'm on a hotels tab
        When I enter the <desired_location> and click search
        Then I must get <available_hotels> as a result

        Examples:
            | desired_location | available_hotels |
            | key west         | 20               |
            | new york         | 20               |
