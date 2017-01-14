from selenium import webdriver

# setup browser
browser = webdriver.Chrome('chromedriver')

# open page
browser.get('https://testshop.pyladies.cz/vasek')

# teardown
browser.quit()
