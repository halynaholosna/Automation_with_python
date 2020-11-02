from behave import given, then
from selenium.webdriver.common.by import By

BEST_SELLERS_LINKS = (By.CSS_SELECTOR, "a[href*='ref=zg_bs_tab']")

@given('Open Amazon Best Sellers page')
def open_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify {expected_count} links are present')
def verify_link_count(context, expected_count):
    links = len(context.driver.find_elements(*BEST_SELLERS_LINKS))
    assert links == int(expected_count), f'Amount of links incorrect. Expected {expected_count}, but got {links}'