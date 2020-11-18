from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def login(driver):
    driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1605725857?ModuleName=time_entry/job_summary.pl")
    element = driver.find_element_by_id("j_username")
    element.send_keys("Username")


driver = webdriver.Firefox()
login(driver)
time.sleep(3)
driver.close()