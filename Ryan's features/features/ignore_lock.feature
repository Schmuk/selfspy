Feature: A command line option to ignore the lock

  Scenario: lock is ignored
    Given: a lock already exists
    When: the user has entered the command line switch to ignore the lock
    Then: the program will delete_the_lock_and_close

  Scenario: lock is acknowledged
    Given: a lock exists
    When: the user has not entered the command line switch to ignore the lock
    Then: the program will acknowledge the lock and close
