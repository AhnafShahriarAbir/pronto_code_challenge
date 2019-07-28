from Orientation import OrientationEnum
from Robot import Robot

# This initiates the robot with x, y and orientation value
robot = Robot(0, 0, OrientationEnum.North.value)


class Movement:
    """
        This class contains all the functions needed for 
        the commands those will be passed to the robot.
    """

    def move_forward_x_axis(self, value):
        facing = robot.get_orientation()
        if (
            value > 0
            and facing == OrientationEnum.East.value
            or facing == OrientationEnum.West.value
        ):
            if facing == OrientationEnum.West.value:
                new_value = robot.get_x_value() - value
            else:
                new_value = robot.get_x_value() + value
                self.print_forward(value)
            robot.set_position(new_value, robot.get_y_value())
        else:
            print("Robot can not move that way. It's facing {}".format(facing))

    def move_backward_x_axis(self, value):
        facing = robot.get_orientation()
        if (
            value > 0
            and facing == OrientationEnum.East.value
            or facing == OrientationEnum.West.value
        ):
            if facing == OrientationEnum.West.value:
                new_value = robot.get_x_value() + value
            else:
                new_value = robot.get_x_value() - value
            robot.set_position(new_value, robot.get_y_value())
            self.print_backward(value)
        else:
            print("Robot can not move that way. It's facing {}".format(facing))

    def move_forward_y_axis(self, value):
        facing = robot.get_orientation()
        if (
            value > 0
            and facing == OrientationEnum.North.value
            or facing == OrientationEnum.South.value
        ):
            if facing == OrientationEnum.South.value:
                new_value = robot.get_y_value() - value
            else:
                new_value = robot.get_y_value() + value
            robot.set_position(robot.get_x_value(), new_value)
            self.print_forward(value)
        else:
            print("Robot can not move that way. It's facing {}".format(facing))

    def move_backward_y_axis(self, value):
        facing = robot.get_orientation()
        if (
            value != 0
            and facing == OrientationEnum.North.value
            or facing == OrientationEnum.South.value
        ):
            if facing == OrientationEnum.South.value:
                new_value = robot.get_y_value() + value
            else:
                new_value = robot.get_x_value() - value
            robot.set_position(robot.get_x_value(), new_value)
            self.print_backward(value)
        else:
            print("Robot can not move that way. It's facing {}".format(facing))

    def print_forward(self, value):
        facing = robot.get_orientation()
        print("I moved forward {} times in {} direction".format(value, facing))

    def print_backward(self, value):
        facing = robot.get_orientation()
        print("I moved backward {} times in {} direction".format(value, facing))

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
                """Robot is not facing at any direction.
                 Probably sleeping..zzzz"""
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
            print(
                """Robot is not facing at any direction.
             Probably sleeping..zzzz"""
            )

    def facing(self):
        return robot.get_orientation()

    def get_robot_position(self):
        return robot.current_position()

