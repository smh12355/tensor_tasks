import pytest
from selenium import webdriver
import Base

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_human_strenght_search(browser):
    data = Base.TaskSolver(browser)
    data.driver.get(data.base_url)
    assert data.FirstPhraseCheck(), "блок не содержится на странице"