# 06-efficient-locators.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the driver
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    # Navigate to a page
    driver.get('https://www.selenium.dev/documentation/')
    
    # Best Practice 1: Use IDs when available (most efficient)
    search_box = driver.find_element(By.ID, 'search-by')
    print("Found search box using ID")
    
    # Best Practice 2: Use meaningful CSS selectors
    # Bad example (too broad):
    # driver.find_element(By.CSS_SELECTOR, 'div div div a')
    
    # Good example (specific and readable):
    main_header = driver.find_element(By.CSS_SELECTOR, '.hero h1')
    print(f"Main header text: {main_header.text}")
    
    # Best Practice 3: Use XPath wisely
    # Bad XPath (absolute path, brittle):
    # driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div/div/h1')
    
    # Good XPath (relative, more robust):
    header_by_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Selenium')]")
    print(f"Found header by text: {header_by_text.text}")
    
    # Best Practice 4: Create custom locators with CSS combinators
    # Find links within the Getting Started section
    getting_started_links = driver.find_elements(
        By.CSS_SELECTOR, 
        'nav a[href*="getting-started"]'
    )
    print(f"Number of Getting Started links: {len(getting_started_links)}")
    
    # Best Practice 5: Use appropriate methods for the task
    # For example, when working with forms:
    driver.get('https://www.selenium.dev/selenium/web/web-form.html')
    
    # Find the form element
    form = driver.find_element(By.TAG_NAME, 'form')
    
    # Find all input elements within the form
    inputs = form.find_elements(By.TAG_NAME, 'input')
    print(f"Number of input elements in form: {len(inputs)}")
    
    # Best Practice 6: Use parent-child relationships
    # Find dropdown element by its parent-child relationship
    dropdown_parent = driver.find_element(By.CSS_SELECTOR, 'div.form-floating:has(select)')
    dropdown = dropdown_parent.find_element(By.TAG_NAME, 'select')
    print(f"Found dropdown with name: {dropdown.get_attribute('name')}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()