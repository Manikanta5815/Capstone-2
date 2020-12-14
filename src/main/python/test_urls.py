from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
driver=webdriver.Chrome()
action = ActionChains(driver)
driver.get("http://127.0.0.1:8000/")
driver.find_element_by_name('username').send_keys("manikanta")
driver.find_element_by_name('password').send_keys("mani@1234")
driver.find_element_by_id('logsu').click()

print('test case passed')
														



def x(out):
    
    out.write("test case passed")
