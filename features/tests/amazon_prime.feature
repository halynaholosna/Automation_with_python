# Created by golos at 11/2/2020
Feature: Amazon Prime tests
  # Enter feature description here

  Scenario: Amazon Prime displays 8 benefit boxes
    Given Open Amazon Prime
    Then Verify 8 benefit boxes are displayed