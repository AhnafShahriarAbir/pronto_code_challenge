
class Movement:
    def __init__(self):
        self.x_value, self.y_value = 0, 0
    
    def move_forward_x_axis(self, value):
        if value > 0 and value != 0:
            self.x_value += value
            print("I moved forward {} times".format(value))

    def move_backward_x_axis(self, value):
        if value != 0:
            self.x_value -= abs(value)
            print("I moved backward {} times".format(value))
    
    def move_forward_y_axis(self, value):
        if value > 0 and value != 0:
            self.y_value += value

    def move_backward_y_axis(self, value):
        if value != 0:
            self.y_value -= abs(value)

    def functionprint(self):
        self.move_forward_x_axis(10)
        self.move_forward_y_axis(10)
        self.move_backward_y_axis(2)
        self.move_backward_x_axis(20)
        