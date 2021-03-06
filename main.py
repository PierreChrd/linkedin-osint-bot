#!/usr/bin/env python
# 
# Complete LinkedIn Bot Version 1.0.7 (2022)
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool. The author accepts no liability for
# damage caused by this tool.  If these terms are not acceptable to you, then do 
# not use this tool.
# 
# by Pierre CHAUSSARD & Nathan TEBOUL
# 
# 17-Mar-2022 - 1.0.0 - [Add] Linkedin connexion function.
# 21-Mar-2022 - 1.0.1 - [Add] Bot's structure.
# 23-Mar-2022 - 1.0.2 - [Fix] Searching function.
# 25-Mar-2022 - 1.0.3 - [Add] Auto-add function.
#             - 1.0.4 - [Add] Advanced scraping.
# 28-Mar-2022 - 1.0.5 - [Fix] Scrap issues.
# 30-Mar-2022 - 1.0.6 - [Add] Automatic acceptance of invitations, 
#                     - [Fix] Scrap function.
# 31-Mar-2022 - 1.0.7 - [Fix] Scrap + invitation.
# 

import sys, pyfiglet
from bot import *


class Main():
    def __init__(self):
        self.state = True
        self.con = LinkedIn()
        self.con.connect()
        self.options = {
            "1": [1, " 1. Searching function.", self.con.search],
            "2": [2, " 2. Adding people.", self.con.add_people],
            "3": [3, " 3. Accept invitations.", self.con.accept_invits],
            "4": [4, " 4. Scrap company.", self.con.scrap_company],
        }

    def print_menu(self):
        ascii_banner = pyfiglet.figlet_format("LINKEDIN.BOT")
        print(ascii_banner)
        print("=" * 58)
        print("This tool may be used for legal purposes only. \nUsers take full responsibility for any actions performed \nusing this tool. The author accepts no liability for \ndamage caused by this tool.  If these terms are not \nacceptable to you, then do not use this tool.")
        print("\nTool developed by Pierre CHAUSSARD & Nathan TEBOUL.")
        print("=" * 58)
        print("Bot functions :")
        for i in self.options:
            print(self.options["{}".format(i)][1])
        choice = int(input(">"))
        
        while not 0 < choice <= len(self.options):
            print("\n[x] Please select a number between {} and {}...\n".format(1, len(self.options)))
            for i in self.options:
                print(self.options["{}".format(i)][1])
            choice = int(input(">"))
        
        for i in self.options:
            if choice == self.options["{}".format(i)][0]:
                self.options["{}".format(i)][2]()


if __name__ == '__main__':    
    try:
        main = Main()
        while main.state:
            main.print_menu()

    except KeyboardInterrupt:
        print("\n[x] Exiting Program !")
        sys.exit()  
    except Exception as e:
        print("[!] Error : " + str(e))