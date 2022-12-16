from playwright.sync_api import Page

from components.modals.search_modal import SearchModal
from page_factory.button import Button
from page_factory.link import Link


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_modal = SearchModal(page)

        self.api_link = Link(page, locator="//a[text()='API']", name='API')
        self.docs_link = Link(page, locator="//a[text()='Docs']", name='Docs')
        self.search_button = Button(
            page, locator="button.DocSearch-Button", name='Search'
        )

    def visit_docs(self):
        self.docs_link.click()

    def visit_api(self):
        self.api_link.click()

    def open_search(self):
        self.search_button.should_be_visible()

        self.search_button.hover()
        self.search_button.click()

        self.search_modal.modal_is_opened()
