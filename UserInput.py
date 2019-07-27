from os import system
import re
from Movement import Movement
mv = Movement()
directions = []


class UserInput():

    def title(self):
        system('clear')
        print('*'*10 + "  Hi, Give me directions please!!  " + '*'*10)

    def checkMovement(self, move):
        value = int(move[1:2])

        if "F" in move:
            mv.move_forward_x_axis(value)

        elif 'B' in move:
            mv.move_backward_x_axis(value)

        else:
            print("I did not move")   

    def functionprint(self):
        self.title()
        userInput = None
        try:
            userInput = input("Please enter like F1 or R1\n")

        except:
            print("please enter correct string")
       
        if userInput is not None and len(userInput) > 1:
            for i in range(0, len(userInput) - 1, 2):
                firstOne = userInput[i:i+2]
                directions.append(firstOne)
                # #check = bool(re.search(r'^\D\d$', direction))
            
            for direction in directions:
                self.checkMovement(direction)
        else:
            print("Please type at least 2 characters")
                    

            