*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Keywords ***
Begin Web Test
    open browser  about:blank  ${BROWSER} remote_url=https://dtranphoto:bd4e1021-fbf7-42cc-8520-f049d3779343@ondemand.saucelabs.com:443/wd/hub  desired_capabilities=name:Win 10 + Chrome 70,platform:Windows 10,browserName:chrome,version:70.0
    #maximize browser window

End Web Test
    close all browsers