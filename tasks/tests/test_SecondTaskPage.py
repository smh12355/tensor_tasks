from pages.SecondTaskPage import SecondTaskPage

def test_RegionCheck(browser, setup_logging):
    secondtaskpage = SecondTaskPage(browser)
    region, list_of_orgs = secondtaskpage.RegionCheck()
    assert region == "Республика Башкортостан", setup_logging.error("region is incorrect")
    assert list_of_orgs != None, setup_logging.error("partner list does not exist")
    assert len(list_of_orgs) > 1, setup_logging.error("There is no organization in the list of partners")

def test_RegionsSwitchCheck(browser, setup_logging):
    secondtaskpage = SecondTaskPage(browser)
    region, list_of_orgs, url, title_of_new_page, new_region, new_list_of_orgs = secondtaskpage.RegionSwitchCheck()
    assert region != new_region, setup_logging.error("the region has not changed")
    assert list_of_orgs != new_list_of_orgs, setup_logging.error("the list of organizations has not changed")
    assert "kamchatskij-kraj" in url, setup_logging.error("incorrect url")
    assert "Камчатский край" in title_of_new_page, setup_logging.error("incorrect web title")