*** Settings ***
Documentation  A simple Amazon.com suite
Library  SeleniumLibrary

*** Variables ***
# These variables can be overriden on the command line
${BROWSER} =  chrome
${START_URL} =  https://www.pokemon.com/us/
#${START_URL} =  https://www.google.com/
${START_URL} =  https://www.amazon.com/

# Use this terminal command to RUN
# robot -d results tests/amazon.robot

*** Test Cases ***
Simple Web GUI Test
    [Documentation]  A simple Pokemon.com test
    [Tags]  Smoke
    Open Browser  ${START_URL}  ${BROWSER}
    # remote_url=https://dtranphoto:bd4e1021-fbf7-42cc-8520-f049d3779343@ondemand.saucelabs.com:443/wd/hub  desired_capabilities=name:Win 10 + Chrome 70,platform:Windows 10,browserName:chrome,version:70.0
    #Open Browser  ${START_URL}  ${BROWSER}  remote_url=http://YOUR-SAUCE-USERNAME:YOUR-SAUCE-KEY@ondemand.saucelabs.com:80/wd/hub  desired_capabilities=name:Win 10 + IE 11,platform:Windows 10,browserName:internet explorer,version:11.285
    Wait Until Page Contains    Home
  #  Click Image     xpath=/html/body/nav/div[2]/ul/li[2]/a

    #css=#body > nav > div.content-wrapper > ul > li.explore > a > span.icon.icon_pokeball
   # Wait Until Page Contains    Google
   #Input Text  id=twotabsearchtextbox  Ferrari 458
   # Click Button    xpath=//*[@id="nav-search"]/form/div[2]/div/input
   Click Link   /us/pokedex/

   Wait Until Page Contains    Name or Number

   Input Text   id=searchInput  Bulbasaur

   Wait Until Page Contains    Bulbasaur

   Click Link   /us/pokedex/bulbasaur

   sleep    5s

    #Wait Until Page Contains  results for
   Close Browser

*** Keywords ***
