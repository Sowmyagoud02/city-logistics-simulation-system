import requests
import os
import time

BASE_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
TIMEOUT = 10


class BackendUnavailable(Exception):
    """Raised when backend is sleeping or unreachable"""
    pass


def safe_request(method, endpoint, retries=5, wait=6, **kwargs):
    """
    Makes a safe API request with retries.
    Designed to handle Render free-tier cold starts.
    Returns None instead of crashing the UI.
    """
    for attempt in range(retries):
        try:
            response = requests.request(
                method,
                f"{BASE_URL}{endpoint}",
                timeout=TIMEOUT,
                **kwargs
            )

            if response.status_code != 200:
                raise ValueError("Backend not ready")

            if not response.text.strip():
                raise ValueError("Empty response")

            return response.json()

        except Exception:
            if attempt < retries - 1:
                time.sleep(wait)
            else:
                return None


def wake_backend():
    """
    Ping backend to wake Render instance.
    Non-blocking by design.
    """
    try:
        requests.get(f"{BASE_URL}/healthz", timeout=5)
    except:
        pass


# ---------------- API FUNCTIONS ----------------

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