import sqlite3
import os

def run_query(command):
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(Base_dir, "data", "deliveries.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(command)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def average_travel_time():
    command = "SELECT AVG(travel_time_minutes) FROM deliveries"
    solution = run_query(command)
    return f"{solution[0][0]:.2f}"


def average_delay():
    command = "SELECT AVG(delay_minutes) FROM deliveries"
    solution = run_query(command)
    return solution[0][0]


def delay_rate(): # wt percentage of deliveries faced delays
    command = """
    SELECT (SUM(CASE WHEN delay_minutes > 0.0 THEN 1 ELSE 0 END)*100.0)/COUNT(*) FROM deliveries"""
    solution = run_query(command)
    return solution[0][0]


def get_busiest_route(): # Which route type (city_center/suburbs/industrial/rural) is used most often?
    command = """SELECT route_type, COUNT(route_type)
    FROM deliveries
    GROUP BY route_type
    ORDER BY COUNT(route_type) DESC 
    LIMIT 1"""
    solution = run_query(command)
    return solution


def fastest_delivery():
    command = """SELECT driver_id, travel_time_minutes
    FROM deliveries
    ORDER BY travel_time_minutes
    LIMIT 1"""
    solution = run_query(command)
    return solution


def slowest_delivery():
    command = """SELECT driver_id, travel_time_minutes
    FROM deliveries
    ORDER BY travel_time_minutes DESC
    LIMIT 1"""
    solution = run_query(command)
    return solution


def get_driver_performace():
    command = """SELECT driver_id, AVG(travel_time_minutes)
    FROM deliveries
    GROUP BY driver_id
    """
    solution = run_query(command)
    return solution