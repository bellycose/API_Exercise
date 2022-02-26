import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Feature: Joke Generator Button

#Scenario: Click button to move onto next jokes.
def test_joke():
    
    #Given the website is displayed with the instruction and button
    b=webdriver.Chrome()
    b.get("https://elated-benz-84557d.netlify.app/#")
    b.implicitly_wait(10)
    title = "Random Jokes"
    assert title == b.title
    #When the user clicked on the button
    l=b.find_element(By.ID,"next")
    l.click()
    #The the joke gets generated
    b.find_element(By.ID,"p")

    
    b.quit()

test_joke()
