from api.utils.db import fetch_all
from fastapi import APIRouter

router = APIRouter()

@router.get("/deliveries/driver/{driver_id}")
def get_delivery_by_id(driver_id: int):
    query = "SELECT * FROM deliveries WHERE driver_id = ?"
    data = fetch_all(query, (driver_id,))
    if not data:
        return {"error": "Driver not found"}
    else:
        #final output
        output = []
        for result in data:
            output.append({
            "delivery_id": result[0],
            "driver_id": result[1],
            "route_type": result[2],
            "distance": result[3],
            "start_time": result[4],
            "travel_time_minutes": result[5],
            "delay_minutes": result[6],
            "delay_reason": result[7],
            "end_time": result[8],
            })
        return output