from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_utils import wait_and_click, wait_between_actions

def test_browser_windows(driver):
    driver.get("https://demoqa.com/browser-windows")
    wait_between_actions()
    
    original_window = driver.current_window_handle
    
    # Test New Tab
    wait_and_click(driver, (By.ID, "tabButton"))
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    assert "This is a sample page" in driver.find_element(By.ID, "sampleHeading").text
    driver.close()
    driver.switch_to.window(original_window)
    wait_between_actions()
    
    # Test New Window
    wait_and_click(driver, (By.ID, "windowButton"))
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    assert "This is a sample page" in driver.find_element(By.ID, "sampleHeading").text
    driver.close()
    driver.switch_to.window(original_window)
    wait_between_actions()

def test_alerts(driver):
    driver.get("https://demoqa.com/alerts")
    wait_between_actions()
    
    # Test simple alert
    wait_and_click(driver, (By.ID, "alertButton"))
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert "You clicked a button" in alert.text
    alert.accept()
    wait_between_actions()
    
    # Test timed alert
    wait_and_click(driver, (By.ID, "timerAlertButton"))
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert "This alert appeared after 5 seconds" in alert.text
    alert.accept()
    wait_between_actions()
    
    # Test confirm alert
    wait_and_click(driver, (By.ID, "confirmButton"))
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()
    result = driver.find_element(By.ID, "confirmResult").text
    assert "You selected Ok" in result
    wait_between_actions()
    
    # Test prompt alert
    wait_and_click(driver, (By.ID, "promtButton"))
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.send_keys("Test User")
    alert.accept()
    result = driver.find_element(By.ID, "promptResult").text
    assert "You entered Test User" in result
    wait_between_actions()

def test_frames(driver):
    driver.get("https://demoqa.com/frames")
    wait_between_actions()
    
    # Test first frame
    driver.switch_to.frame("frame1")
    frame_text = driver.find_element(By.ID, "sampleHeading").text
    assert "This is a sample page" in frame_text
    driver.switch_to.default_content()
    wait_between_actions()
    
    # Test second frame
    driver.switch_to.frame("frame2")
    frame_text = driver.find_element(By.ID, "sampleHeading").text
    assert "This is a sample page" in frame_text
    driver.switch_to.default_content()
    wait_between_actions()

def run_alerts_windows_tests(driver):
    test_browser_windows(driver)
    test_alerts(driver)
    test_frames(driver)