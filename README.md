# Automate Adding Attendees To Your Event In Eventbrite

DISCLAIMER: My work is based on the script written by Stephan Lead, which is found here: (https://github.com/IgniteTalks/AddAttendeesToEventBrite). The functionality within the original script is obsolete, thus the one found here is up-to-date.

## Background
Eventbrite is a great package for managing events. It allows you to set-up an event's basic info, details, registration page, and much more. Additionally, you are able to sell tickets (either paid or free) to check people in during the event using their mobile device.

One major pain is that there is no easy import function to add multiple attendees at once. Thus, if you have a long list of attendees to add, it's time-consuming and error-prone.

This script automates the process, so you can easily import multiple attendees to your guest list.

### Before You Get Started

1) Log into your EventBrite account and open up the event that you wish to add people to. Note its `eid` value, which will be shown in the URL, eg https://www.eventbrite.com/myevent?eid=123456.

2) Hit the `Manage Attendees` drop-down menu (found in the lower-left of the Home page), then select the `Add Attendees` option. use your browser's Developer Tools to note the ID of the ticket type that you wish to create.

![Finding the ID of the quantify field](https://i.imgur.com/isWfSJe.png)

3) Install the Selenium python plugin from https://selenium-python.readthedocs.org/

4) Install the ChromeDriver server from https://chromedriver.chromium.org/home

### Update The Script Where Needed

* Enter your EventBrite login and password on lines 13 & 14.
* Add your attendees to a comma-limited text file in the format `firstname,surname,email_address` (see example text file).
* Update the `attendeeList` variable on line 17 to point to the text file.
* Update the `eventID` and `ticketID` variables on lines 20 & 21 with the values you determined in (1) and (2) above.

### Run the Python script

This opens a new Chrome browser, logs into your event, and one-by-one adds each individual from the text file to your event. 
