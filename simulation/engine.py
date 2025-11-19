from .delivery import Delivery
from .driver import Driver
import random


class SimulationEngine:
    def __init__(self):
        self.current_time = 0
        self.drivers = []
        self.deliveries = []
        self.logs = []

    
    def create_drivers(self):
        number_of_drivers = random.randint(5, 10)
        for i in range(number_of_drivers):
            speed_factor = random.uniform(0.8, 1.2)
            region = random.choice(["city_center", "suburbs", "industrial", "rural"])
            break_frequency = random.choice(["high", "low", "medium"])
            driver = Driver(i, speed_factor, region, break_frequency)
            self.drivers.append(driver)


    def assign_delivery(self):
        delivery_id = len(self.deliveries) + 1
        driver = random.choice(self.drivers)
        route_type = random.choice(["city_center", "suburbs", "industrial", "rural"])
        if route_type == "city_center":
            distance = random.uniform(2, 8)
        elif route_type == "suburbs":
            distance = random.uniform(7, 20)
        elif route_type == "industrial":
            distance = random.uniform(5, 15)
        else:
            distance = random.uniform(10, 30)
        delivery = Delivery(delivery_id, driver, route_type, distance)
        self.deliveries.append(delivery)  