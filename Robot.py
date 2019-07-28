
class Robot():
    def __init__(self, x, y, orientation):
        self.x_value, self.y_value = x, y
        self.orientation = orientation
    
    def set_position(self, x, y):
        self.x_value, self.y_value = x, y

    def set_orientation(self, facing):
        self.orientation = facing

    def get_x_value(self):
        return self.x_value

    def get_orientation(self):
        return self.orientation

    def get_y_value(self):
        return self.y_value

    def current_position(self):
        return (self.x_value, self.y_value, self.orientation)

    def printfunc(self):
        print(self.current_position())

# robot = Robot(1, 2, "West")
# robot.printfunc()
# robot.set_position(5, 8)
# robot.set_orientation("North")
# robot.printfunc()