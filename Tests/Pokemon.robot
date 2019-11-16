*** Settings ***
Documentation  A simple Pokemon.com suite
Library  SeleniumLibrary

*** Variables ***
# These variables can be overriden on the command line
${BROWSER} =  chrome
${START_URL} =  https://www.pokemon.com/us/

# Use this terminal command to RUN
# robot -d Results Tests/Pokemon.robot

*** Test Cases ***
Web GUI Test Click Main Buttons
    [Documentation]  Pokemon.com test
    [Tags]  Smoke
#    Open Browser  ${START_URL}  ${BROWSER}
    Open Browser  ${START_URL}  ${BROWSER}  remote_url=https://dtranphoto:bd4e1021-fbf7-42cc-8520-f049d3779343@ondemand.saucelabs.com:443/wd/hub  desired_capabilities=name:Win 10 + Chrome 70,platform:Windows 10,browserName:chrome,version:70.0
    #Open Browser  ${START_URL}  ${BROWSER}  remote_url=http://YOUR-SAUCE-USERNAME:YOUR-SAUCE-KEY@ondemand.saucelabs.com:80/wd/hub  desired_capabilities=name:Win 10 + IE 11,platform:Windows 10,browserName:internet explorer,version:11.285
    Wait Until Page Contains    Home
    Click Link  /us/pokedex/
    Wait Until Page Contains    Name or Number
    sleep    1s
    Click Link  /us/pokemon-video-games/
    Wait Until Page Contains    Video Games & Apps
    sleep    1s
    Click Link  /us/pokemon-tcg/
    Wait Until Page Contains    Pokémon TCG
    sleep    1s
    Click Link  /us/pokemon-episodes/
    Wait Until Page Contains    Pokémon TV
    sleep    1s
    Click Link  /us/play-pokemon/
    Wait Until Page Contains    Play! Pokémon Events
    sleep    1s
    Click Link  /us/pokemon-news/
    Wait Until Page Contains    Pokémon News
    sleep    1s

    Close Browser

Web GUI Test Search Pokedex for Eevee
    [Documentation]  A simple Pokemon.com test
    [Tags]  Smoke
#    Open Browser  ${START_URL}  ${BROWSER}
    Open Browser  ${START_URL}  ${BROWSER}  remote_url=https://dtranphoto:bd4e1021-fbf7-42cc-8520-f049d3779343@ondemand.saucelabs.com:443/wd/hub  desired_capabilities=name:Win 10 + Chrome 70,platform:Windows 10,browserName:chrome,version:70.0
    Wait Until Page Contains    Home
    Click Link   /us/pokedex/
    Wait Until Page Contains    Name or Number
    Input Text   id=searchInput  Eevee
    sleep    1s
    Click Button    id=search
    Wait Until Page Contains    133
    sleep   3s

    Close Browser

*** Keywords ***

