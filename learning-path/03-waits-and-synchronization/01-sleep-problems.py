# 01-sleep-problems.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to a dynamic page
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    
    # Find and click the start button
    start_button = driver.find_element(By.CSS_SELECTOR, 'div#start button')
    start_button.click()
    
    # Bad practice: using a fixed sleep time
    print("Waiting with fixed sleep...")
    time.sleep(5)  # This might be too short or too long
    
    # Try to get the text that appears after loading
    finish_text = driver.find_element(By.CSS_SELECTOR, 'div#finish h4')
    print(f"Loaded text: {finish_text.text}")
    
    # Problem: If the page loads faster, we waste time waiting
    # If the page loads slower, the test will fail
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()