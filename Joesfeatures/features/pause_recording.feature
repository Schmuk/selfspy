# Created by joemullen at 4/30/17
Feature: A command line option to pause Selfspy's system recording
  Scenario: Selfspy recording is paused
    Given: selfspy is currently running
    When: user enters "--pause" command
    Then: selfspy pauses it's recording

  Scenario: Selfspy recording is unpaused
    Given: selfspy is currently paused
    When: user enters "--unpause" command
    Then: selfspy resumes recording