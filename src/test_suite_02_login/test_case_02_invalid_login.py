from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest
@pytest.fixture
def selenium(selenium):
    # selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


def test_case_02_invalid_login(selenium, base_url):
    step_01_open_tested_page(selenium, base_url)
    step_02_click_on_login(selenium)
    step_03_fill_username(selenium)
    step_04_fill_password(selenium)
    step_05_click_submit(selenium)


def step_01_open_tested_page(selenium, base_url):
    selenium.get(base_url)

def step_02_click_on_login(selenium):
    el = selenium.find_element_by_link_text('Login or register')
    el.click()

    re = WebDriverWait(selenium, 2).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Log In')
    )

def step_03_fill_username(selenium):
    el = selenium.find_element_by_id('id_login-username')
    el.send_keys('asdf@asfd.cz')

def step_04_fill_password(selenium):
    el = selenium.find_element_by_id('id_login-password')
    el.send_keys('asdf')

def step_05_click_submit(selenium):
    el = selenium.find_element_by_name('login_submit')
    el.click()

    # kdyz potrebujeme otestovat, ze na strance je nejaky konkretni element
    el = selenium.find_element_by_xpath('//*[@id="login_form"]/div[1]/strong')

    # kdyz potrebujeme zjistit, ze element obsahuje konkretni text
    assert 'Oops!' in el.text



