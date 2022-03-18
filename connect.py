#!/usr/bin/env python
# 
# Complete LinkedIn Bot Version 1.0.0 (2022)
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool. The author accepts no liability for
# damage caused by this tool.  If these terms are not acceptable to you, then do 
# not use this tool.
# 
# by Pierre CHAUSSARD & Nathan TEBOUL
# 
# 17-Mar-2022 - 1.0.0 - Creating the linkedin connexion function.
# 

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import random

# https://github.com/mozilla/geckodriver/releases

def fill_word(word, xpath):
        elem = browser.find_element_by_xpath(xpath)
        elem.send_keys(word)

browser = webdriver.Firefox()
browser.get('https://www.linkedin.com/login/fr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

time.sleep(1)

if browser.find_element_by_xpath('/html/body/div/main/div[3]/div[1]/div[1]/h1'):
        username_xpath = '/html/body/div/main/div[3]/div[1]/form/div[1]/input'
        password_xpath = '/html/body/div/main/div[3]/div[1]/form/div[2]/input'
        body = browser.find_element_by_tag_name('body')

        load_dotenv()
        linkedin_username = os.getenv('linkedin_username')
        linkedin_password = os.getenv('linkedin_password')

        fill_word(linkedin_username, username_xpath)
        time.sleep(0.5)
        fill_word(linkedin_password, password_xpath)
        time.sleep(0.5)
        body.send_keys(Keys.ENTER)

        