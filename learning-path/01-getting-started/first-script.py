## Set Up Virtual Environment: ##
# python -m venv venv
# source venv/bin/activate  # On Windows: venv\Scripts\activate
# pip install -r requirements.txt


# 01-first-script.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


# Set up the driver
# We use ChromeDriverManager to automatically download and set up the appropriate version of ChromeDriver.
#service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

## Understanding WebDriver ##
# WebDriver is the core component that allows Selenium to control browsers. Here's what you should know:

#1. Browser Abstraction: WebDriver provides a unified API to interact with different browsers.
#2. Browser Communication: It communicates with the browser through browser-specific drivers.
#3. Stateless: Each command is sent independently to the browser.

# We use a try-finally block to ensure the browser is closed properly with driver.quit() 
# even if an error occurs.
try:
    # Open a website
    driver.get('https://www.python.org')
    
    # Print the title of the page
    print(f"Title: {driver.title}")

    # Wait for a few seconds to see the result
    time.sleep(3)

    # Get current URL
    print(f"Current URL: {driver.current_url}")

    # Get page source
    # print(f"Page Source: {driver.page_source}")  # This would be long, so I commented it out
    # Lets write it in file
    with open('page_source.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    
    # Navigate to another site
    driver.get('https://www.python.org')
    time.sleep(1)
    
    # Go back to the previous page
    driver.back()
    time.sleep(1)
    
    # Go forward
    driver.forward()
    time.sleep(1)
    
    # Refresh the page
    driver.refresh()
    time.sleep(1)
    
finally:
    # Close the browser
    driver.quit()