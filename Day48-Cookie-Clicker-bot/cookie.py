import selenium
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os

execution_path=os.environ['PATH']
ser=Service(executable_path=execution_path)
driver=webdriver.Chrome(service=ser)
import time

driver.get(url='http://orteil.dashnet.org/experiments/cookie/')
cookie=driver.find_element('id', 'cookie')
total=time.time() + 60 * 5
timeout= time.time() + 5

while time.time() < total:
    cookie.click()
    if time.time() > timeout:
        money=int(driver.find_element(by='id',value='money').text.replace(',',''))
        if money >= int(driver.find_element('css selector','#buyMine b').text.split(" - ")[1].replace(',',"")):
            Mine = driver.find_element('xpath', '//*[@id="buyMine"]')
            Mine.click()
     
        elif money >= int(driver.find_element('css selector','#buyFactory b').text.split(" - ")[1].replace(',','')):
            Buy = driver.find_element('xpath', '//*[@id="buyFactory"]')
            Buy.click()
      
        elif money >= int(driver.find_element('css selector','#buyGrandma b').text.split(" - ")[1].replace(',','')):
            Buy = driver.find_element('xpath', '//*[@id="buyGrandma"]')
            Buy.click()
 
        elif money >= int(driver.find_element('css selector','#buyCursor b').text.split(" - ")[1].replace(',','')):
            Buy = driver.find_element('xpath', '//*[@id="buyCursor"]')
            Buy.click()
        timeout+=5


time.sleep(7)
driver.close()
