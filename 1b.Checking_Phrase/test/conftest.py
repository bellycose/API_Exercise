#establish the rule

import pytest
import selenium.webdriver

@pytest.fixture #fixture is named "broswer". Also fixture tells the Arrange for test.
def browser():
    
    #Initialize the Webdriver instance
    b=selenium.webdriver.Chrome()
    #Make it calls wait for element to appear upto ten seconds
    b.implicitly_wait(10)
    #Return the WebDriver instance for the setup
    yield b
    #Quit the WebDriver instance for the clean up
    b.quit()