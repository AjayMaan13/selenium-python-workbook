# 04-form-interactions.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the driver
driver = webdriver.Chrome()

try:
    # Navigate to a login form page
    driver.get('https://the-internet.herokuapp.com/login')
    
    # Find username and password fields
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    
    # Type in credentials
    username_field.send_keys('tomsmith')
    password_field.send_keys('SuperSecretPassword!')
    
    # Find and click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
    
    time.sleep(2)
    
    # Check if login was successful
    if "secure" in driver.current_url:
        print("Login successful!")
        
        # Find and display flash message
        flash_message = driver.find_element(By.ID, 'flash')
        print(f"Flash message: {flash_message.text}")
        
        # Find and click logout
        logout_button = driver.find_element(By.CSS_SELECTOR, '.button.secondary')
        logout_button.click()
        print("Logged out")
        
    else:
        print("Login failed")
    
    time.sleep(2)
    
    # Try with incorrect credentials
    driver.get('https://the-internet.herokuapp.com/login')
    
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    
    username_field.send_keys('incorrectuser')
    password_field.send_keys('wrongpassword')
    
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
    
    time.sleep(2)
    
    # Check error message
    flash_message = driver.find_element(By.ID, 'flash')
    print(f"Error message: {flash_message.text}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()