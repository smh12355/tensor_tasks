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
