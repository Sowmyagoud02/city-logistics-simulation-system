import requests
import os

BASE_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

def get_summary():
    return requests.get(f"{BASE_URL}/deliveries/summary").json()

def get_all_deliveries():
    return requests.get(f"{BASE_URL}/deliveries").json()

def get_delivery_by_id(delivery_id):
    return requests.get(f"{BASE_URL}/deliveries/{delivery_id}").json()

def get_deliveries_by_driver(driver_id):
    return requests.get(f"{BASE_URL}/deliveries/driver/{driver_id}").json()

def simulate_new_delivery():
    return requests.post(f"{BASE_URL}/simulate").json()

def filter_deliveries(driver_id=None, route_type=None, min_time=None, max_time=None):
    params = {}

    if driver_id:
        params["driver_id"] = driver_id
    if route_type:
        params["route_type"] = route_type
    if min_time:
        params["min_time"] = min_time
    if max_time:
        params["max_time"] = max_time

    return requests.get(f"{BASE_URL}/deliveries", params=params).json()

def simulate_batch(count):
    return requests.post(f"{BASE_URL}/simulate/batch?count={count}").json()
