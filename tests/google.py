from selene.support.shared import browser
from selene import be, have


def test_q():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_search_no_info():
    browser.element('[name="q"]').should(be.blank).type('dsffdfdsf32432').press_enter()
    browser.element('p[role="heading"]').should(have.text('По запросу dsffdfdsf32432 ничего не найдено.'))

