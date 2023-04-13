import os
import time
from bs4 import BeautifulSoup
import selenium
import requests
import json
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

Google_form = os.environ['GOOGLE FORM']
Magic_bricks = os.environ['HOUSE FOR RENT']
Executable_path=os.environ['CHROME DRIVER PATH']

website_code=requests.get(url=Magic_bricks).text

soup=BeautifulSoup(website_code, 'html.parser')

service=Service(executable_path=Executable_path)
driver=webdriver.Chrome(service=service)
driver.get(Google_form)

wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="text"]')))
# inputs=driver.find_elements(by=By.XPATH,value='//input[@type="text"]')
# print(inputs)
# # time.sleep(3)
# for item in inputs:
#     print(item)
#     print(item.tag_name)
#     item.click()
#     item.send_keys('d')
#
# Submit=driver.find_element(By.XPATH,"//*[contains(text(),'Submit')]")
# Submit.click()
#
# time.sleep(2)
#
# driver.find_element(By.TAG_NAME,'a').click()
#


for residences in soup.find_all('div', class_='mb-srp__list'):

    wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="text"]')))
    inputs = driver.find_elements(by=By.XPATH, value='//input[@type="text"]')

    price = residences.find('div', class_='mb-srp__card__price--amount').text

    place = residences.find('script').text
    place = json.loads(place)
    address = place['address']['addressLocality']

    url = place['url']

    form_list=[address,price,url]

    for i in range(0,3):
        inputs[i].click()
        inputs[i].send_keys(form_list[i])

    Submit = driver.find_element(By.XPATH, "//*[contains(text(),'Submit')]")
    Submit.click()

    time.sleep(2)

    driver.find_element(By.TAG_NAME, 'a').click()

time.sleep(10)
driver.close()

