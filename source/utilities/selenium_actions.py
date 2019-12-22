from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from source.utilities.properties import ReadConfig


def switch_to_child_window(driver):
    child_window = None
    parent_window = driver.current_window_handle
    window_ids = driver.window_handles
    try:
        for window_id in window_ids:
            if window_id != parent_window:
                child_window = window_id
                break
        driver.switch_to.window(child_window)
    except Exception:
        print("Unable to change the focus to the child window")

class Actions:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def move_to_element(self, element):
        self.action.move_to_element(element).perform()

    def action_click(self, element):
        self.action.perform()


class Alert:

    @staticmethod
    def __get_alert(driver):
        wait = WebDriverWait(driver, ReadConfig.get_explicit_wait())
        return wait.until(ec.alert_is_present(), "Alert is not present")

    @staticmethod
    def accept_alert(driver):
        alert = Alert.__get_alert(driver)
        alert.accept()

    @staticmethod
    def dismiss_alert(driver):
        alert = Alert.__get_alert(driver)
        alert.dismiss()

    @staticmethod
    def get_alert_text(driver):
        alert = Alert.__get_alert(driver)
        return alert.text
