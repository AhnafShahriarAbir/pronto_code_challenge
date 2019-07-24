from os import system
import re


class UserInput():

    def title(self):
        system('clear')
        print('*'*10 + "  Hi, Give me directions please!!  " + '*'*10)
        
    def functionprint(self):
        self.title()
        try:
            direction = input("Please enter like F1 or R1\n")
            check = bool(re.search(r'^\D\d$', direction))
            if check:
                print("True")

        except ValueError:
            pass