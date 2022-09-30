from selenium import webdriver
import time

wd = webdriver.Chrome('C:\\users\\juanp\\chromedriver')
wd.get('https://www.linkedin.com/home')
wd.maximize_window()
time.sleep(5)