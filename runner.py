from time import sleep

import pytest
from source.utilities import globals, helper
from datetime import datetime
import os


class ReportPlugin:

    def pytest_sessionfinish(self):
        globals.ALLURE_REPORTS = globals.ALLURE_REPORTS + datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        os.popen("allure generate "+globals.ALLURE_RESULTS + " --output " + globals.ALLURE_REPORTS)


# Deleting the Json files of previous execution
#helper.delete_all_files_in_directory(globals.ALLURE_RESULTS)

requirement_file_path = "./requirements.txt"
com = os.path.abspath(requirement_file_path)
command = "pip install -r " + com
os.system(command)
sleep(3)

argument = ['-q', '--alluredir', globals.ALLURE_RESULTS]
pytest.main(argument, plugins=[ReportPlugin()])
