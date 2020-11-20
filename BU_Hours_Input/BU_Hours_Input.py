from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config


def login(driver):
    driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1605725857?ModuleName=time_entry/job_summary.pl")
    element = driver.find_element_by_id("j_username")
    element.send_keys(config.username)
    element = driver.find_element_by_id("j_password")
    element.send_keys(config.password)
    element.send_keys(Keys.ENTER)
    
    driver.implicitly_wait(3)
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    
    driver.switch_to.frame('duo_iframe')#/div/div/div/div/form/div/fieldset/div[@class = "row-label push-label"]')#update to get xpath inside div
    element = driver.find_element_by_xpath('//div/div/div/div/form/div/fieldset/div/button')
    print(element)
    try:
        element.click()
        driver.implicitly_wait(60)
        print("2FA failed. Please run program again.")
    except:
        return


driver = webdriver.Firefox()
login(driver)
driver.close()