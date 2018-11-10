'''
def add(x, y):
    return x + y

def multipy(x, y):
    return x * y

def divi(x, y):
    return x / y

def minus(x, y):
    return x - y


def main():
    assert 5 == add(3,2)
    assert 12 == add(6,6)
    assert 6 == multipy(3,2)
    assert 10 == minus(20,10)
    assert 5 == divi(10,2)
    assert 28 == add(23,5)
    assert 30 == add(25,5)
main()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")
driver.get("http://www.python.org")
'''

'''
# another option
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.set_headless()
browser = Chrome(options=opts)
browser.get("http://www.python.org")
'''

'''
# another another option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options = options,executable_path=chromedriver)
driver.get("http://www.python.org")
'''

'''
# Firefox
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('-headless')
driver = Firefox(executable_path='geckodriver', firefox_options=options)
print("in")
#wait = WebDriverWait(driver, timeout=10)
driver.get('http://www.google.com')


wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
print(driver.page_source)
driver.quit()
'''


# Firefox v.2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='C:\\Users\\Bright\\Desktop\\DC Spectre Home\\geckodriver.exe')
driver.get("http://www.python.org")
















