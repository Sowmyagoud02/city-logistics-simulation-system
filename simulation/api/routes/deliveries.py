from fastapi import APIRouter
from api.utils.db import fetch_all

router = APIRouter()

@router.get("/deliveries")
def filter_deliveries(driver_id: int | None = None,
                    route_type: str | None = None,
                    min_time: float | None = None,
                    max_time: float | None = None):
    query = "SELECT * FROM deliveries WHERE 1=1"
    params = []
    if driver_id is not None:
        query += " AND driver_id = ?"
        params.append(driver_id)
    if route_type is not None:
        query += " AND route_type = ?"
        params.append(route_type)
    if min_time is not None:
        query += " AND travel_time_minutes >= ?"
        params.append(min_time)
    if max_time is not None:
        query += " AND travel_time_minutes <= ?"
        params.append(max_time)
    # example http://127.0.0.1:8000/filter_deliveries?driver_id=1&route_type=rural&min_time=25.0&max_time=33.0
    data = fetch_all(query, tuple(params))
    deliveries = []
    for row in data:
        deliveries.append({
            "delivery_id": row[0],
            "driver_id": row[1],
            "route_type": row[2],
            "distance": row[3],
            "start_time": row[4],
            "travel_time_minutes": row[5],
            "delay_minutes": row[6],
            "delay_reason": row[7],
            "end_time": row[8],
        })

    return deliveries