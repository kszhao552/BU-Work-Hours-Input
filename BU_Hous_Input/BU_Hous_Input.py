from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1605725845?ModuleName=menu.pl&NewMenu=Work")
driver.close()