# Created by schmuk at 5/4/17
Feature: Reconstruct Text

  Scenario: A user uses selfspy to reconstruct text lost in a crash
    Given the user has the text "<[Tab]x3>Said someone had seem <[Backspace]x2>n Jon on his bike"
    When the to_humanreadable method is called on the text
    Then the output text should be "\t\t\t Said someone had seen Jon on his bike"


