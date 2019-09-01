Feature: As a user I want to search for hotels so that I can book a room on expedia website

    Scenario Outline: User searches for a hotel by entering location in the search box
        Given I'm on a hotels tab
        When I enter the <desired_location> and click search
        Then I must get <hotels_list> as a result
        And if I scroll down to the last hotel
        Then I should see more than <hotels_list>

        Examples:
            | desired_location | hotels_list |
            | honolulu         | 19          |
            | new york         | 19          |
