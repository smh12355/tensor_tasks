from pages.FirstTaskPageThird import FirstTaskPageThird

def test_first_task_third(browser):
    firsttaskpage = FirstTaskPageThird(browser)
    output = firsttaskpage.SizeOfPictures()
    height = output[0].get_attribute('height')
    width = output[0].get_attribute('width')
    for var in output[1:]:
        assert var.get_attribute('height') == height, "изображения имеют разную высоту"
        assert var.get_attribute('width') == width, "изображения имеют разную ширину"