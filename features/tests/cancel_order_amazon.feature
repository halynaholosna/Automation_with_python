# Created by golos at 10/26/2020
Feature: Tests for Amazon Help page
  # Enter feature description here

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon Help page
    When Input Cancel order in Find more solutions field
    Then Verify that ‘Cancel Items or Orders’ text is present
