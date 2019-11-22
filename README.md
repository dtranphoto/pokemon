## Pokemon UI Test Framework Architecture


![Test Framework Architecture](Pokemon.png)



### Story:
As a Potential Pokemon SDET, I would like to setup UI Automated testing for the Pokemon.com/US website using Jenkins, Pytest, Selenium WebDriver and SauceLabs, in order to verify that there are no bugs on the website.

### Acceptance Criteria:
- [x] AWS account with EC2 instance running and Jenkins installed.
- [x] Working Jenkinsfile to Checkout, Execute test and Report failures.
- [x] Script to scrape Pokemon website for all Pokedexs.
- [x] UI Tests written in Pytest.
- [x] Linked SauceLabs account to executed and record UI Test.
- [x] Jenkins job to run nightly and email failures.
- [x] Multi-branch Jenkins job triggered automatically, using github webhook, when new source code is checked in.



### Definition of Done
- [x] UI test to verify all Pokemon.com Header Buttons.
- [x] UI test to verify Pokedex Search feature with randomized input.
- [x] UI tests passes and recorded on SauceLabs.
- [x] Source code checked in.


The Nightly Jenkins job can be found here.

http://3.133.109.139:8080/

The SauceLabs Replay can be seen below.


![SauceLab_Replau](saucelab_replay.gif)




