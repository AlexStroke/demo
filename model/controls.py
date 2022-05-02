from selene.support.shared.jquery_style import s
from selene.support.shared import browser
from selene import have, be, by

class Dropdown:
    def __init__(self, selector: str):
        self.selector = selector

    def select(self, text):
        browser.element(self.selector).click()
        browser.element('//exwc-dropdown/div').all('exwc-option').element_by(
            have.text(text)).click()  # TO DO рандомный выбор страны из дропданута