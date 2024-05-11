from pages.FirstTaskPage import FirstTaskPage
import logging

def test_first_task_first(browser, setup_logging):
    firsttaskpage = FirstTaskPage(browser)
    assert firsttaskpage.FindFirstPhrase(), setup_logging.error('The block "Strength is in people" is not in the html code')
    # assert 0 == 1, setup_logging.error("some mistake here")

def test_first_task_second(browser, setup_logging):
    firsttaskpage = FirstTaskPage(browser)
    output = firsttaskpage.TextLinkOpen()
    # assert output[0] != None, setup_logging.error("link is invalid")
    assert output[0] == output[1], setup_logging.error("the link redirects to a third-party resource")
