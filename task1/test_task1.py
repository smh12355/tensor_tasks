import Base

def test_human_strenght_search(browser):
    data = Base.TaskSolver(browser)
    data.driver.get(data.base_url)
    assert data.FirstPhraseCheck()