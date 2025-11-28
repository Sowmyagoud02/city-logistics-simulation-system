from delivery import Delivery
from driver import Driver
import random
import csv
import sqlite3


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
            driver = Driver(i + 1, speed_factor, region, break_frequency)
            self.drivers.append(driver)
        print(self.drivers)


    def assign_delivery(self):
        delivery_id = len(self.deliveries) + 1
        driver = random.choice(self.drivers)
        print(driver)
        print(driver.__dict__)

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

        delivery.start_time = self.current_time

        #base travel time
        base_speed = 40
        print(driver.speed_factor, "hi")
        # calculate travel time mins
        effective_speed =  driver.speed_factor * base_speed
        travel_time_hrs = distance / effective_speed
        delivery.travel_time_minutes = travel_time_hrs * 60

        #calculate delay mins
        delay_choice = random.random()
        if delay_choice < 0.3:
            delivery.delay_reason = random.choice(["traffic", "break", "weather", "roadblock"])
            delivery.delay_minutes = random.randint(5,25)
        else:
            delivery.delay_reason = None
            delivery.delay_minutes = 0

        #compute total time
        delivery.end_time = delivery.start_time + delivery.travel_time_minutes + delivery.delay_minutes
        
        # update simulation clock
        self.current_time = delivery.end_time

        #create log
        log = {"delivery_id": delivery.delivery_id,
        "driver_id": delivery.driver.driver_id,
        "route_type": delivery.route_type,
        "distance": delivery.distance,
        "start_time": delivery.start_time,
        "travel_time_minutes": delivery.travel_time_minutes,
        "delay_minutes": delivery.delay_minutes,
        "delay_reason": delivery.delay_reason,
        "end_time": delivery.end_time
        }
        self.logs.append(log)
        # print(self.logs)

    
    def export_to_csv(self, filename):
        with open(filename, 'w', newline = '') as f:
            headers = ['delivery_id', 'driver_id', 'route_type', 'distance', 
            'start_time', 'travel_time_minutes', 'delay_minutes', 'delay_reason', 
            'end_time']
            writer = csv.DictWriter(f, fieldnames = headers)
            # print("\n")
            # print(writer.__dict__)
            writer.writeheader()
            writer.writerows(self.logs)

    
    def export_to_sql(self, db_path):
        import sqlite3
        import os

        # Ensure folder exists
        os.makedirs(os.path.dirname(db_path), exist_ok = True)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS deliveries(
        delivery_id INTEGER PRIMARY KEY,
        driver_id INTEGER,
        route_type TEXT,
        distance REAL,
        start_time REAL,
        travel_time_minutes REAL,
        delay_minutes REAL,
        delay_reason TEXT,
        end_time REAL
        )
        """)

        for log in self.logs:
            cursor.execute("""
            INSERT INTO deliveries VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",(
            log["delivery_id"],
            log["driver_id"],
            log["route_type"],
            log["distance"],
            log["start_time"],
            log["travel_time_minutes"],
            log["delay_minutes"],
            log["delay_reason"],
            log["end_time"]))

        conn.commit()
        cursor.close()
        conn.close()

obj = SimulationEngine()
obj.create_drivers()
for i in range(50):
    obj.assign_delivery()

import os
Base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(Base_dir, "data", "deliveries.db")
obj.export_to_sql(db_path)