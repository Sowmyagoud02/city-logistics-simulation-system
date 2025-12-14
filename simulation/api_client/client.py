import requests
import os
import time

BASE_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
TIMEOUT = 10


class BackendUnavailable(Exception):
    pass


def safe_request(method, endpoint, **kwargs):
    try:
        response = requests.request(
            method,
            f"{BASE_URL}{endpoint}",
            timeout=TIMEOUT,
            **kwargs
        )

        if response.status_code != 200:
            raise BackendUnavailable("Backend not ready")

        if not response.text.strip():
            raise BackendUnavailable("Empty response from backend")

        return response.json()

    except requests.exceptions.RequestException:
        raise BackendUnavailable("Backend unreachable")
    except ValueError:
        raise BackendUnavailable("Invalid JSON from backend")


def wake_backend():
    """Ping backend to wake it up"""
    try:
        requests.get(f"{BASE_URL}/healthz", timeout=5)
        time.sleep(2)  # give backend time to wake
    except:
        pass


def get_summary():
    return safe_request("GET", "/deliveries/summary")


def get_all_deliveries():
    return safe_request("GET", "/deliveries")


def get_delivery_by_id(delivery_id):
    return safe_request("GET", f"/deliveries/{delivery_id}")


def get_deliveries_by_driver(driver_id):
    return safe_request("GET", f"/deliveries/driver/{driver_id}")


def simulate_new_delivery():
    return safe_request("POST", "/simulate")


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

    return safe_request("GET", "/deliveries", params=params)


def simulate_batch(count):
    return safe_request("POST", f"/simulate/batch?count={count}")