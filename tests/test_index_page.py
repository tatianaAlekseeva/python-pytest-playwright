import pytest
import pages
import time


class TestFooter:

    def test_the_main_search_button_must_have_the_text_google_search(self, page):
        pages.index_page.open_index_page(page)
        time.sleep(10)
