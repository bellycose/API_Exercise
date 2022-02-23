#This module contains the website's URL search result page and it's page-object. Written in OOP. Get something.

from selenium.webdriver.common.by import By

class ResultPage:
    
    # Locator
    RESULT_LINKS = (By.CSS_SELECTOR,"a.result__a")
    SEARCH_INPUT = (By.ID, "search_form_input")

    # Initializer
    def __init__(self,browser):
        self.browser = browser

    # Interaction Methods
    def result_link_titles(self): #Should return a linked title
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self): #Should return a value following the css element
        search_input = self.browser.frind_element(*self.RESULT_INPUT)
        value = search_input.get_attribute("value")
        return value

    def title(self):
        return self.browser.title