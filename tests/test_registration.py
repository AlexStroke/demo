from faker import Faker
from selene import have, be, by
from selene.support.shared import browser

from model.controls import Dropdown
from python_web_test_kit.helpers.reporting import step


class TestFirst:

    faker = Faker()

    first_name = faker.first_name()

    def test_successfulFillFormSignUp(self):

        @step("Open signup") #TO DO локаторы
        def _():
            browser.open("/accounts/sign-up")
            Dropdown('[name="country"]').select('Argentina')
            browser.element('[type="email"]').click().type(self.faker.email())
            browser.element('[type="password"]').click().type('kl234DRf23dsf').press_enter() ## TO DO рандомный пароль без спецсимволов
            browser.should(have.url_containing("https://my.exness.com/webtrading/"))







