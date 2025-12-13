from pydantic import BaseModel
from typing import List, Optional
from .delivery import DeliveryModel 

class DriverPerformance(BaseModel):
    driver_id: int
    travel_time_minutes: float

class BusiestRoute(BaseModel):
    route: str
    count: int

class AnalyticsSummary(BaseModel):
    avg_travel_time: float
    avg_delay: float
    delay_rate: float
    busiest_route: BusiestRoute
    fastest_delivery: DeliveryModel
    slowest_delivery: DeliveryModel
    driver_performance: List[DriverPerformance]

