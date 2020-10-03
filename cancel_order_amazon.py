"""
Test Case:
User can search for solutions of Cancelling an order on Amazon
1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
2. Use “Find more solutions” field and search for Cancel order:
3. Click Go ot hit Enter button
4. Verify that ‘Cancel Items or Orders’ text is present
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='D:\QA\Automation_with_python\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# send text in search field
input_field = driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)

# verify if particular text is present on the page
assert "Cancel Items or Orders" in driver.page_source

driver.quit()



