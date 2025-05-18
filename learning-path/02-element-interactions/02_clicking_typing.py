# 02-clicking-and-typing.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the driver
driver = webdriver.Chrome()

try:
    # Navigate to Python.org
    driver.get('https://www.python.org')
    
    # Find the search field
    search_field = driver.find_element(By.ID, "id-search-field")
    
    # Type into the search field
    search_field.clear()  # Clear any existing text
    search_field.send_keys("web testing")
    print("Typed 'web testing' in search field")
    time.sleep(1)
    
    # Submit the search form (press Enter)
    search_field.send_keys(Keys.RETURN)
    print("Submitted search")
    time.sleep(2)
    
    # Verify we're on the search results page
    print(f"Current URL: {driver.current_url}")
    
    # Find search results
    search_results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
    print(f"Number of search results: {len(search_results)}")
    
    # Navigate back to the home page
    driver.back()
    time.sleep(1)
    
    # Find and click on the Downloads link
    downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
    downloads_link.click()
    print("Clicked on Downloads link")
    time.sleep(2)
    
    # Verify we're on the Downloads page
    if "Download" in driver.title:
        print("Successfully navigated to Downloads page")
    else:
        print(f"Unexpected page title: {driver.title}")
        
    # Find and click on one of the download buttons
    try:
        download_button = driver.find_element(By.CSS_SELECTOR, ".download-os-windows")
        download_button.click()
        print("Clicked on Windows download button")
        time.sleep(1)
    except Exception as e:
        print(f"Could not find Windows download button: {e}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()