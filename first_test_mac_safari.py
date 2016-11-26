from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
# browser = webdriver.Firefox(firefox_binary=binary)
browser = webdriver.Safari()
browser.get('http://seleniumhq.org/')

try:
    el = browser.find_element_by_class_name('downloadBox')
    el.click()

    re = WebDriverWait(browser, 2).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Downloads')
    )

    print("Hooray, we are on Downloads page")

except TimeoutException:
    print("Sorry, it didn't work")

finally:
    browser.quit()