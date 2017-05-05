# Created by schmuk at 4/28/17



Feature: Get the URL of the active tab

  Scenario:  A user of selfspy and selfstats wants the active tab's url displayed instead of the window's name in the output
    Given I have been running selfspy and using Google Chrome
    When I enter the "selfstats" command
    Then I should see the the active tab urls in the output