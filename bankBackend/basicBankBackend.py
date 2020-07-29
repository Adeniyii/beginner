"""A BANKING FILE SYSTEM"""

#  import useful modules
import os
import random
import linecache
from sys import exit
from time import sleep
from textwrap import dedent
# default prompt
prompt = ("> ")


#  class to house useful methods to be imported by classes in the program.
class ToolBox(object):
    #  method to create a new file
    def make_file(self, new_file):
        self.new_file = new_file

        file = open(self.new_file,'a')
        file.close()
    #  method to write to file
    def write_to_file(self, file_name, file_content):
        self.file_name = file_name
        self.file_content = file_content

        w_file = open(self.file_name,'a')
        w_file.write(self.file_content)
        w_file.close()
    #  method to read into file and split result into list.
    def read_and_split_file(self, filename):
        self.filename = filename
        file = open(self.filename, 'r')
        return file.read().split(',')
    #  method to generate account number.
    def acct_num_gen(self):
        num = random.choices(range(10), k=10)
        acct_num = ''
        for digits in num:
            digits = str(digits)
            acct_num += digits
        return acct_num
    #  method to locate a string and return it's line number.
    def get_line_num(self, filename, keyword):
        with open (filename) as f:
            for i, line in enumerate(f, 1):
                if keyword in line:
                    return i
    #  method to collect strings from multiple lines using linecache.
    def get_multiple_lines(self, start, limit, filename):
        self.limit = limit
        self.filename = filename
        self.start = start
        details_list = []
        # to iterate over a number of lines and collect the corresponding strings
        for num in range(self.limit):
            details = linecache.getline(self.filename, self.start)
            linecache.clearcache()
            details_list.append(details)
            self.start += 1

        new = '\n'.join(details_list)
        return new


#  Engine base-class to control switching and running pages.
class Engine(object):

    def __init__(self, page_map):
        self.page_map = page_map

    def run(self):
        current_page = self.page_map.opening_page()
        last_page = self.page_map.next_page('logout')

        while current_page != last_page:
            next_page_name = current_page.enter()
            current_page = self.page_map.next_page(next_page_name)
        current_page.enter()


#  base-class for all page classes.
class Pages(object):

    def enter(self):

        print("Base class for all pages in the program")
        print("Sub-class and continue.")
        pass


#  sub-class to run welcome page
class WelcomePage(Pages):
    #  method to welcom user to the program and return the homepage class.
    def enter(self):
        print("\n\t\t\tWELCOME TO DENIYI DIGITAL BANK\n\n")
        print("Press enter to proceed")
        input(prompt)
        return 'home_page'


#  sub-class to run home page
class HomePage(Pages):
    #  method to choose to log-in, close app, or create new staff account.
    #  and return the appropriate page sub-class.
    def enter(self):
        while True:
            print(dedent("""

                Enter 1 to login
                Enter 2 to close app

                Enter # to create staff account
            """))
            response = input(prompt)
            if response == "2":
                print("\nExiting app...\n")
                sleep(1)
                return exit(1)

            elif response == "1":
                return 'staff_login'

            elif response == "#":
                return 'create_staff_acct'

            else:
                print("\nInvalid entry")


#  sub-class to create staff account.
class CreateStaffAcct(Pages):
    #  method to collect and record new staff details and return the home page.
    def enter(self):
        #  instantiate the toolbox class
        self.toolbox = ToolBox()
        self.staff_file = 'staff.txt'
        #  create new file using an imported toolbox method
        self.toolbox.make_file(self.staff_file)


        username_exists = False
        print("===============================================")

        #  collecting new staff details.
        new_fullname = input(f" Enter new fullname\n {prompt} ")
        new_email = input(f" Enter new email\n {prompt} ")

        while not username_exists:
            new_username = input(f" Enter new username\n {prompt} ")

            #  use method of the imported toolbox class to read and split file.
            file_content = self.toolbox.read_and_split_file(self.staff_file)

            if f"[{new_username}]" in file_content:
                print("Username already exists.")
            else:
                username_exists = True

        new_password = input(f" Enter new password\n {prompt} ")
        sorted = f"[{new_username}],({new_password}),{new_fullname},{new_email},"
        #  use method of the imported toolbox class to write to file.
        self.toolbox.write_to_file('staff.txt', sorted)

        print("\nNew staff added.")
        return 'home_page'


