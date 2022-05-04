from faker import Faker
from selene import have, be, by
from selene.support.shared import browser

from model.controls import Dropdown
from python_web_test_kit.helpers.reporting import step


class Test:

    faker = Faker()

    first_name = faker.first_name()

    def test_successfulFillFormSignUp(self):
        @step("Open signup")
        def _():
            browser.open("/accounts/sign-up")
            Dropdown('[name=country]').select('Argentina')
            browser.element('[type=email]').click().type(self.faker.email())
            browser.element('[type=password]').click().type('kl234DRf23dsf').press_enter() #TO DO вынести в фикстуру, а пароль в env
            browser.element('[aria-label=Close]').click()
            browser.should(have.url_containing("https://my.exness.com/webtrading/"))

    def test_search(self):
        @step("Search")
        def _():
            browser.open("/accounts/sign-in")
            browser.element('[type=email]').click().type('jameslisa@hotmail.com')
            browser.element('[type=password]').click().type('kl234DRf23dsf').press_enter() #TO DO вынести в фикстуру, а пароль в env
            browser.open("/webtrading/")
            browser.element('[data-test=nav-button-watchlist]').click()
            browser.element('[data-test=asset-popup-search]').type('AAPL')

    def test_auth(self):
        @step("Auth")
        def _():
            browser.open("/accounts/sign-in")
            browser.element('[type="email"]').click().type('jameslisa@hotmail.com')
            browser.element('[type="password"]').click().type('kl234DRf23dsf').press_enter() #TO DO вынести в фикстуру
            browser.should(have.url_containing("https://my.exness.com/pa/"))









