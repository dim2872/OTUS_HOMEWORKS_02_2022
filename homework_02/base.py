from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False
    weight = 0
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0: #not self.started and
            self.started = True
            # return self.started
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        total_fuel = self.fuel_consumption * distance
        if self.fuel < total_fuel:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel -= total_fuel
            return self.fuel
