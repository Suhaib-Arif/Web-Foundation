import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os


path=os.environ["PATH"]
url='https://tinder.com/app/recs'
service=Service(path)
driver=webdriver.Chrome(service=service)


wait = WebDriverWait(driver,10)



driver.get(url=url)

driver.maximize_window()
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="q-497183963"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')))
login=driver.find_element(by='xpath',value='//*[@id="q-497183963"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Log in with Facebook')]")))
    print("Click")
    Facebook=driver.find_element(by=By.XPATH,value="//div[contains(text(),'Log in with Facebook')]")
    Facebook.click()
except StaleElementReferenceException:
    Facebook = driver.find_element(by=By.XPATH, value="//div[contains(text(),'Log in with Facebook')]")
    Facebook.click()

except TimeoutException:
    Facebook = driver.find_element(by=By.XPATH, value="//button[contains(text(),'More Options')]")
    Facebook.click()

    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Log in with Facebook')]")))
    Facebook = driver.find_element(by=By.XPATH, value="//div[contains(text(),'Log in with Facebook')]")
    Facebook.click()


time.sleep(4)

driver.switch_to.window(driver.window_handles[1])

email=driver.find_element(by=By.ID,value='email')
email.send_keys(os.environ["NUMBER"])
password=driver.find_element(by=By.ID,value='pass')
password.send_keys(os.environ['PASSWORD'])
password.send_keys(Keys.ENTER)

driver.switch_to.window(driver.window_handles[0])

def handling_requests():
    try:
        for i in range(0,2):
            time.sleep(4)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="q2069402257"]/main/div/div/div/div[3]/button[1]')))
            Allow=driver.find_element(By.XPATH,'//*[@id="q2069402257"]/main/div/div/div/div[3]/button[1]')
            Allow.click()
    except TimeoutException:
        time.sleep(4)
        handling_requests()



handling_requests()

wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="q-497183963"]/div/div[2]/div/div/div[1]/div[1]/button')))
I_accept=driver.find_element(By.XPATH,'//*[@id="q-497183963"]/div/div[2]/div/div/div[1]/div[1]/button')
I_accept.click()

time.sleep(4)

Continue=True

body=driver.find_element(By.CSS_SELECTOR,'body')

while Continue:
    try:
        time.sleep(4)
        driver.find_element(by=By.XPATH,value='//*[@id="q2069402257"]/main/div/div[1]/div[3]/div[3]/button')
        print("Excepted")
        Continue=False

    except NoSuchElementException:
        for i in range(0,5):
            time.sleep(1)
            body.send_keys(Keys.RIGHT)

time.sleep(6)

driver.close()
