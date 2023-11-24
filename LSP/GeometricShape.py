from abc import ABC


class GeometricShape(ABC):
    def init(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_eight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
