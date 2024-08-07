from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
import time

def wait_between_actions(duration=0.2):
    time.sleep(duration)

def move_to_element(driver, element):
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.5)  # Wait for scroll to complete

def set_driver(URL):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        return driver
    except WebDriverException as e:
        print(f"WebDriver error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while setting up the driver: {e}")
        return None

def wait_and_click(driver, locator, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable(locator))

            if not element.is_displayed():
                move_to_element(driver, element)
                
            # Try to click using JavaScript
            driver.execute_script("arguments[0].click();", element)
            
            wait_between_actions()
            return
        except (TimeoutException, ElementClickInterceptedException) as e:
            if attempt == max_attempts - 1:
                print(f"Failed to click element {locator} after {max_attempts} attempts")
                raise e
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(2)

def wait_and_send_keys(driver, locator, text, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located(locator))
            if not element.is_displayed():
                move_to_element(driver, element)
            
            # Clear the field (in case it's not empty)
            driver.execute_script("arguments[0].value = '';", element)
            
            # Send keys using JavaScript
            driver.execute_script(f"arguments[0].value = '{text}';", element)
            
            # Trigger change event
            driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", element)
            
            wait_between_actions()
            return
        except (TimeoutException, ElementNotInteractableException) as e:
            if attempt == max_attempts - 1:
                print(f"Failed to send keys to element {locator} after {max_attempts} attempts")
                raise e
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(2)

def wait_and_select_dropdown(driver, locator, option_text, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            wait = WebDriverWait(driver, 10)
            
            # Find the dropdown element
            dropdown = wait.until(EC.presence_of_element_located(locator))
            
            if not dropdown.is_displayed():
                move_to_element(driver, dropdown)
            
            # Click to open the dropdown
            driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(0.5)  # Wait for dropdown to open
            
            # Find and click the option
            option_xpath = f"//div[contains(@class, 'css-') and text()='{option_text}']"
            option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
            time.sleep(0.5)  # Wait for scroll to complete
            driver.execute_script("arguments[0].click();", option)
            
            wait_between_actions()
            return
        except (TimeoutException, ElementClickInterceptedException) as e:
            if attempt == max_attempts - 1:
                print(f"Failed to select dropdown {locator} or option {option_text} after {max_attempts} attempts")
                raise e
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(2)

def dismiss_overlay(driver):
    try:
        overlay = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0"))
        )
        driver.execute_script("arguments[0].remove();", overlay)
        wait_between_actions()
    except TimeoutException:
        print("No overlay found or unable to remove it.")