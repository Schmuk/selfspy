Feature: A command line option to ignore the lock

  Scenario: lock is ignored
    Given: the user has entered the command line switch to ignore the lock
    When: program runs
    Then: the program will ignore the lock

  Scenario: lock is acknowledge
    Given: the user has not entered the command line switch to ignore the lock
    When: the program runs
    Then: the program will acknowledge the lock
