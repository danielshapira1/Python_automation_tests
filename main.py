from test_utils import set_driver
from elements_tests import run_elements_tests
from practice_form_tests import run_practice_form_tests
from alerts_windows_tests import run_alerts_windows_tests


def main():
    driver = set_driver("https://demoqa.com/")
    if driver:
        try:
            run_alerts_windows_tests(driver)
            run_elements_tests(driver)
            run_practice_form_tests(driver)

        finally:
            driver.quit()
        print("All tests completed!")
    else:
        print("Driver setup failed. Unable to run tests.")

if __name__ == "__main__":
    main()