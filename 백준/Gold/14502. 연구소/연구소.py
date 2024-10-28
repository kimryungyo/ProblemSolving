from collections import deque
from itertools import combinations
from copy import deepcopy

class Simulation():
    def __init__(self, x, y, maps):
        self.x = x
        self.y = y
        self.maps = maps

        self.patient_zero = { (x, y) for y in range(self.y) 
                                     for x in range(self.x) 
                                     if self.maps[y][x] == 2 }

        self.paths = { (x, y) for y in range(self.y) 
                                     for x in range(self.x) 
                                     if self.maps[y][x] == 0 }
        
        self.path_count = len(self.paths)

        self.cases = list(combinations(self.paths, 3))
        self.simulation()

    def get_point(self, maps, point):
        if point[0] < 0 or point[0] >= self.x: return None
        if point[1] < 0 or point[1] >= self.y: return None
        return maps[point[1]][point[0]]

    def set_point(self, maps, point, value):
        maps[point[1]][point[0]] = value

    def print_maps(self, maps): 
        for y in range(self.y): print(*maps[y])

    def simulation(self):
        max_count = 0

        for case in self.cases:
            visited = set()
            check = deque(self.patient_zero)
            maps = deepcopy(self.maps)
            
            for changed in case: self.set_point(maps, changed, 1)
            count = self.path_count - 3

            while check:
                point = check.popleft()
                directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
                for d in directions:

                    p = ( point[0] + d[0], point[1] + d[1] )

                    if p not in visited:
                        value = self.get_point(maps, p)
                        visited.add(p)

                        if value == 0:
                            self.set_point(maps, p, 2)
                            check.append(p)
                            count -= 1

            if count > max_count: max_count = count
            
        print(max_count)

y, x = tuple(map(int, input().split()))
maps = [ list(map(int, input().split())) for _ in range(y) ]

simulation = Simulation(x, y, maps)
