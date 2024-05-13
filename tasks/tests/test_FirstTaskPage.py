from pages.FirstTaskPage import FirstTaskPage
import logging

def test_first_task_first(browser, setup_logging):
    firsttaskpage = FirstTaskPage(browser)
    assert firsttaskpage.FindFirstPhrase(), setup_logging.error('The block "Strength is in people" is not in the html code')

def test_first_task_second(browser, setup_logging):
    firsttaskpage = FirstTaskPage(browser)
    output = firsttaskpage.TextLinkOpen()
    assert output[0] == output[1], setup_logging.error("the link redirects to a third-party resource")

def test_first_task_third(browser, setup_logging):
    firsttaskpage = FirstTaskPage(browser)
    output = firsttaskpage.SizeOfPictures()
    height = output[0].get_attribute('height')
    width = output[0].get_attribute('width')
    for var in output[1:]:
        assert var.get_attribute('height') == height, setup_logging.error("images have different heights")
        assert var.get_attribute('width') == width, setup_logging.error("images have different widths")

def test_Download_plagin(browser_for_download, setup_logging):
    thirdtaskpage = FirstTaskPage(browser_for_download)
    size, pre_size = thirdtaskpage.DownloadCheck()
    assert str(size) == pre_size, setup_logging.error("different size")