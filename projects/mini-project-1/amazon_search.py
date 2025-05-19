# A small project to get the names of all the top imbd rated series with their names and stars

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome()


try:
    #seriesList = []
    #{"name": [], "rating": []}
    driver.get('https://www.imdb.com/fr/chart/toptv/')


    seriesList = driver.find_elements(By.XPATH, '//a//h3')
    
    for i in seriesList:
        if i.text[0].isdigit():
            print(i.text)

   
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()