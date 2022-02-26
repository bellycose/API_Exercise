#Test module

from src.page import SearchPhrase
from src.phrase import ResultPhrase


def test_phrase(browser): #fixture will be called and run that module and insert that value into the arguement to commence the clean up. Dependency injection.
    search_page = SearchPhrase(browser)
    result_page = ResultPhrase(browser)
    PHRASE = "Trigonometry"

    #Given the homepage is displayed
    search_page.load()

    #When user searches for 'phrase'
    search_page.search(PHRASE)

    #Then search result title contains 'phrase'
    assert PHRASE in result_page.title()

    #And the search result is 'phrase'
    assert PHRASE == result_page.search_input_value()

    #And the search result links pertain to 'phrase'
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches)>0

    raise Exception("Incomplete Test")
