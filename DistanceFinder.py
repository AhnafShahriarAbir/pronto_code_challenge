from Robot import Robot
import math
robot = Robot(0, 2, "West")


class DistanceFinder():
    def __init__(self, pos=None):
        self.count = 0
        self.pos = pos

    def add_point(self, a, b):
        return [a[0] + b[0], a[1] + b[1]]

    def fill_shortest_path(self, start, end):
        
        # we start here, thus a distance of 0
        open_list = [start]
        count = 0
        cur_pos = start
        ncell_pos = None
        
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for neighbour in neighbours:
            ncell_pos = self.add_point(cur_pos, neighbour)
            if ncell_pos == end:
                break

            cell = ncell_pos
            open_list.append(ncell_pos)

            if ncell_pos[0] < cur_pos[0] or ncell_pos[1] < cur_pos[1]:
                print("found short way")
                count += 1
                cur_pos = ncell_pos
                print(ncell_pos)
    

dis = DistanceFinder()
start = (4, 2)
end = (0, 0)
dis.fill_shortest_path(start, end)