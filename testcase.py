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

from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
browser = Chrome(options=opts)
browser.get("http://www.python.org")


