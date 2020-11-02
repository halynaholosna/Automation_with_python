# Created by golos at 10/4/2020
Feature: Tests for Amazon search
  # Enter feature description here
 Scenario: Amazon search returns correct results
    Given Open Amazon page
    When Input Shoes into Amazon search field
    And Click on Amazon search icon
    Then Search result Shoes is shown

  Scenario: User can add product to the card
    Given Open Amazon page
    When Input Laptop into Amazon search field
    And Click on Amazon search icon
    And Click on the first product
    And Click on Add to cart button
    Then Verify shopping cart has 1 item


