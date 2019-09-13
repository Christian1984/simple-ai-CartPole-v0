import math
from helper import *

class Laser:
    def __init__(self, initial_rotation = 0, rotation_velocity = 2 * math.pi / 360):
        self.rotation = initial_rotation
        self.rotation_velocity = rotation_velocity
        self.fires = True
    
    def rotate(self, clockwise):
        self.rotation += self.rotation_velocity if clockwise else -self.rotation_velocity
        clamp(self.rotation, 0, 2 * math.pi)