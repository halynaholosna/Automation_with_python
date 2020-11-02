# Created by golos at 11/2/2020
Feature: Amazon Best Sellers tests
  # Enter feature description here

  Scenario: Amazon Best Sellers page contains 5 links
    Given Open Amazon Best Sellers page
    Then Verify 5 links are present