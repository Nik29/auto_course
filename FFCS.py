import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
from pygame import mixer




mixer.init()

##chromedriver = "/Users/Nikunj/Downloads/chromedriver"
##os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome()

driver.get('https://vtop.vit.ac.in/addrop/ffcs_login.asp')

username = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input")
password = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input")

username.send_keys("REGISTRATION NUMBER HERE")
password.send_keys("PASSWORD HERE")

st = input()

##elem =driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[6]/td/input[1]')
##print('go')
##
##
##elem.click()
##

driver.get('https://vtop.vit.ac.in/addrop/course_home.asp')

elem = driver.find_element_by_xpath('//*[@id="content"]/tbody/tr/td/form/table/tbody/tr[2]/td[1]/input') # radio button
elem.click()
elem3 = driver.find_element_by_xpath('//*[@id="content"]/tbody/tr/td/form/table/tbody/tr[9]/td/input')#submit button
elem3.click()

while True:
    ele1=driver.find_element_by_xpath('//*[@id="content"]/tbody/tr/td/table/tbody/tr[6]/td[11]/input[9]')
    ele1.click()
    elem = driver.find_element_by_xpath('//*[@id="content"]/tbody/tr/td/table[2]/tbody/tr[3]/td[9]/font')
    print(elem.text)
    if elem.text != '0':
        alert= mixer.Sound('bell.wav')
        alert.play()
        s=input()
                           
        
    time.sleep(2)
    ele2=driver.find_element_by_xpath('//*[@id="content"]/tbody/tr/td/input')
    ele2.click()

driver.quit()
pygame.mixer.quit()
