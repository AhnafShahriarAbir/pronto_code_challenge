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
        value = None
        try:
            value = int(move[1:2])
        except ValueError:
            print("Please enter valid string")
        except TypeError:
            print("Please enter correct type ")
        except:
            print("Please enter valid move")
            system(exit)

        if value is not None:
            if "F" in move:
                mv.move_forward_x_axis(value)

            elif "B" in move:
                mv.move_backward_x_axis(value)

            elif "R" in move:
                mv.turn_right()

            elif "L" in move:
                pass

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
            data = userInput.split(",")
            print(data)
            # for i in range(0, len(userInput) - 1, 2):
            #    firstOne = userInput[i:i+2]
            #    directions.append(data)
            #     # #check = bool(re.search(r'^\D\d$', direction))
            
            for direction in data:
                print(direction)
                self.checkMovement(direction)
            print(mv.current_position())
        else:
            print("Please type at least 2 characters")
                    

            