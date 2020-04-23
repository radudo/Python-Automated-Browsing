#Automated Web Browsing Example For Login or Completeing fields using Selenium 
# This works for any website or fields on this example I have used a simple facebook Login
# Dependecies:
# Selenium , ChromeDriver (install using pip3)
from selenium import webdriver
import time
#Number Of clicks
for i in range(0,50):
  

    driver = webdriver.Chrome()
    driver.get('https://soundcloud.com/radudo/')

    #Use the Google Chrome Inspector Tool To get the path of the field
    login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')


    #Actions
    login_button.click()
    time.sleep(5)

    driver.quit()
print('Done')
