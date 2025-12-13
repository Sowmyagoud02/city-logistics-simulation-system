from typing import Optional
from pydantic import BaseModel

class DeliveryModel(BaseModel):
    delivery_id: int
    driver_id: int
    route_type: str
    distance: float
    start_time: float
    travel_time_minutes: float
    delay_minutes: float
    delay_reason: Optional[str]
    end_time: float