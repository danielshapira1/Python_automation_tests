from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_utils import wait_and_click, wait_and_send_keys, wait_between_actions

def test_text_box(driver):
    driver.get("https://demoqa.com/text-box")
    wait_between_actions()

    wait_and_send_keys(driver, (By.ID, "userName"), "daniel shap")
    wait_and_send_keys(driver, (By.ID, "userEmail"), "daniel@gmail.com")
    wait_and_send_keys(driver, (By.ID, "currentAddress"), "123 Main St")
    wait_and_send_keys(driver, (By.ID, "permanentAddress"), "456 other Ave")
    
    wait_and_click(driver, (By.ID, "submit"))
    
    wait_between_actions()
    output = driver.find_element(By.ID, "output").text
    assert "daniel shap" in output, "Name not found in output"
    assert "daniel@gmail.com" in output, "Email not found in output"

def test_check_box(driver):
    driver.get("https://demoqa.com/checkbox")
    wait_between_actions()

    wait_and_click(driver, (By.XPATH, "//button[@title='Expand all']"))
    wait_and_click(driver, (By.XPATH, "//span[text()='Documents']"))
    wait_between_actions()
    result = driver.find_element(By.ID, "result").text
    assert "documents" in result.lower(), "Documents not checked"

def test_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")
    wait_between_actions()

    wait_and_click(driver, (By.XPATH, "//label[@for='yesRadio']"))
    wait_between_actions()
    result = driver.find_element(By.CLASS_NAME, "text-success").text
    assert result == "Yes", f"Expected 'Yes', but got '{result}'"

def run_elements_tests(driver):
    test_text_box(driver)
    test_check_box(driver)
    test_radio_button(driver)