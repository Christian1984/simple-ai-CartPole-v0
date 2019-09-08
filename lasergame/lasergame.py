from laser import Laser
from target import Target

class LaserGame:
    def __init__(self):
        self.laser = Laser()
        self.target = Target(0.5, 0.75)