from behave import when
from selenium.webdriver.common.by import By

PRODUCT_RESULT=(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

@when('Click on the first product')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULT).click()
