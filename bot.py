#!/usr/bin/env python
#
# Complete LinkedIn Bot Version 1.0.4 (2022)
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
# 25-Mar-2022 - 1.0.3 - Creating the auto-add function.
#             - 1.0.4 - Starting the advanced scraping.
# 

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,re, os, sys, random


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
            print("\n[x] Please select a number between {} and {}...\n".format(1, len(self.search_options)))
            for i in self.search_options:
                print(self.search_options["{}".format(i)][1])
            choice = int(input(">"))

        research = str(input("Enter what ({}) you want to research :\n>".format(self.search_options["{}".format(i)][2])))

        for i in self.search_options:
            if choice == self.search_options["{}".format(i)][0]:
                self.browser.get("https://www.linkedin.com/search/results/{}/?keywords={}&origin=SWITCH_SEARCH_VERTICAL&sid=KOm".format(
                    self.search_options["{}".format(i)][2], research))

    def add_people(self):
        research = str(input("What profession do you want to find?\n>"))
        self.browser.get("https://www.linkedin.com/search/results/people/?keywords={}&origin=SWITCH_SEARCH_VERTICAL&sid=KOm".format(research))

        buttons = self.browser.find_elements_by_class_name("artdeco-button")
        for button in buttons:
            time.sleep(0.5)
            rand = random.uniform(0.6, 1.2)
            if button.text == "Se connecter": 
                time.sleep(rand)
                button.click()
                spans = self.browser.find_elements_by_class_name("artdeco-button__text")
                for span in spans:
                    if span.text == "Envoyer" :
                        time.sleep(rand/2)
                        span.click()
            elif button.text == "En attente": 
                print(button.text)

    def custom_url_pagination(self, page):
        url = self.browser.current_url
        final_str = url[:-7]
        page_stat = f"r'\1page={page}'"
        final_url = re.sub(r'(COMPANY_PAGE_CANNED_SEARCH&)', r'\1page=' + str(page), final_str)
        self.browser.get(final_url)

    def scrap(self, company):
        names = self.browser.find_elements_by_class_name("visually-hidden")
        with open("src/{}.csv".format(company), 'a', encoding='utf-8') as file:
            for name in names:
                # print(name.text)
                if "Voir le profil de" in name.text:
                    cname = name.text
                    cname = cname.replace("Voir le profil de ", "")
                    file.write(cname + "\n")
        file.close()

    def scrap_company(self):
        company = str(input("What profession do you want to find?\n>"))
        self.browser.get("https://www.linkedin.com/search/results/companies/?keywords={}&origin=SWITCH_SEARCH_VERTICAL&sid=u6P".format(company))
        time.sleep(1)
        # find and click on the first element
        titles = self.browser.find_elements_by_class_name("app-aware-link")
        time.sleep(1)
        titles[0].click()
        time.sleep(2)
        # click on the number of employees to get the full list
        class_name = "org-top-card-secondary-content__see-all"
        class_name_2 = "link-without-visited-state"
        try:
            if self.browser.find_element_by_class_name(class_name):
                # print(self.browser.find_element_by_class_name(class_name).text)
                self.browser.find_element_by_class_name(class_name).click()
            else :
                spans = self.browser.find_elements_by_class_name(class_name_2)
                # self.browser.find_element_by_class_name(class_name_2)
                spans[1].click()
        except:
            print("[x] Error...")
        
        time.sleep(1)
        # scrap all names from first page
        self.scrap(company)

        time.sleep(1)
        """
        Ici il faut modifier toute la structure de la fonction, mon raisonnement n'est pas bon, je reviens dessus lundi quand j'aurai les idées clairs.
        """
        i = 2
        self.custom_url_pagination(i)
        try:
            while 1:
                self.custom_url_pagination(i)
                self.scrap(company)
                i += 1
                time.sleep(1)
        except:
            print("fin")
        
        