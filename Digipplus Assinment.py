from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from sqlalchemy import false
import os
import csv


def open(url):
   path = r'C:\DATA\web Scraping\chromedriver-mac-x64\chromedriver'
   webdriver.chrome.driver = path
   options = Options()
   driver = webdriver.Chrome(options=options)
   wait = WebDriverWait(driver, 300)
   driver.get(url)
   
   elements = driver.find_elements(By.XPATH, "//a[@class='hfpxzc']")
   for element in elements:
      # print(element.text)
      link = (element.get_attribute('href'))
      links.append(link)
      element.click()
      wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Suggest an edit']")))
      time.sleep(3)
      name_ele = driver.find_element(By.XPATH, "//h1[@class = 'DUwDvf lfPIob']")
      names.append(name_ele.text)
      rating_ele = driver.find_element(By.XPATH, "//div[@class='skqShb ']/div/div[2]/span/span")
      ratings.append(rating_ele.text)
      add_ele = driver.find_element(By.XPATH, "//button[@data-item-id='address']/div/div[2]/div[1]")
      addresses.append(add_ele.text)
      
      try:
         phon_no_ele = driver.find_element(By.XPATH, "//button[@data-tooltip='Copy phone number']/div/div[2]/div[1]")
         phone_nos.append(phon_no_ele.text)
      except:
         phone_nos.append("")
      
      plus_code_ele = driver.find_element(By.XPATH, "//button[@data-tooltip='Copy plus code']/div/div[2]/div[1]")
      plus_codes.append(plus_code_ele.text)
      
      # link_ele = driver.find_element(By.XPATH, "")
   driver.quit()

# keyword = input("Enter type of bussiness and location: ")
keyword = "food in delhi india"
keyword = keyword.replace(" ", "+")
url = "https://www.google.com/maps/search/" + keyword
names=[]
ratings=[]
addresses=[]
phone_nos=[]
plus_codes=[]
links=[]
open(url)

df = pd.DataFrame({
   "Name":names, 
   "Rating":ratings,
   "Address":addresses,
   "Phone No":phone_nos,
   "Plus code":plus_codes,
   "Link":links
})
df.to_csv('data.csv', index=false)
print(df)
