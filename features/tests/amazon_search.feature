# Created by golos at 10/4/2020
Feature: Tests for Amazon search
  # Enter feature description here

  Scenario: Amazon search returns correct results
    Given Open Amazon page
    When Input Dress into Amazon search field
    And Click on Amazon search icon
    Then Search result Dress is shown
