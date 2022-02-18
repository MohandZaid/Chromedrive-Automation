from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import pyautogui

import time



PATH="C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://grid.space/kiri/")

time.sleep(2)

driver.find_element_by_id("mod-x").click()

driver.find_element_by_id("gotit").click()
time.sleep(2)



pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("delete")


time.sleep(1)

pyautogui.hotkey("i")

time.sleep(1)


pyautogui.hotkey("alt", "d")


pyautogui.typewrite("C:/Users/mohand/Desktop")

pyautogui.hotkey("enter")

pyautogui.hotkey("alt", "n")


pyautogui.typewrite("King.STL")


pyautogui.hotkey("enter")

time.sleep(2)

pyautogui.hotkey("x")



time.sleep(30)


driver.find_element_by_id("print-download").click()
time.sleep(5)
driver.quit()
