from selenium import webdriver
from source.utilities import globals
from source.utilities.properties import ReadConfig


chrome_capabilities = {
"browserName": "chrome",
"platform": "WIN10"
}

firefox_capabilities = {
"browserName": "firefox",
"platform": "WIN10"
}


def start_browser(browser_name, url):
    driver = None
    if browser_name == "Chrome" or browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=globals.CHROME_PATH)
        '''driver = webdriver.Remote(command_executor="http://192.168.1.156:4445/wd/hub"
                                  , desired_capabilities=chrome_capabilities)'''
    elif browser_name == "Firefox" or browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=globals.FIREFOX_PATH)
        '''driver = webdriver.Remote(command_executor="http://192.168.1.156:4445/wd/hub"
                                  , desired_capabilities=firefox_capabilities)'''
    driver.implicitly_wait(ReadConfig.get_implicit_wait())
    driver.maximize_window()
    driver.get(url)

    return driver
