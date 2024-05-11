import pytest
from selenium import webdriver
import logging
from datetime import datetime
import os

@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
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

    # info_logger = logging.getLogger(__name__)
    # current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # log_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'logs',f"info_log_{current_datetime}.log")
    # info_file_handler = logging.FileHandler(log_file_path)
    # info_file_handler.setLevel(logging.INFO)
    # info_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    # info_logger.addHandler(info_file_handler)
    yield debug_logger
    debug_logger.removeHandler(debug_file_handler)
    # debug_logger.removeHandler(info_file_handler)
    debug_file_handler.close()
    # info_file_handler.close()

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
# def pytest_runtest_logreport(report):
#     debug_logger = logging.getLogger(__name__)
#     if report.when == "call":
#         if not hasattr(pytest_runtest_logreport, 'logger_setup_done'):
#             # Настройка логирования производится только один раз
#             debug_logger.setLevel(logging.DEBUG)
#             current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             log_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'logs',f"debug_log_{current_datetime}.log")
#             debug_file_handler = logging.FileHandler(log_file_path)
#             debug_file_handler.setLevel(logging.DEBUG)
#             debug_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
#             debug_logger.addHandler(debug_file_handler)
#             pytest_runtest_logreport.logger_setup_done = True
#     # setup_logging = logging.getLogger(__name__)
#     if report.passed:
#         debug_logger.info(f"Test '{report.nodeid}' passed")
#     elif report.failed:
#         debug_logger.error(f"Test '{report.nodeid}' failed: {report.longreprtext}")
#     elif report.skipped:
#         debug_logger.warning(f"Test '{report.nodeid}' skipped: {report.longreprtext}")
#     elif report.outcome == "xfail":
#         debug_logger.warning(f"Test '{report.nodeid}' expectedly failed: {report.longreprtext}")
#     elif report.outcome == "xpass":
#         debug_logger.error(f"Test '{report.nodeid}' unexpectedly passed: {report.longreprtext}")