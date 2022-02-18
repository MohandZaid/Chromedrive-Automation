from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import pyautogui

import time

PATH="/home/mohand5/Desktop/automation_project/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://grid.space/kiri/")

time.sleep(10)

driver.find_element_by_id("mod-x").click()

driver.find_element_by_id("gotit").click()


time.sleep(2)

pyautogui.moveTo(500, 500, duration = 0.5)

pyautogui.rightClick()
time.sleep(2)
pyautogui.rightClick()


driver.find_element_by_id("context-menu").click()

driver.find_element_by_id("context-clear-workspace").click()

time.sleep(2)


driver.find_element_by_id("lt-file").click()
driver.find_element_by_id("lt-file").click()



driver.find_element_by_id("file-import").click()

time.sleep(1)


for i in range(5):
    pyautogui.hotkey("tab")

pyautogui.hotkey("enter")


pyautogui.typewrite("/home/mohand5/Desktop/automation_project/upload-files")

pyautogui.hotkey("enter")

# for i in range(10):
#     pyautogui.hotkey("tab")

# time.sleep(1)

# pyautogui.typewrite("King.STL")

# for i in range(2):
#     pyautogui.hotkey("tab")

# pyautogui.hotkey("enter")


# driver.find_element_by_id("act-slice").click()
# driver.find_element_by_id("act-slice").click()



# driver.find_element_by_id("act-export").click()

# time.sleep(30)


# driver.find_element_by_id("print-download").click()
# time.sleep(5)
# driver.quit()
