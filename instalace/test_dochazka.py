from selenium import webdriver

# setup
browser = webdriver.Chrome('chromedriver')
browser.get('https://testshop.pyladies.cz/vasek')


# teardown
# browser.quit()
