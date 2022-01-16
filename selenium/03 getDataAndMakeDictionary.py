from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\developer_chrome\chromedriver.exe"

s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

event = {}

for n in range(len(event_times)):
    event[n] = {
        "time" : event_times[n].text,
        "name" : event_name[n].text,
    }

print(event)

driver.quit()
