from fastapi import APIRouter
from api.utils.db import fetch_all

router = APIRouter()

@router.get("/deliveries/driver")
def driver():
    query = """SELECT driver_id, AVG(travel_time_minutes)
    FROM deliveries
    GROUP BY driver_id"""
    result = fetch_all(query)
    return result