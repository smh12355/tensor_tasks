from pages.FirstTaskPage import FirstTaskPage

def test_first_task_first(browser):
    firsttaskpage = FirstTaskPage(browser)
    assert firsttaskpage.FindFirstPhrase()