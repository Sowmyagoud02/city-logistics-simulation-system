from fastapi import APIRouter
from api.utils.db import fetch_all
from api.models.create_analytics import AnalyticsSummary, DriverPerformance, BusiestRoute
from api.models.delivery import DeliveryModel

router = APIRouter()

@router.get("/deliveries/summary", response_model=AnalyticsSummary)
def summary():

    avg_time = fetch_all("SELECT AVG(travel_time_minutes) FROM deliveries")[0][0]
    avg_delay = fetch_all("SELECT AVG(delay_minutes) FROM deliveries")[0][0]
    delay_rate = fetch_all(
        "SELECT (SUM(CASE WHEN delay_minutes > 0 THEN 1 ELSE 0 END) * 100.0) / COUNT(*) FROM deliveries"
    )[0][0]

    # busiest route
    row = fetch_all(
        "SELECT route_type, COUNT(*) FROM deliveries GROUP BY route_type ORDER BY COUNT(*) DESC LIMIT 1"
    )[0]
    busiest_route = BusiestRoute(route=row[0], count=row[1])

    # fastest
    f = fetch_all("SELECT * FROM deliveries ORDER BY travel_time_minutes ASC LIMIT 1")[0]
    fastest = DeliveryModel(
        delivery_id=f[0], driver_id=f[1], route_type=f[2], distance=f[3],
        start_time=f[4], travel_time_minutes=f[5], delay_minutes=f[6],
        delay_reason=f[7], end_time=f[8]
    )

    # slowest
    s = fetch_all("SELECT * FROM deliveries ORDER BY travel_time_minutes DESC LIMIT 1")[0]
    slowest = DeliveryModel(
        delivery_id=s[0], driver_id=s[1], route_type=s[2], distance=s[3],
        start_time=s[4], travel_time_minutes=s[5], delay_minutes=s[6],
        delay_reason=s[7], end_time=s[8]
    )

    # driver performance
    rows = fetch_all(
        "SELECT driver_id, AVG(travel_time_minutes) FROM deliveries GROUP BY driver_id ORDER BY driver_id"
    )
    driver_perf = [DriverPerformance(driver_id=r[0], travel_time_minutes=r[1]) for r in rows]

    return AnalyticsSummary(
        avg_travel_time=avg_time,
        avg_delay=avg_delay,
        delay_rate=delay_rate,
        busiest_route=busiest_route,
        fastest_delivery=fastest,
        slowest_delivery=slowest,
        driver_performance=driver_perf
    )