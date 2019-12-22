from time import sleep
import allure
from pathlib import Path
import os


def delete_all_files_in_directory(directory_path):
    path = Path(directory_path)
    files_in_path = path.iterdir()

    for item in files_in_path:
        if item.is_file():
            os.remove(directory_path + item.name)
    sleep(5)


def attach_screen_shot(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name,
                  attachment_type=allure.attachment_type.PNG)


