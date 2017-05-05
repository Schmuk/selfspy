# Created by joemullen at 4/30/17
Feature: A command line option to get process_id timings

  Scenario: Timings Requested
    Given: selfspy is running
    When: the user enters "--get-timings" into the command line
    Then: SQL database will get return timings of all process_ids