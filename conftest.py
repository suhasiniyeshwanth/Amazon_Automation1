import pytest
from source.utilities.properties import ReadConfig
from source.utilities import webdriver_manager as manager, helper


@pytest.fixture(scope='session', autouse=True)
def set_property():
    yield
    ReadConfig.write_to_report()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_"+rep.when, rep)


@pytest.fixture(scope="function", params=[ReadConfig.get_browser()], autouse=True)
def setup(request):
    browser_name = request.param
    url = ReadConfig.get_url()
    driver = manager.start_browser(browser_name, url)
    if request is not None:
        request.node.driver = driver
    yield
    if request.node.rep_call.failed:
        helper.attach_screen_shot(driver, request.function.__name__)
    driver.quit()

