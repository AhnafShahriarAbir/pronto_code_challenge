from os import system
import re
from Movement import Movement
from Orientation import OrientationEnum

mv = Movement()
directions = []


class UserInput:
    def title(self):
        system("clear")
        print("*" * 10 + "  Hi, Give me directions please!!  " + "*" * 10)

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
            facing = mv.facing()
            if "F" in move:
                if (
                    facing == OrientationEnum.East.value
                    or facing == OrientationEnum.West.value
                ):
                    mv.move_forward_x_axis(value)

                elif (
                    facing == OrientationEnum.North.value
                    or facing == OrientationEnum.South.value
                ):
                    mv.move_forward_y_axis(value)

            elif "B" in move:
                if (
                    facing == OrientationEnum.East.value
                    or facing == OrientationEnum.West.value
                ):
                    mv.move_backward_x_axis(value)

                elif (
                    facing == OrientationEnum.North.value
                    or facing == OrientationEnum.South.value
                ):
                    mv.move_backward_y_axis(value)

            elif "R" in move:
                if value > 1:
                    print(
                        """Robot can rotate only once at a time.\n
                        Please write 1 with your direction"""
                    )
                mv.turn_right()

            elif "L" in move:
                if value > 1:
                    print(
                        """Robot can rotate only once at a time.\n
                        Please write 1 with your direction"""
                    )

                mv.turn_left()

            else:
                print("Robot did not move!! Something is wrong.")

    def functionprint(self):
        self.title()
        userInput = None
        try:
            userInput = input("Please enter like F1,R1\n")
        except:
            print("please enter correct string")

        if userInput is not None and len(userInput) > 1:
            try:
                data = userInput.split(",")
            except:
                print("Please write directions separated by commas")

            # for i in range(0, len(userInput) - 1, 2):
            #    firstOne = userInput[i:i+2]
            #    directions.append(data)
            #     # #check = bool(re.search(r'^\D\d$', direction))

            for direction in data:
                self.checkMovement(direction)
                print(mv.get_robot_position())
        else:
            print("Please type at least 2 characters")

