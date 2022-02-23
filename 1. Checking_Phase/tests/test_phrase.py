#Test module for search engine. Written in functional programming.

from pages.result import ResultPage #Error for Pages. can be ignored.
from pages.phrase import Page

def test_phrase(browser):
    phrase_page = Page(browser)
    result_page = ResultPage(browser)
    PHRASE = "trigonometry"
    
    # Given the DuckDuckGo home page is displayed
    Page.load()

    # When the user searches for "panda"
    Page.search(PHRASE)

    # Then the search result query is "panda"
    assert PHRASE in result_page.title()
  
    # And the search result links pertain to "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result title contains "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0