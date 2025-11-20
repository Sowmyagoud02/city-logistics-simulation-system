class Delivery:
    def __init__(self, delivery_id, driver, route_type, distance):
        self.delivery_id = delivery_id
        self.driver = driver
        self.route_type = route_type
        self.distance = distance
        self.start_time = None
        self.end_time = None
        self.delay_reason = None
        self.delay_minutes = None
        self.status = "completed"
        self.travel_time_minutes = 0