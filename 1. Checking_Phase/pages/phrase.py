#This module contains the URL Search Engine and the page-object for the search bar. Written in OOP. Do something

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Page:
    #URL
    URL = "https://www.duckduckgo.com"
    
    #Locators
    SEARCH_INPUT = (By.ID, "search_form_input_homepage") #Input the locator in the string

    #Initializer
    def __init__(self,browser):
        self.browser = browser
    
    #Interaction Methods
    def load(self): #loading the page
        self.browser.get(self.URL) #Load the Webpage

    def search(self,phrase): #Searching the page for target phrase
        search_input = self.browser.find_element(*self.SEARCH_INPUT) #(Locator type and query) Positional Arguement, Tuple for SEARCH_INPUT
        search_input.send_keys(phrase+Keys.RETURN) #return keys of phrase and preceed with the search result page