#  sub-class to login staff.
class StaffLogin(Pages):
    #  method to login staff by comparing input info with text file info.
    #  and to return the menu page on successful login.
    def enter(self):
        #  instantiate toolbox base-class.
        self.toolbox = ToolBox()
        self.staff_file = 'staff.txt'

        correct_username = False
        correct_password = False
        logged_in = False
        print("===============================================")

        while not logged_in:

            user = input(f"\n    Enter your staff username\n {prompt} ")
            username = f"[{user}]"
            passw = input(f"\n    Enter your staff password\n {prompt} ")
            password = f"({passw})"
            # call toolbox method to read and split text file.
            content = self.toolbox.read_and_split_file(self.staff_file)

            for u in content:
                if username == u:
                    correct_username = True

            for p in content:
                if password == p:
                    correct_password = True

            if correct_username and correct_password:
                print("\nAccess granted")
                logged_in = True

            elif correct_username and not correct_password:
                print("\nInvalid password")

            elif correct_password and not correct_username:
                print("\nInvalid username")

            else:
                print("\nAccess denied\n")

        return 'menu_page'


#  sub-class to present the menu page.
class MenuPage(Pages):

    def enter(self):
        #  instantiate toolbox base-class
        self.toolbox = ToolBox()
        self.staff_file = 'session.txt'
        self.toolbox.make_file(self.staff_file)
        correct_response = False
        print("===============================================")

        print(dedent("""
            Enter 1 to create bank account
            Enter 2 to check account details
            Enter 3 to logout
        """))

        while not correct_response:
            response = input(f" {prompt}")
            if response == "1":
                return 'create_bank_acct'

            elif response == "2":
                return 'chect_acct_details'

            elif response == "3":
                os.remove(self.staff_file)
                return 'home_page'
            else:
                print("Invalid entry")


# sub-class to create new customer bank account
class CreateBankAcct(Pages):

    def enter(self):

        self.toolbox = ToolBox()
        self.staff_file = 'customer.txt'
        self.toolbox.make_file(self.staff_file)
        print("===============================================")

        acct_name = input(f" Enter new account name\n {prompt} ")
        opening_bal = input(f" Enter opening balance\n {prompt} ")

        valid = False

        while not valid:
            choice = input(f" Choose account type\n1 Savings\n2 Current \n{prompt} ")

            if choice == "1" or choice.lower() == "savings":
                acct_type = "Savings"
                valid = True

            elif choice == "2" or choice.lower() == "current":
                acct_type = "Current"
                valid = True

            else:
                print("\nInvalid entry\n")

        acct_email = input(f" Enter new account email\n {prompt} ")

        acct_num = self.toolbox.acct_num_gen()

        content = dedent(f"""{acct_num}
Account name: {acct_name}
Account type: {acct_type}
Opening balance: {opening_bal}
Account email: {acct_email}
""")

        self.toolbox.write_to_file(self.staff_file, content)

        print(f"Customers' newly minted account number is\n > [{acct_num}]\n")
        print("Press enter to continue")
        input(prompt)

        sleep(1)

        return 'menu_page'


# complete
class CheckAcctDetails(Pages):

    def enter(self):

        self.toolbox = ToolBox()
        self.file = 'customer.txt'
        correct_acct_num = False
        print("===============================================")

        while not correct_acct_num:
            try:
                key = input(f"\nEnter Customer account number\n{prompt}")

                key_line = self.toolbox.get_line_num(self.file, key)
                cust_details = self.toolbox.get_multiple_lines(key_line, 5, self.file)
                correct_acct_num = True
            except TypeError:
                print("\nInvalid entry.")

        print(f"\n{cust_details}")

        print("Press enter to continue")
        input(prompt)

        sleep(1)

        return 'menu_page'



class LogOut(Pages):

    def enter(self):
        pass


# complete
class Map(object):

    pages = {
        'welcome_page': WelcomePage(),
        'home_page': HomePage(),
        'create_staff_acct': CreateStaffAcct(),
        'staff_login': StaffLogin(),
        'menu_page': MenuPage(),
        'create_bank_acct': CreateBankAcct(),
        'chect_acct_details': CheckAcctDetails(),
        'logout': LogOut()
    }

    def __init__(self, start_page):
        self.start_page = start_page

    def next_page(self, page_name):
        val = self.pages.get(page_name)
        return val

    def opening_page(self):
        return self.next_page(self.start_page)



map = Map('welcome_page')
engine = Engine(map)
engine.run()
