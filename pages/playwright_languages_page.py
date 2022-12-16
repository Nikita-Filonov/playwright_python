from playwright.sync_api import Page

from page_factory.title import Title
from pages.base_page import BasePage


class PlaywrightLanguagesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.language_title = Title(
            page, locator='h2#{language}', name='Language title'
        )

    def language_present(self, language: str):
        self.language_title.should_be_visible(language=language)
        self.language_title.should_have_text(
            language.capitalize(), language=language
        )
