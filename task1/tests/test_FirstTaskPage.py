from pages.FirstTaskPage import FirstTaskPage

def test_first_task_first(browser):
    firsttaskpage = FirstTaskPage(browser)
    assert firsttaskpage.FindFirstPhrase(), 'Блока "Сила в людях" нету в html коде'

def test_first_task_second(browser):
    firsttaskpage = FirstTaskPage(browser)
    output = firsttaskpage.TextLinkOpen()
    # print(output)
    assert output[0] == None, "ссылка недействительна"
    assert output[1] == output[2], "ссылка редиректит на сторонний ресурс"

def test_first_task_third(browser):
    firsttaskpage = FirstTaskPage(browser)
    output = firsttaskpage.SizeOfPictures()
    height = output[0].get_attribute('height')
    width = output[0].get_attribute('width')
    for var in output[1:]:
        assert var.get_attribute('height') == height, "изображения имеют разную высоту"
        assert var.get_attribute('width') == width, "изображения имеют разную ширину"