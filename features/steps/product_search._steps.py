from behave import then
from selenium.webdriver.common.by import By

TOOLBAR_TEXT_BOLD = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@then('Search result {product} is shown')
def verify_search_result(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    assert product in result_text, f"Expected text is {product}, but got {result_text}"
