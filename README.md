## Pokemon UI Test Framework Architecture


![Test Framework Architecture](Pokemon.png)



### Story:
As a Potential Pokemon SDET, I would like to setup UI Automated testing for the Pokemon.com/US website using Jenkins, Robot Framework, Selenium WebDriver and SauceLabs, in order to verify that there are no bugs on the website.

### Acceptance Criteria:
- [x] AWS account with EC2 instance running and Jenkins installed.
- [x] Working Jenkinsfile to Checkout, Execute test and Report failures.
- [x] Installed Robot Framework with Selenium Library to execute and run the UI Test.
- [x] Linked SauceLabs account to executed and record UI Test.
- [x] Jenkins job to run nightly and email failures
- [x] Multi-branch Jenkins job to automatically run when new source code is checked in

### Definition of Done
- [x] UI test to verify all Pokemon.com Header Buttons.
- [x] [checkbox:checked] UI test to verify Pokedex Search feature.
- [x] [checkbox:checked] UI tests passes and Runs on SauceLabs.
- [x] [checkbox:checked] Source code checked in


The Nightly Jenkins job can be found here.

http://3.133.109.139:8080/

The SauceLabs Replay can be seen below.


![SauceLab_Replau](saucelab_replay.gif)


Steps required to set th
I created an AWS account. I set up my Amazon EC2 key pair and configured a Virtual Private Cloud(VPC.).
I then launched my instance and installed Jenkins, Git, and Robot Framework.
Then I created a Jenkins Job that points to this repo and uses the Jenkinfile to run the jobs.


