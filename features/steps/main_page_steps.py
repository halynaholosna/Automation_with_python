from behave import given, when
from selenium.webdriver.common.by import By

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@value='Go']")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when ('Click Amazon Orders Link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()

@when('Input {product} into Amazon search field')
def input_search_word(context, product):
    search_field=context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)

@when('Click on Amazon search icon')
def click_search_icon(context):
    search_icon = context.driver.find_element(*SEARCH_ICON)
    search_icon.click()


