from Orientation import OrientationEnum
from Robot import Robot
robot = Robot(0, 0, "North")


class Movement:
    def move_forward_x_axis(self, value):
        facing = robot.get_orientation()
        if value > 0 and facing == "East" or facing == "West":
            new_value = robot.get_x_value() + value
            if facing == "West":
                new_value = new_value * -1
                robot.set_position(new_value, robot.get_y_value())
            robot.set_position(new_value, robot.get_y_value())
            self.print_forward(value)
        
        else:
            print("Robot can not move that way. It's facing {}".format(facing))
            
    def move_backward_x_axis(self, value):
        facing = robot.get_orientation()
        if value != 0 and facing == "East" or facing == "West":
            new_value = robot.get_x_value() - abs(value)
            robot.set_position(new_value, robot.get_y_value())
            self.print_backward(value)
        else:
            print("Robot can not move that way. It's facing {}".format(facing))

    def move_forward_y_axis(self, value):
        facing = robot.get_orientation()
        if value > 0 and facing == "North" or facing == "South":
            if facing == "South":
                self.move_backward_y_axis(value)
            else:
                new_value = robot.get_y_value() + value
                robot.set_position(robot.get_x_value(), new_value)
                self.print_forward(value)
        else:
            print("Robot can not move that way. It's facing {}".format(facing))

    def move_backward_y_axis(self, value):
        facing = robot.get_orientation()
        if value != 0 and facing == "North" or facing == "South":
            new_value = robot.get_y_value() - abs(value)
            robot.set_position(robot.get_x_value(), new_value)
            self.print_backward(value)
        else:
            print("Robot can not move that way. It's facing {}".format(facing))

    def print_forward(self, value):
        facing = robot.get_orientation()
        print("I moved forward {} times in {} direction".format(
                value, facing))

    def print_backward(self, value):
        facing = robot.get_orientation()
        print("I moved backward {} times in {} direction".format(
                value, facing))
    
    def turn_right(self):
        facing = robot.get_orientation()
        if facing == OrientationEnum.North.value:
            robot.set_orientation(OrientationEnum.East.value)
        elif facing == OrientationEnum.East.value:
            robot.set_orientation(OrientationEnum.South.value)
        elif facing == OrientationEnum.South.value:
            robot.set_orientation(OrientationEnum.West.value)
        elif facing == OrientationEnum.West.value:
            robot.set_orientation(OrientationEnum.North.value)
        else:
            print(
                "Robot is not facing at any direction. Probably sleeping..zzzz"
                )

    def turn_left(self):
        facing = robot.get_orientation()
        if facing == OrientationEnum.North.value:
            robot.set_orientation(OrientationEnum.West.value)
        elif facing == OrientationEnum.West.value:
            robot.set_orientation(OrientationEnum.South.value)
        elif facing == OrientationEnum.South.value:
            robot.set_orientation(OrientationEnum.East.value)
        elif facing == OrientationEnum.East.value:
            robot.set_orientation(OrientationEnum.North.value)
        else:
            print("""Robot is not facing at any direction.
             Probably sleeping..zzzz""")

    def facing(self):
        return robot.get_orientation()

    def get_robot_position(self):
        return robot.current_position()

    def functionprint(self):
        print(robot.current_position())
        self.move_forward_y_axis(5)
        print(robot.current_position())
        self.turn_left()
        print(robot.current_position())
        self.move_forward_x_axis(2)
        self.turn_left()
        print(robot.current_position())

