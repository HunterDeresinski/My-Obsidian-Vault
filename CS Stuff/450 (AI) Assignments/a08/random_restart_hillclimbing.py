import random
from hillclimbing import hillclimbing

class Random_Restart_Hillclimbing:
    def __init__(self):
        self.prev_points = None
        self.successor_method = 'p2'
    def __call__(self,
                 obj, points):
        print("*** NOT IMPLEMENTED ***")

    def final(self, obj, points):
        if obj(points) < obj(self.prev_points):
            return points
        else:
            return self.prev_points
        
random_restart_hillclimbing = Random_Restart_Hillclimbing()
