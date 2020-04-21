from selenium import webdriver
import time
import random
import os
from info import usernamegrab, passwordgrab
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Nebula#3177 Roulette Automation Script")

#LOGIN BLOCK ##

browser = webdriver.Chrome("YOUR LOCATION DIRECTORY HERE") #Loads chromedriver, change dir to yours if needed
browser.get('http://addon.to/') # Launches addon.to
print("Please enter captcha...")
time.sleep(20) # Saves the program crashing by giving time to enter the captcha

#LOGIN
loginButton = browser.find_element_by_link_text('LOGIN') #Finds the actual login button
loginButton.click() # Saves time by hitting the login button

#USERNAME
usernameField = browser.find_element_by_id('username') #Finds the element "Username"
usernameField.click() # Clicks element for Username field

time.sleep(1)

#SENDS USERNAME
actualUsername = usernameField.send_keys(f'{usernamegrab}') #Sends username to the login form

#PASSWORD
passwordField = browser.find_element_by_id('userpassword')
passwordField.click()

#SENDS PASSWORD
actualPassword = passwordField.send_keys(f'{passwordgrab}') #Send password to the login form

#LOGIN BUTTON
loginButton = browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[1]/form/div[3]/div/button')
loginButton.click()

time.sleep(7) #Gives time to pass guard


#ROULETTE BLOCK ##

browser.get("https://addon.to/tools/roulette.php")
time.sleep(4)
roulettePage = browser.find_element_by_xpath('//*[@id="startRouletteee"]/button')

while True:
    roulettePage.click()
    time.sleep(8)