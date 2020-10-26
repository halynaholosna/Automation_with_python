# Created by golos at 10/26/2020
Feature: Test for Amazon shopping cart
  # Enter feature description here

  Scenario: Shopping cart shows correct quantity of items
    Given Open Amazon page
    When Click on shopping cart icon
    Then Verify Shopping cart is empty