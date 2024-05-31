Feature: Amazon Shopping
  As an online shopper,
  I want to search for a product on Amazon,
  add it to my basket, and update the quantity of the item
  to ensure a seamless shopping experience.

  Scenario: Shopping on Amazon
    Given I am on the Amazon.de homepage
    When I search for a product
    And I add the product to my basket
    And I update the quantity of the item in my basket
    Then I should see the updated quantity in my basket