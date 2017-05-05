# Created by schmuk at 4/28/17



Feature: Get the url of the active tab

  Scenario: I am using Google Chrome and I want
    Selfspy to retrieve the URL tab
    Given Google chrome is open
    When Selfspy is running
    Then the URL will be in the output of selfstats