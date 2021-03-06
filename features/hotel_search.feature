Feature: As a user I want to search for hotels so that I can book a room on expedia website

    Scenario Outline: User searches for a hotel by entering location in the search box
        Given I'm on a hotels tab
        When I enter the <desired_location> and click search
        Then I must get <hotels_quantity> hotels as a result
        And if I scroll down to the last hotel
        Then I should see more than <hotels_quantity> hotels
        And first result must have sponsored label

        Examples:
            | desired_location | hotels_quantity |
            | honolulu         | 19              |
            | miami            | 20              |

