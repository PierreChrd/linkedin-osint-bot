#!/usr/bin/env python
#
# Complete LinkedIn Bot Version 1.0.2 (2022)
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool. The author accepts no liability for
# damage caused by this tool.  If these terms are not acceptable to you, then do
# not use this tool.
#
# by Pierre CHAUSSARD & Nathan TEBOUL
#
# 17-Mar-2022 - 1.0.0 - Creating the linkedin connexion function.
# 21-Mar-2022 - 1.0.1 - Creating the bot's structure.
# 23-Mar-2022 - 1.0.2 - Upgrading the searching function.
# 

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import time
import os
import sys
import random


class LinkedIn():
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.get(
            'https://www.linkedin.com/login/fr?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        self.body = self.browser.find_element_by_tag_name('body')
        self.search_options = {
            "1": [1, " 1. Companies.", "companies"],
            "2": [2, " 2. Peoples.", "people"],
            "3": [3, " 3. Groups.", "groups"],
        }

    def section_print(self, title):
        print("\n" + "=" * 50)
        print(title)
        print("=" * 50)

    def fill_word(self, word, xpath):
        elem = self.browser.find_element_by_xpath(xpath)
        elem.send_keys(word)

    def connect(self):
        time.sleep(1)
        if self.browser.find_element_by_xpath('/html/body/div/main/div[3]/div[1]/div[1]/h1'):
            username_xpath = '/html/body/div/main/div[3]/div[1]/form/div[1]/input'
            password_xpath = '/html/body/div/main/div[3]/div[1]/form/div[2]/input'

            load_dotenv()
            linkedin_username = os.getenv('linkedin_username')
            linkedin_password = os.getenv('linkedin_password')

            self.fill_word(linkedin_username, username_xpath)
            time.sleep(0.5)
            self.fill_word(linkedin_password, password_xpath)
            time.sleep(0.5)
            self.body.send_keys(Keys.ENTER)
            time.sleep(1)

    def search(self):
        self.section_print("SEARCHING FUNCTION")
        for i in self.search_options:
            print(self.search_options["{}".format(i)][1])
        choice = int(input(">"))

        while not 0 < choice <= len(self.search_options):
            print("\n[x] Please select a number between {} and {}...\n".format(
            1, len(self.search_options)))
            for i in self.search_options:
                print(self.search_options["{}".format(i)][1])
            choice = int(input(">"))

        research = str(input("Enter what ({}) you want to research :\n>".format(self.search_options["{}".format(i)][2])))

        for i in self.search_options:
            if choice == self.search_options["{}".format(i)][0]:
                self.browser.get("https://www.linkedin.com/search/results/{}/?keywords={}&origin=SWITCH_SEARCH_VERTICAL&sid=KOm".format(
                    self.search_options["{}".format(i)][2], research))


        time.sleep(3)
        parentElement = self.browser.find_element_by_class_name(
            "reusable-search__entity-result-list")
        elementList = parentElement.find_elements_by_tag_name("li")
        dict = []
        # /html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]
        # /html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/ul/li[2]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]
        for i, elem in enumerate(elementList):
            print(str(elem.text))
        # child_parentElement = self.browser.find_element_by_class_name("entity-result__actions")
        # child_elementList = child_parentElement.find_elements_by_xpath(".//*")
        # dict.append(child_elementList.text)
        # time.sleep(1)
        print(dict)
