from Robot import Robot
import math
robot = Robot(0, 2, "West")


class DistanceFinder():
    def __init__(self, pos=None):
        self.count = 0
        self.pos = pos
        
    def add_point(self, a, b):
        return [a[0] + b[0], a[1] + b[1]]

    def fill_shortest_path(self, start, end, max_distance=math.inf):
        """ Creates a duplicate of the board and fills the `Cell.count` 
        field with the distance from the start to that cell. """

        # we start here, thus a distance of 0
        open_list = [start]
        # robot.at(start).count = 0
        count = 0
        # (x,y) offsets from current cell
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while open_list:
            cur_pos = open_list.pop(0)
            cur_cell = robot.set_position(cur_pos[0], cur_pos[1])
            
            for neighbour in neighbours:
                ncell_pos = self.add_point(cur_pos, neighbour)
                if ncell_pos == end:
                    break

                if ncell_pos[0] < cur_pos[0] or ncell_pos[1] < cur_pos[1]:
                    print("found short way")
                    count += 1
                    print(count)
                    robot.set_position(ncell_pos[0], ncell_pos[1])
                    print(robot.current_position())

                # # cell = self.at(ncell_pos)

                # dist = count + 1
                # print(dist)
                # if dist > max_distance:
                #     continue

                # if count > dist:
                #     count = dist
                #     # cell.path_from = cur_cell
                #     open_list.append(ncell_pos)

                # return nboard

dis = DistanceFinder()
start = (1, 1)
end = (0, 0)
dis.fill_shortest_path(start, end)
