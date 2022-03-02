import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Feature: Joke Generator Button

#Scenario: Click button to move onto next jokes.

def test_joke():

#Given the website is displayed with the instruction and button
    b=webdriver.Chrome()
    wait = WebDriverWait(b, 20)

    b.get("https://elated-benz-84557d.netlify.app/#")
    
#When the user clicked on the button
    wait.until(EC.visibility_of_element_located((By.ID, "next"))).click()

#Then the joke gets generated
    m = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='p']"))).text
    if m == "":
        assert False
    else:
        assert True


    b.quit()

test_joke()
