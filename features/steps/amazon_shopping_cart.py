from behave import when, then
from selenium.webdriver.common.by import By

SHOPPING_CART_ICON = By.ID, 'nav-cart'
SHOPPING_CART_ITEMS = By.XPATH, "//div[@class = 'a-row sc-your-amazon-cart-is-empty']"

@when ('Click on shopping cart icon')
def click_shopping_cart_icon(context):
    context.driver.find_element(*SHOPPING_CART_ICON).click()

@then ('Verify Shopping cart is empty')
def verify_shopping_cart_empty(context):
    result = context.driver.find_element(*SHOPPING_CART_ITEMS)
    assert result.text == 'Your Amazon Cart is empty', f'Error.Expected Your Amazon Cart is empty , but got {result.text}'
