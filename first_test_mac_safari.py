from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions







browser = webdriver.Safari()
browser.get('http://seleniumhq.org/')

try:
    el = browser.find_element_by_class_name('downloadBox')
    el.click()

    re = WebDriverWait(browser, 2).until(
        expected_conditions.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Downloads')
    )

    print("Hooray, we are on Downloads page")

except exceptions.TimeoutException:
    print("Sorry, it didn't work")

finally:
    browser.quit()
