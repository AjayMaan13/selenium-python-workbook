from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the driver
driver = webdriver.Chrome()

try:
    # Navigate to a website with various elements
    driver.get('https://www.python.org')
    
    # 1. Find element by ID
    search_field = driver.find_element(By.ID, "id-search-field")
    print(f"Search field found: {search_field.tag_name}")
    
    # 2. Find element by NAME
    # Let's find the search form
    search_form = driver.find_element(By.NAME, "search")
    print(f"Search form found: {search_form.tag_name}")
    
    # 3. Find element by CLASS_NAME
    # Find the navigation menu
    main_nav = driver.find_element(By.CLASS_NAME, "navigation")
    print(f"Navigation found: {main_nav.tag_name}")
    
    # 4. Find element by TAG_NAME
    # Find the first h1 element
    h1 = driver.find_element(By.TAG_NAME, "h1")
    print(f"H1 content: {h1.text}")
    
    # 5. Find element by LINK_TEXT
    # Find the link to "Downloads"
    downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
    print(f"Downloads link href: {downloads_link.get_attribute('href')}")
    
    # 6. Find element by PARTIAL_LINK_TEXT
    # Find a link containing "Community"
    community_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Community")
    print(f"Community link text: {community_link.text}")
    
    # 7. Find element by CSS_SELECTOR
    # Find the submit button in the search form
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.search-button")
    print(f"Submit button type: {submit_button.get_attribute('type')}")
    
    # 8. Find element by XPATH
    # Find the Python logo
    logo = driver.find_element(By.XPATH, "//img[@class='python-logo']")
    print(f"Logo alt text: {logo.get_attribute('alt')}")
    
    # Finding multiple elements
    # Find all main navigation list items
    nav_items = driver.find_elements(By.CSS_SELECTOR, "#mainnav li")
    print(f"Number of navigation items: {len(nav_items)}")
    for i, item in enumerate(nav_items[:3]):  # Just print the first 3 for brevity
        print(f"  Nav item {i+1}: {item.text}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()