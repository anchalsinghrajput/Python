from selenium import webdriver

chrome_driver_path = "C:\developer_chrome/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")          #opening amazon website

#driver.close()    //closes the current tab

driver.quit()    #quit the entire programe
