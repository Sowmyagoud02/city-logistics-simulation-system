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
            i += 1
            speed_factor = random.uniform(0.8, 1.2)
            region = random.choice(["city_center", "suburbs", "industrial", "rural"])
            break_frequency = random.choice(["high", "low", "medium"])
            driver = Driver(i, speed_factor, region, break_frequency)
            self.drivers.append(driver)


    def assign_delivery(self):
        pass