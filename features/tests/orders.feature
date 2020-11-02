# Created by golos at 11/1/2020
Feature: Tests for orders functionality
  # Enter feature description here

  Scenario: Logged out user sees Sign In page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders Link
    Then Verify Sign In page is opened
