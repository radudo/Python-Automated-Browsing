#Automated Web Browsing Example For Login or Completeing fields using Selenium 
# This works for any website or fields on this example I have used a simple facebook Login
# Dependecies:
# Selenium , ChromeDriver (install using pip3)
for i in range(0,2):
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')

    #Use the Google Chrome Inspector Tool To get the path of the field
    login_acc = driver.find_element_by_xpath('//*[@id="email"]')
    login_pass = driver.find_element_by_xpath('//*[@id="pass"]')
    login_button = driver.find_element_by_xpath('//*[@id="u_0_b"]')


    #Actions
    login_acc.send_keys('acc')
    login_pass.send_keys('pass')
    login_button.click()
  
    driver.quit()
print('Done')
