# Simple-Honeypot
This is a simple honeypot written using python that logs the action of clicking the 'click me button' on the site


app.py:

This python code uses flask to integrate html code
It also integrates the honeypot.py with the thread that runs the honeypot in the background.

honeypot.py:

This code is a very basic honeypot implementation which uses socket and logging module
Every time this script is run, honeypot.log file is created

index.html:

This is the interface of the honeypot which contains the click me button
And when a user clicks the button, it uses javascript function logClick which sends a POST request which will be then logged in to the honeypot.log file


To run this:

python3 app.py
and navigate to http://127.0.0.1:5000
