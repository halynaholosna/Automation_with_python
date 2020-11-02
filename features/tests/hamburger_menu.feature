# Created by golos at 11/2/2020
Feature: Tests for Amazon Hamburger menu
  # Enter feature description here

  Scenario: User sees all links when opens
    Given Open Amazon page
    When Click to open Amazon Hamburger menu
    Then Verify 53 links are visible
