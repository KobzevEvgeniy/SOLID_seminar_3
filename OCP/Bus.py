from abc import ABC

from OCP.Vehicle import Vehicle


class Bus(Vehicle, ABC):
    pass

    def get_type(self):
        return self.type

    def get_max_speed(self):
        return f"максимальная скорость-  {self.get_speed() * 0.6}"
