# 05-element-properties.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the driver
driver = webdriver.Chrome()

try:
    # Navigate to a page
    driver.get('https://the-internet.herokuapp.com/')
    
    # Find an element
    link = driver.find_element(By.LINK_TEXT, 'Form Authentication')
    
    # Get element properties and attributes
    print(f"Tag name: {link.tag_name}")
    print(f"Text: {link.text}")
    print(f"Href attribute: {link.get_attribute('href')}")
    print(f"Class attribute: {link.get_attribute('class')}")
    
    # Check element state
    print(f"Is displayed: {link.is_displayed()}")
    print(f"Is enabled: {link.is_enabled()}")
    
    # Get element size and location
    print(f"Size: {link.size}")
    print(f"Location: {link.location}")
    
    # Navigate to a page with a button
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    
    # Find the Add Element button
    add_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    
    # Click it a few times to add elements
    for i in range(3):
        add_button.click()
        print(f"Added element {i+1}")
        time.sleep(0.5)
    
    # Find all delete buttons
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
    print(f"Number of delete buttons: {len(delete_buttons)}")
    
    # Get CSS values
    delete_button = delete_buttons[0]
    print(f"Background color: {delete_button.value_of_css_property('background-color')}")
    print(f"Font size: {delete_button.value_of_css_property('font-size')}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()