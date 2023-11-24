from abc import ABC


class Vehicle(ABC):

    def __init__(self, speed, type):
        self.speed = speed
        self.type = type

    def get_speed(self):
        return self.speed

    def get_type(self):
        return self.type
