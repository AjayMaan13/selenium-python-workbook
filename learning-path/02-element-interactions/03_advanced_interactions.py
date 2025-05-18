# 03-advanced-interactions.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the driver
driver = webdriver.Chrome()

try:
    # Example 1: Dropdown selection (using HTML Select)
    driver.get('https://the-internet.herokuapp.com/dropdown')
    
    # Find the dropdown element
    dropdown = Select(driver.find_element(By.ID, 'dropdown'))
    
    # Select by visible text
    dropdown.select_by_visible_text('Option 1')
    print("Selected 'Option 1'")
    time.sleep(1)
    
    # Select by value
    dropdown.select_by_value('2')
    print("Selected option with value '2'")
    time.sleep(1)
    
    # Select by index
    dropdown.select_by_index(1)  # Index is zero-based
    print("Selected option at index 1")
    time.sleep(1)
    
    # Example 2: Checkboxes
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    
    # Find checkboxes
    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    
    # Check if checkbox is selected and toggle it
    for i, checkbox in enumerate(checkboxes):
        print(f"Checkbox {i+1} is selected: {checkbox.is_selected()}")
        checkbox.click()
        print(f"Checkbox {i+1} is now selected: {checkbox.is_selected()}")
        time.sleep(1)
    
    # Example 3: Mouse hover
    driver.get('https://the-internet.herokuapp.com/hovers')
    
    # Find the elements to hover over
    figures = driver.find_elements(By.CSS_SELECTOR, '.figure')
    
    # Create ActionChains instance
    actions = ActionChains(driver)
    
    # Hover over the first figure
    actions.move_to_element(figures[0]).perform()
    print("Hovered over first figure")
    time.sleep(1)
    
    # Check if the caption is visible
    caption = driver.find_element(By.XPATH, "//div[@class='figcaption']/h5")
    print(f"Caption text: {caption.text}")
    
    # Example 4: Drag and Drop
    driver.get('https://the-internet.herokuapp.com/drag_and_drop')
    
    # Find source and target elements
    source = driver.find_element(By.ID, 'column-a')
    target = driver.find_element(By.ID, 'column-b')
    
    # Perform drag and drop
    print("Attempting drag and drop...")
    actions.drag_and_drop(source, target).perform()
    time.sleep(2)
    
    # Example 5: Right-click (Context menu)
    driver.get('https://the-internet.herokuapp.com/context_menu')
    
    # Find the element to right-click
    hot_spot = driver.find_element(By.ID, 'hot-spot')
    
    # Perform right-click
    actions.context_click(hot_spot).perform()
    print("Right-clicked on hot spot")
    time.sleep(1)
    
    # Handle the alert
    alert = driver.switch_to.alert
    print(f"Alert text: {alert.text}")
    alert.accept()
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()