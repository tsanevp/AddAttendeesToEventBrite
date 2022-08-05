import sys
import time
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except Exception as exception:
    print(exception)
    msg = "Please instatall Selenium"
    print(msg)
    sys.exit(msg)

# Add Login Credentials
login = "<Your Eventbrite Username>"
pwd = "<Your Eventbrite Password>"

# Comma-delimited file containing the firstname, surname and email address of your attendees (see ReadMe for example)
attendeeList = "path_to_attendee_list.txt"

# Your Current Event's Information
eventID = "123456"  # eg open your event then see the URL to obtain the ID, eg https://www.eventbrite.com/myevent?eid=123456
ticketID = "quant_632892259"  # Use the Dev Tools inspector to determine the ID of the ticket type you wish to add (https://i.imgur.com/isWfSJe.png)

# Opens a new Chrome browser
try:
    browser = webdriver.Chrome()
except Exception as exception:
    print(exception)
    msg = "Please install ChromeDriver"
    print(msg)
    sys.exit(msg)

# Opens Eventbrite 
browser.get("https://www.eventbrite.com/attendees-add?eid=" + str(eventID))
username = browser.find_element(By.ID, "email")
password = browser.find_element(By.ID, "password")
username.send_keys(login)
password.send_keys(pwd)
time.sleep(2)
loginButton = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div/form/div[4]/div/button')
loginButton.click()
time.sleep(10)

# Iterate through and add each first/last name & email in the attendee list
with open(attendeeList) as inFile:
    lines = inFile.readlines()
    for line in lines:
        tokens = line.split(",")
        firstname = tokens[0]
        surname = tokens[1]
        email = tokens[-1]
        print("Adding " + firstname + " " + surname + " (" + email + ")")

        # Add each person to the event attendee list
        try:
            # Open "Add Attendees" page for current event
            browser.get("https://www.eventbrite.com/attendees-add?eid=" + str(eventID))
            time.sleep(10)
            # Populate ticket purchase amount for current customer
            ticket_quantity = browser.find_element(By.ID, ticketID)
            ticket_quantity.send_keys("1")
            time.sleep(2)
            # Click "Continue" button
            continuebtn = browser.find_element(By.XPATH, '//*[@id="continue-attendee"]')
            continuebtn.click()
            time.sleep(10)
            browser.switch_to.frame(0)
            # Populate current attendee's first/last name & email
            buyer_first_name = browser.find_element(By.XPATH, '//*[@id="buyer.N-first_name"]').send_keys(firstname)
            buyer_last_name = browser.find_element(By.XPATH, '//*[@id="buyer.N-last_name"]').send_keys(surname)
            buyer_email = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/main/div/div[1]/div[1]/div/form/div[1]/div/div/div[4]/div/div[1]/div/div/input').send_keys(email)
            # buyer_first_name.send_keys(firstname)
            # buyer_last_name.send_keys(surname)
            # buyer_email.send_keys(email)
            time.sleep(5)
            # Click "Submit" button
            submitbtn = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/main/div/div[2]/div/nav/div[1]/button')
            submitbtn.click()
            time.sleep(10)
        except Exception as exception:
            print(exception)
            print("There was a problem adding " + firstname + " " + surname)

browser.close()