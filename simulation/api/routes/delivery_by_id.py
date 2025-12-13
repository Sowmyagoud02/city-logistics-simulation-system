from api.utils.db import fetch_all
from fastapi import APIRouter
from api.models.delivery import DeliveryModel
from api.models.create_errors import ErrorResponse

router = APIRouter()

@router.get("/deliveries/{delivery_id}", response_model = DeliveryModel | ErrorResponse)
def get_delivery_by_id(delivery_id: int):
    query = "SELECT * FROM deliveries WHERE delivery_id = ?"
    result = fetch_all(query, (delivery_id,))
    if not result:
        return {"error": "Delivery not found"}
    else:
        #final output
        result = result[0]
        output = {
            "delivery_id": result[0],
            "driver_id": result[1],
            "route_type": result[2],
            "distance": result[3],
            "start_time": result[4],
            "travel_time_minutes": result[5],
            "delay_minutes": result[6],
            "delay_reason": result[7],
            "end_time": result[8],
            }
        return output