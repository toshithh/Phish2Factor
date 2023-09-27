# Phish2Factor

<h2>Phishing for Multi-Factor authentication systems such as deployed by Google with automated request prevention.</h2>
Since Google has implemented a framework to detect automated browsers and requests to prevent phishing of multi-factor authentication systems there was a need for an automated browser which could perform automated tasks without being detected as an automated browser.

This file i.e., CVBrowser.py makes that possible. It uses computer vision and can automate any browser. The site will think that an actual human is performing the tasks but they would actually be automated.
Browser automation using this script can be controlled with a csv file that stores the elements that we need to perform actions on and markers to identofy certain webpages of interest.

<h1>Phishing Gmail Accounts</h1>
This repository demonstrates the use of this browser for phishing GMAIL Accounts. 
It is a sample Django website which uses <b>Login or SignUp with Google</b> option to simulate the real action that creates accounts according to the google account login and side by side also <b>performs login action using the cvBrowser on the server which when approved by the user on his/her phone(with the intention of logging in to our website) will grant the server permanent access to his/her account</b>
