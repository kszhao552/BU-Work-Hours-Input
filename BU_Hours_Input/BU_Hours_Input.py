from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config
import sys

def login(driver):
    driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1605725857?ModuleName=time_entry/job_summary.pl")
    element = driver.find_element_by_id("j_username")
    element.send_keys(config.username)
    element = driver.find_element_by_id("j_password")
    element.send_keys(config.password)
    element.send_keys(Keys.ENTER)
    
    driver.implicitly_wait(20)
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    
    driver.switch_to.frame('duo_iframe')
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div/div/div/div/form/div/fieldset/div/button')))
    driver.find_element_by_xpath('//div/div/div/div/form/div/fieldset/div/button').click()
    element.click()
    start = time.time()
    while True:
        if "Login" not in driver.title:
            return
        elif(time.time() - start >= 60):
            print("2FA failed, please try again")
            driver.close()
            sys.exit()
    
    

driver = webdriver.Firefox()
login(driver)
driver.close()