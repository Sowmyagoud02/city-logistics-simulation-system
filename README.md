# 🚚 City Logistics Simulation System
### A Python-Based Discrete-Event Simulation for Urban Delivery Networks

This project simulates a real-world last-mile delivery network (like **Amazon, DHL, FedEx**).
It generates delivery events, logs delays, computes analytics, stores data in SQLite, and visualizes insights through dashboards.

---

## ⭐ Features (What This Project Can Do)

✔ Simulates 50+ deliveries with **drivers, routes, delays, timings & distances**  
✔ Randomized realistic logistics behavior  
✔ Stores results in **SQLite database**  
✔ Generates **CSV and SQL** exports  
✔ Computes powerful analytics:  
- Average delay  
- Busiest route  
- Fastest delivery  
- Slowest delivery  
✔ Creates clear **Matplotlib dashboards**  
✔ Modular architecture: engine, entities, analytics, dashboards  
✔ Extensible: **Streamlit UI, FastAPI, Docker, Cloud deployment**

---

## 🧱 Project Architecture

```
city-logistics-simulation-system/
│
├── simulation/
│   ├── engine.py                 # Simulation engine (DES)
│   ├── driver.py                 # Driver entity
│   ├── delivery.py               # Delivery entity
│   ├── analytics.py              # SQL analytics functions
│   ├── analytics_dashboard.py    # Console analytics dashboard
│   ├── dashboard.py              # Matplotlib multi-plot dashboard
│   ├── data/                     # SQLite DB here
│   ├── experiments/              # Earlier visualization tests
│   └── sample_outputs/           # Saved graphs & reports
│
├── README.md
└── requirements.txt
```

---

## 🧪 Simulation Overview (DES — Discrete Event Simulation)

The simulation runs through four main events:

| Event                | Meaning                                     |
|----------------------|---------------------------------------------|
| **DeliveryAssigned** | Delivery generated, driver selected         |
| **DeliveryStarted**  | Travel begins                               |
| **DelayEvent**       | Weather/Traffic/Break causes delay          |
| **DeliveryCompleted**| Delivery ends & logs are stored             |

Time jumps **event-to-event**, not every second — making the simulation fast and realistic.

---

## 📊 Analytics Generated

✔ Average Travel Time  
✔ Average Delay  
✔ Delay Rate (%)  
✔ Busiest Route  
✔ Fastest Delivery  
✔ Slowest Delivery  
✔ Driver Performance Table  

---

## 📈 Visualization Dashboard

The `dashboard.py` script generates:

- **Histogram** → Travel time distribution  
- **Bar Chart** → Delay frequency  
- **Pie Chart** → Route distribution  
- **Scatter Plot** → Distance vs. travel time  

All plots are automatically saved to:

```
simulation/sample_outputs/
```

---

## 🗄 Data Storage

Data is stored in:

```
simulation/data/deliveries.db
```

SQLite keeps the project lightweight, portable, and ideal for analytics workflows.

---

## ▶️ How to Run the Project

### **1. Clone the repository**
```bash
git clone https://github.com/Sowmyagoud02/city-logistics-simulation-system.git
cd city-logistics-simulation-system/simulation
```

### **2. Run the simulation & populate the database**
```bash
python engine.py
```

### **3. Run analytics**
```bash
python analytics_dashboard.py
```

### **4. Generate visualization dashboard**
```bash
python dashboard.py
```

---

## 🧩 Tech Stack

| Category          | Tools                           |
|------------------|----------------------------------|
| Language          | Python                          |
| Simulation Method | DES (Discrete-Event Simulation) |
| Database          | SQLite                          |
| Visualization     | Matplotlib                      |
| Data Export       | CSV + SQL                       |
| Future Extensions | Streamlit, FastAPI, Docker      |

---

## 🚀 Future Roadmap

- Phase 6: Streamlit Web App  
- Phase 7: REST API (FastAPI)  
- Phase 8: Dockerize Simulation  
- Phase 9: Deploy Dashboard Online  
- Phase 10: Add ML-based Delivery Time Predictions  

---

## 👤 Author

**Talla Sowmya Goud**  
Master’s in Digital Engineering, OVGU Magdeburg  
Specializing in **Simulation • Data Engineering • Cloud • Python**