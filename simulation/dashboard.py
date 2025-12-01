import sqlite3
import os
import matplotlib.pyplot as plt

def get_db_path():
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(Base_dir, "data", "deliveries.db")

def load_deliveries():
    db_path = get_db_path()

    #connect to db
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #fetch all data
    cursor.execute("SELECT * FROM deliveries")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

def get_report_path(filename):
    Base_dir = os.path.dirname(os.path.abspath(__file__))
    report_dir = os.path.join(Base_dir, "sample_outputs")
    os.makedirs(report_dir, exist_ok = True)
    return os.path.join(report_dir, filename)

def generate_all_plots(save=False):
    """Generate the 4-plot dashboard. 
       If save=True, it saves as PNG. 
       Returns matplotlib figure object."""
    
    data = load_deliveries()

    travel_times = []
    delay_reasons = []
    route_types = []

    for i in data:
        travel_times.append(i[5])
        if i[7] is not None:
            delay_reasons.append(i[7])
        route_types.append(i[2])

    fig, axes = plt.subplots(2, 2, figsize = (15, 10))

    # histogram plot - plot 1

    axes[0][0].hist(travel_times, bins = 10, edgecolor = "black")
    axes[0][0].grid(alpha = 0.1)
    axes[0][0].set_title("Travel Time Distribution")
    axes[0][0].set_xlabel("Travel Time (mins)")
    axes[0][0].set_ylabel("Number of Deliveries")


    #bar chart - plot 2
    delay_dict = {}
    for i in delay_reasons:
        if i not in delay_dict:
            delay_dict[i] = 1
        else:
            delay_dict[i] = delay_dict[i] + 1

    x = delay_dict.keys()
    y = delay_dict.values()
    axes[0][1].set_title("Delay Reason Frequency")
    axes[0][1].set_xlabel("delay reasons")
    axes[0][1].set_ylabel("number of frequency")
    axes[0][1].bar(x, y)


    #pie chart - plot 3
    route_type_dict = {}
    for i in route_types:
        if i not in route_type_dict:
            route_type_dict[i] = 1
        else:
            route_type_dict[i] = route_type_dict[i] + 1

    labels = route_type_dict.keys()
    sizes = route_type_dict.values()
    axes[1][0].set_title("ROUTE TYPE DISTRIBUTION PIE CHART")
    axes[1][0].pie(sizes, labels = labels, autopct = '%1.1f%%')


    # scatter plot - distance vs time - plot 4
    distance = []
    for i in data:
        distance.append(i[3])
    axes[1][1].scatter(distance, travel_times)
    axes[1][1].set_title("Distance vs Time")
    axes[1][1].set_xlabel("Distance (km)")
    axes[1][1].set_ylabel("Time (mins)")
    axes[1][1].grid(alpha = 0.2)

    plt.tight_layout()

    # ✔ Optional saving (controlled with parameter)
    if save:
        save_path = get_report_path("dashboard.png")
        fig.savefig(save_path, dpi=300)
        print("Dashboard saved to:", save_path)

    return fig
