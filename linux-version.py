from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

PATH=""

driver = webdriver.Chrome(PATH)

driver.get("https://grid.space/kiri/")

driver.find_element_by_id("mod-x").click()

driver.find_element_by_id("gotit").click()


driver.find_element_by_id("lt-file").click()
driver.find_element_by_id("lt-file").click()



driver.find_element_by_id("file-import").click()