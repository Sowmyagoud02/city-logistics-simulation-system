from typing import Optional
from pydantic import BaseModel
from .delivery import DeliveryModel

class SimulateResponse(BaseModel):
    message: str
    delivery: DeliveryModel