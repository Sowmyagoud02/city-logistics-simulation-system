from analytics import *

def generate_report():
    analysis_dict = {"avg_travel": average_travel_time(),
                    "avg_delay": average_delay(),
                    "delay_rate": delay_rate(),
                    "busiest_route": get_busiest_route(),
                    "fastest_delivery": fastest_delivery(),
                    "slowest_delivery": slowest_delivery(),
                    "driver_stats": get_driver_performace()}
    return analysis_dict


def print_dashboard(analysis_dict):
    driver_lines = ""
    for id, travel_time in analysis_dict["driver_stats"]:
        driver_lines += f"• Driver {id}: {travel_time:.2f} mins" + "\n"

    print(f"""
=================== DELIVERY ANALYTICS REPORT ===================

Total Deliveries: 50
Average Travel Time: {analysis_dict["avg_travel"]} mins
Average Delay: {analysis_dict["avg_delay"]} mins
Delay Rate: {analysis_dict["delay_rate"]}%

Busiest Route: {analysis_dict["busiest_route"][0][0]} ({analysis_dict["busiest_route"][0][1]} deliveries)

Fastest Delivery: ID {analysis_dict["fastest_delivery"][0][0]} (travel time {analysis_dict["fastest_delivery"][0][1]:.2f} mins)
Slowest Delivery: ID {analysis_dict["slowest_delivery"][0][0]} (travel time {analysis_dict["slowest_delivery"][0][1]:.2f} mins)

Driver Performance (Avg Travel Time):
{driver_lines}

=================================================================
        """)


dict = generate_report()
print_dashboard(dict)