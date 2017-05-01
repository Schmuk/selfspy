Feature: Recognize a program, regardless of inputs

  Scenario: Program is recognized
    Given: the user has attempted opening said program
    When: the program opens
    Then: the program is recognized
