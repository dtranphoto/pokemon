# coding=utf-8

import pytest
import os
from selenium import webdriver
from Resources.PO.MainPage import MainPage
from Resources.PO.PokedexPage import PokedexPage
import requests
import re
import random
from bs4 import BeautifulSoup

print("\nScraping Pokemon website for all pokedex to create a Pokedex Dictionary")
url = 'https://www.pokemon.com/us/pokedex/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#Scraping pokemon website to find all the href with pokedex in the address this wil be used to build a diction of all pokedex
def match_pokedex(href):
    return href and re.compile("pokedex").search(href)
deck = soup.find_all(href=match_pokedex)

#Create a dictionary with all Pokedex
poke_dict={}
for i in range(len(deck)):
    if ( deck[i].get_text() != None):
        temp = deck[i].get_text().split("-")
        if(len(temp)==2):
            #print(temp[0])
            #print(temp[1])
            poke_dict[temp[0].strip()] = temp[1].strip()

#print(poke_dict['133'])

@pytest.fixture
def driver(request):
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

    sauceOptions = {
        'screenResolution': '1280x768',
        'seleniumVersion': '3.141.59',
        # best practices involve setting a build number for version control
        'build': 'Pokenmon test - Python + Pytest',
        'name': 'Pokemon UI test',
        'username': sauce_username,
        'accessKey': sauce_access_key,
        # tags to filter test reporting.
        'tags': ['instant-sauce', 'ruby-rspec', 'module4'],
        # setting sauce-runner specific parameters such as timeouts helps
        # manage test execution speed.
        'maxDuration': 1800,
        'commandTimeout': 300,
        'idleTimeout': 1000,
    }

    chromeOpts = {
        'platformName': 'Windows 10',
        'browserName': 'chrome',
        'browserVersion': 'latest',
        'goog:chromeOptions': {'w3c': True},
        'sauce:options': sauceOptions
    }

    browser = webdriver.Remote(command_executor=remote_url, desired_capabilities=chromeOpts)
    yield browser
    browser.quit()

@pytest.mark.repeat(3)
def test_pokedex_search(driver):
    driver.get("https://www.pokemon.com/us/pokedex/")
    driver.implicitly_wait(100)

    pokedexPage = PokedexPage(driver)

    random_pokedex = random.choice(list(poke_dict.keys()))

    pokedexPage.enter_pokedex(random_pokedex)

    driver.implicitly_wait(100)
    pokedexPage.click_search()

    driver.implicitly_wait(100)
    pokedexPage.click_result()

    pokedex_result = poke_dict[random_pokedex]

    print(random_pokedex)
    print(pokedex_result)

    assert (pokedex_result in driver.page_source)



    driver.implicitly_wait(100)

def main_buttons(driver):
 #   driver = webdriver.Chrome(executable_path="C:/bin/chromedriver.exe")
    driver.get("https:\\www.pokemon.com")
    driver.implicitly_wait(100)

    mainPage = MainPage(driver)

    mainPage.click_pokedex()
    expected_url = r"https://www.pokemon.com/us/pokedex/"
    assert expected_url == driver.current_url
    driver.implicitly_wait(100)

    mainPage.click_video_game()
    expected_url = r"https://www.pokemon.com/us/pokemon-video-games/"
    assert expected_url == driver.current_url
    driver.implicitly_wait(100)

    mainPage.click_tcg()
    expected_url = r"https://www.pokemon.com/us/pokemon-tcg/"
    assert expected_url == driver.current_url
    driver.implicitly_wait(100)

    mainPage.click_tv()
    expected_url = r"https://www.pokemon.com/us/pokemon-episodes/"
    assert expected_url == driver.current_url
    driver.implicitly_wait(100)

    mainPage.click_play()
    expected_url = r"https://www.pokemon.com/us/play-pokemon/"
    assert expected_url == driver.current_url
    driver.implicitly_wait(100)

    mainPage.click_news()
    expected_url = r"https://www.pokemon.com/us/pokemon-news/"
    assert expected_url == driver.current_url
    driver.implicitly_wait(100)

