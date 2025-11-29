🚚 City Logistics Simulation System
A Python-based Discrete-Event Simulation for Urban Delivery Networks

This project simulates a real-world last-mile delivery network (like Amazon, DHL, FedEx).
It generates delivery events, logs delays, computes analytics, stores data in SQLite, and visualizes insights through dashboards.

⭐ Features (What This Project Can Do)
✔ Simulates 50+ deliveries with drivers, routes, delays, timing & distances
✔ Randomized realistic logistics behavior
✔ Stores results in SQLite database
✔ Generates CSV and SQL exports
✔ Computes logistics analytics (avg delay, busiest route, fastest delivery…)
✔ Creates clear matplotlib dashboards
✔ Modular architecture: engine, entities, analytics, dashboards
✔ Ready to extend: Streamlit UI, APIs, Docker deployment, CI/CD

🧱 Project Architecture
city-logistics-simulation-system/
│
├── simulation/
│   ├── engine.py               # Simulation engine (DES)
│   ├── driver.py               # Driver entity
│   ├── delivery.py             # Delivery entity
│   ├── analytics.py            # SQL analytics functions
│   ├── analytics_dashboard.py  # Console dashboard
│   ├── dashboard.py            # Matplotlib multi-plot dashboard
│   ├── data/                   # SQLite DB here
│   ├── experiments/            # Earlier visualization tests
│   └── sample_outputs/         # Saved graphs & reports
│
├── README.md
└── requirements.txt

🧪 Simulation Overview
The simulation uses Discrete-Event Simulation (DES):

Event and Meaning
DeliveryAssigned - A package is created & driver chosen
DeliveryStarted - Travel begins
DelayEvent - Weather/Traffic/Break causes time loss
DeliveryCompleted -	Delivery ends & logs stored

📊 Analytics Generated
✔ Average Travel Time
✔ Average Delay
✔ Delay Rate (%)
✔ Fastest Delivery
✔ Slowest Delivery
✔ Busiest Route
✔ Driver Performance Table

📈 Visualization Dashboard
The dashboard.py script generates:
Histogram → Travel time distribution
Bar Chart → Delay frequencies
Pie Chart → Route usage
Scatter Plot → Distance vs Time
All graphs are automatically saved to:
simulation/sample_outputs/

🗄 Data Storage
All simulated deliveries are stored in:
simulation/data/deliveries.db

SQLite makes the project portable and perfect for quick analysis.

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/Sowmyagoud02/city-logistics-simulation-system.git
cd city-logistics-simulation-system/simulation

2. Run the simulation & populate database
python engine.py

3. Run analytics
python analytics_dashboard.py

4. Generate visual dashboard
python dashboard.py

🧩 Tech Stack
Category and Tools
Language - Python
Simulation Method - DES (Discrete-Event Simulation)
Database - SQLite
Visualization - Matplotlib
Data Export - CSV + SQL
Future Extensions - Streamlit UI, FastAPI, Docker

🚀 Future Roadmap
Phase 6: Streamlit Web App
Phase 7: REST API (FastAPI)
Phase 8: Dockerize Simulation
Phase 9: Deploy Dashboard Online
Phase 10: Add Machine-Learning Predictions

👤 Author
Talla Sowmya Goud
Master’s in Digital Engineering, OVGU Magdeburg
Specializing in Simulation • Data Engineering • Cloud • Python