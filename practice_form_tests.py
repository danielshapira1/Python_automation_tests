from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from test_utils import wait_and_click, wait_and_send_keys, wait_and_select_dropdown, dismiss_overlay, wait_between_actions

def fill_practice_form(driver):
    wait_between_actions()
    dismiss_overlay(driver)
    
    wait_and_send_keys(driver, (By.ID, "firstName"), "Daniel")
    wait_and_send_keys(driver, (By.ID, "lastName"), "Shapira")
    wait_and_send_keys(driver, (By.ID, "userEmail"), "Danielshapira14@gmail.com")
    
    wait_and_click(driver, (By.XPATH, "//label[text()='Male']"))
    
    wait_and_send_keys(driver, (By.ID, "userNumber"), "1234567890")
    
    dob_input = driver.find_element(By.ID, "dateOfBirthInput")

    # delete currnt input
    dob_input.send_keys(Keys.CONTROL + "a")
    wait_between_actions()
    dob_input.send_keys("10 oct 1997")
    wait_between_actions()
    dob_input.send_keys(Keys.ENTER)
    wait_between_actions()
    
    subjects_input = driver.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Math")
    wait_between_actions()
    subjects_input.send_keys(Keys.ENTER)
    wait_between_actions()
    subjects_input.send_keys("English")
    wait_between_actions()
    subjects_input.send_keys(Keys.ENTER)
    wait_between_actions()
    
    wait_and_click(driver, (By.XPATH, "//label[text()='Sports']"))
    wait_and_click(driver, (By.XPATH, "//label[text()='Reading']"))
    
    wait_and_send_keys(driver, (By.ID, "currentAddress"), "123 Test Street, Test City, 12345")
    
    
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", submit_button)
    wait_between_actions()

def verify_submission(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
        modal_body = driver.find_element(By.CLASS_NAME, "modal-body")
        print("Submitted Information:")
        print(modal_body.text)
        return True
    except TimeoutException:
        print("Submission verification failed: Modal not found")
        return False

def run_practice_form_tests(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    fill_practice_form(driver)
    assert verify_submission(driver), "Practice form submission failed"