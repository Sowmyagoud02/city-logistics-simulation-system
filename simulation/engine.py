from typing import Optional
from delivery import Delivery
from driver import Driver
import random
import csv
import sqlite3
import os


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

    def assign_delivery(self, new_delivery_id: Optional[int] = None):
        if new_delivery_id is None:
            delivery_id = len(self.deliveries) + 1
        else:
            delivery_id = new_delivery_id

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

        delivery.start_time = self.current_time

        base_speed = 40
        effective_speed = driver.speed_factor * base_speed
        travel_time_hrs = distance / effective_speed
        delivery.travel_time_minutes = travel_time_hrs * 60

        delay_choice = random.random()
        if delay_choice < 0.3:
            delivery.delay_reason = random.choice(["traffic", "break", "weather", "roadblock"])
            delivery.delay_minutes = random.randint(5, 25)
        else:
            delivery.delay_reason = None
            delivery.delay_minutes = 0

        delivery.end_time = delivery.start_time + delivery.travel_time_minutes + delivery.delay_minutes
        self.current_time = delivery.end_time

        log = {
            "delivery_id": delivery.delivery_id,
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

    def export_to_sql(self, db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

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
                INSERT OR IGNORE INTO deliveries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                log["delivery_id"],
                log["driver_id"],
                log["route_type"],
                log["distance"],
                log["start_time"],
                log["travel_time_minutes"],
                log["delay_minutes"],
                log["delay_reason"],
                log["end_time"]
            ))

        conn.commit()
        cursor.close()
        conn.close()


# ---------------------------------------------------------
# Single delivery function (used by API)


def generate_single_delivery():
    """Generate EXACTLY one new delivery and insert it fresh into DB."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "data", "deliveries.db")

    # Load DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get latest delivery ID
    cursor.execute("SELECT MAX(delivery_id) FROM deliveries")
    max_id = cursor.fetchone()[0] or 0
    new_id = max_id + 1

    # Simulation engine instance for a single delivery
    engine = SimulationEngine()
    engine.create_drivers()
    engine.assign_delivery(new_id)

    new_delivery = engine.logs[-1]

    # Insert single row
    cursor.execute("""
        INSERT INTO deliveries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        new_delivery["delivery_id"],
        new_delivery["driver_id"],
        new_delivery["route_type"],
        new_delivery["distance"],
        new_delivery["start_time"],
        new_delivery["travel_time_minutes"],
        new_delivery["delay_minutes"],
        new_delivery["delay_reason"],
        new_delivery["end_time"]
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return new_delivery


def generate_batch_deliveries(count: int):
    """Generate multiple deliveries and save them to DB using global engine."""

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "data", "deliveries.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get current max ID from DB
    cursor.execute("SELECT MAX(delivery_id) FROM deliveries")
    max_id = cursor.fetchone()[0] or 0

    new_deliveries = []

    for i in range(1, count + 1):
        new_id = max_id + i
        global_engine.assign_delivery(new_id)
        new_delivery = global_engine.logs[-1]

        cursor.execute("""
            INSERT INTO deliveries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            new_delivery["delivery_id"],
            new_delivery["driver_id"],
            new_delivery["route_type"],
            new_delivery["distance"],
            new_delivery["start_time"],
            new_delivery["travel_time_minutes"],
            new_delivery["delay_minutes"],
            new_delivery["delay_reason"],
            new_delivery["end_time"]
        ))

        new_deliveries.append(new_delivery)

    conn.commit()
    cursor.close()
    conn.close()

    return new_deliveries


def ensure_initial_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "data", "deliveries.db")

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ensure table exists
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

    cursor.execute("SELECT COUNT(*) FROM deliveries")
    count = cursor.fetchone()[0]

    conn.close()

    if count == 0:
        print("🔄 No deliveries found. Seeding initial data...")

        engine = SimulationEngine()
        engine.create_drivers()

        for _ in range(50):
            engine.assign_delivery()

        engine.export_to_sql(db_path)

        print("Initial 50 deliveries seeded.")

# Global shared engine instance
global_engine = SimulationEngine()
global_engine.create_drivers()