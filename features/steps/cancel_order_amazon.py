from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

HELP_SEARCH_FIELD= By.ID, 'helpsearch'
SEARCH_RESULT=By.XPATH, "//h1[text()='Cancel Items or Orders']"

@given('Open Amazon Help page')
def open_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Input Cancel order in Find more solutions field')
def input_search_phrase(context):
    context.driver.find_element(*HELP_SEARCH_FIELD).send_keys('Cancel order', Keys.ENTER)

@then('Verify that ‘Cancel Items or Orders’ text is present')
def verify_search_result(context):
    result = context.driver.find_element(*SEARCH_RESULT)
    assert result.text == 'Cancel Items or Orders', f'Error.Expected Cancel Items or Orders, but got {result.text}'
