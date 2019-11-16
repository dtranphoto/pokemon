## Pokemon UI Test Framework Architecture

![Test Framework Architecture](Pokemon.png)


As a Potential Pokemon SDET, I would like to setup UI Automated testing for the Pokemon.com/us website using Jenkins, Robot Framework, Selenium WebDriver and SauceLabs.
I will be using AWS to spin up a EC2 instance which will Run Jenkins. From Jenkins, I will have an automated nightly job that will call the Robot Framework to run all the UI Test on the Pokemon.com website.
The UI tests will be executed and recorded via SauceLabs.

# The Nightly Jenkins job can be found here.

http://3.133.109.139:8080/

# The SauceLabs Replay can be seen below.

![SauceLab_Replau](saucelab_replay.gif)

Steps to install Jenkins on AWS EC2 Linux:

   `sudo yum update`

   `sudo yum remove java-1.7.0-openjdk`

   `sudo yum install java-1.8.0`

   `sudo rpm — import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key`

   `sudo yum install jenkins -y`

   `sudo service jenkins start`

Initial Jenkins Password can be found here.

   `sudo vi /var/lib/jenkins/secrets/initialAdminPassword`

Install Git

    `sudo yum install git`

