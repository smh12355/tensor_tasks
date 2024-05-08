from pages.FirstTaskPage import FirstTaskPage

def test_first_task_first(browser):
    firsttaskpage = FirstTaskPage(browser)
    assert firsttaskpage.FindFirstPhrase()

def test_first_task_second(browser):
    firsttaskpage = FirstTaskPage(browser)
    assert firsttaskpage.TextLinkOpen() < 400