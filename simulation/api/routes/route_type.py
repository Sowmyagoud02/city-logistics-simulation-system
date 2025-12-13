from fastapi import APIRouter
from api.utils.db import fetch_all

router = APIRouter()


@router.get("/deliveries/route/{route_type}")
def get_delivery_by_route_id(route_type: str):
    route_type = route_type.lower()   # normalize input
    query = "SELECT * FROM deliveries WHERE route_type = ?"
    data = fetch_all(query, (route_type,))
    if not data:
        return {"message": f"No deliveries found for route type '{route_type}'"}
    else:
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