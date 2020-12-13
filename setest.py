from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
action = ActionChains(driver)
driver.get("http://127.0.0.1:8000/")
import time
#driver.find_element_by_link_text("Signup").click()
#driver.find_element_by_name('User_Name').send_keys("sasank11")
#driver.find_element_by_name('Email').send_keys("sa1@gmail1.com")
#driver.find_element_by_name('Password').send_keys("sa11@gmail.com")
#driver.find_element_by_id('sp').click()
#time.sleep(1)
driver.find_element_by_name('username').send_keys("manikanta")
driver.find_element_by_name('password').send_keys("mani1234")
driver.find_element_by_id('logsu').click()


driver.find_element_by_link_text("KNOW UR DIABETIC STATUS").click()

driver.find_element_by_name('pg').send_keys("6")
driver.find_element_by_name('gl').send_keys("148")
driver.find_element_by_name('bp').send_keys("72")
driver.find_element_by_name('st').send_keys("35")
driver.find_element_by_name('ins').send_keys("0")
driver.find_element_by_name('bmi').send_keys("33.6")
driver.find_element_by_name('dpf').send_keys("0.627")
driver.find_element_by_name('age').send_keys("50")
driver.find_element_by_id('dia').click()

time.sleep(1)
driver.find_element_by_link_text("Profile").click()
time.sleep(3)
driver.find_element_by_link_text("Home").click()
time.sleep(1)
driver.find_element_by_link_text("KNOW UR HEART STATUS").click()
time.sleep(1)

driver.find_element_by_name('nop').send_keys("2")
driver.find_element_by_name('nol').send_keys("2")
driver.find_element_by_name('nom').send_keys("2")
driver.find_element_by_name('d1').send_keys("0")
driver.find_element_by_name('d2').send_keys("1")
driver.find_element_by_name('d3').send_keys("2")
driver.find_element_by_name('nod').send_keys("2")
driver.find_element_by_name('DM').send_keys("1")
driver.find_element_by_id('ad').click()

time.sleep(1)
driver.find_element_by_link_text("Profile").click()
driver.find_element_by_link_text("Sign out").click()
