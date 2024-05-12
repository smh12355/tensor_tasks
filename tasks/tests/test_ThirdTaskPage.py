from pages.ThirdTaskPage import ThirdTaskPage

def test_Download_plagin(browser_for_download):
    thirdtaskpage = ThirdTaskPage(browser_for_download)
    size, pre_size = thirdtaskpage.DownloadCheck()
    assert str(size) == pre_size