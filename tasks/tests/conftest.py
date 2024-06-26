import pytest
from selenium import webdriver
import logging
from datetime import datetime
import os
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def browser_for_download():
    options = Options()
    download_dir = os.path.dirname(__file__)
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_argument("--allow-running-insecure-content")  # Allow insecure content
    options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://sbis.ru/download?tab=plugin&innerTab=default")
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    debug_logger = logging.getLogger(__name__)
    debug_logger.setLevel(logging.DEBUG)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(os.path.dirname(__file__),
                                '..', 
                                'logs',
                                f"debug_log_{current_datetime}.log")
    debug_file_handler = logging.FileHandler(log_file_path)
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    debug_logger.addHandler(debug_file_handler)
    yield debug_logger
    debug_logger.removeHandler(debug_file_handler)
    debug_file_handler.close()

def pytest_runtest_logreport(report):
    setup_logging = logging.getLogger(__name__)
    if report.when == "call":
        if report.passed:
            setup_logging.info(f"Test '{report.nodeid}' passed")
        elif report.failed:
            setup_logging.error(f"Test '{report.nodeid}' failed: {report.longreprtext}")
        elif report.skipped:
            setup_logging.warning(f"Test '{report.nodeid}' skipped: {report.longreprtext}")
        elif report.outcome == "xfail":
            setup_logging.warning(f"Test '{report.nodeid}' expectedly failed: {report.longreprtext}")
        elif report.outcome == "xpass":
            setup_logging.error(f"Test '{report.nodeid}' unexpectedly passed: {report.longreprtext}")