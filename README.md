# 🚚 City Logistics Simulation System

**A Full-Stack Simulation & Analytics Platform for Last-Mile Delivery
Networks**

This project models a **real-world last-mile logistics system** (similar
to Amazon, DHL, FedEx) using **Discrete-Event Simulation (DES)**.
It generates realistic delivery events, captures delays, stores data in
a database, exposes analytics via a REST API, and visualizes insights
through an interactive dashboard.

Built end-to-end to demonstrate **simulation engineering, backend
development, data analytics, and cloud deployment skills**.

------------------------------------------------------------------------

## ⭐ Key Features

✔ Simulates **50+ realistic deliveries** with drivers, routes, delays,
timing & distances
✔ Probabilistic modeling of **traffic, breaks, weather & roadblocks**
✔ Stores simulation output in **SQLite database**
✔ Computes rich analytics: - Average travel time
- Average delay
- Delay rate (%)
- Busiest route
- Fastest & slowest deliveries
- Driver performance metrics

✔ **REST API (FastAPI)** to query & mutate simulation data
✔ **Streamlit dashboard** connected to live API data
✔ Interactive filtering, visualization & data downloads
✔ **Docker-ready** for cloud deployment
✔ Clean, modular & extensible architecture

------------------------------------------------------------------------

## 🧱 Project Architecture
```
    city-logistics-simulation-system/
    │
    ├── simulation/
    │   ├── engine.py
    │   ├── driver.py
    │   ├── delivery.py
    │   ├── generate_initial.py
    │   │
    │   ├── api/
    │   │   ├── main.py
    │   │   ├── routes/
    │   │   ├── models/
    │   │   └── utils/
    │   │
    │   ├── data/
    │   │   └── deliveries.db
    │
    ├── streamlit_app/
    │   ├── app.py
    │   └── api_client/
    │
    ├── Dockerfile.api
    ├── Dockerfile.streamlit
    ├── requirements.txt
    ├── README.md
```
------------------------------------------------------------------------

## 🧪 Simulation Overview (Discrete-Event Simulation)

The system advances **event-to-event** instead of second-by-second,
making it efficient and realistic.

**Core Events**
- **Delivery Assigned** → Driver & route selected
- **Delivery Started** → Travel begins
- **Delay Event** → Traffic / break / weather may occur
- **Delivery Completed** → End time logged & stored

------------------------------------------------------------------------

## 📊 Analytics Generated

✔ Average Travel Time
✔ Average Delay
✔ Delay Rate (%)
✔ Busiest Route
✔ Fastest Delivery
✔ Slowest Delivery
✔ Driver Performance Table

All analytics are exposed via **FastAPI endpoints** and consumed by the
frontend.

------------------------------------------------------------------------

## 📈 Visualization Dashboard (Streamlit)

The Streamlit UI provides:
- Travel time distribution (histogram)
- Delay reason frequency (bar chart)
- Route distribution insights
- Driver performance comparison

**Filtering Options**
- Driver ID
- Route type
- Travel time range

**Extras**
- Export data as CSV / Excel / JSON
- Trigger new delivery simulation via API


------------------------------------------------------------------------

## 🗄 Data Storage

All deliveries are stored in:
```
    simulation/data/deliveries.db
```
SQLite keeps the system lightweight, portable, and ideal for
analytics-driven workflows.

------------------------------------------------------------------------

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/Sowmyagoud02/city-logistics-simulation-system.git
cd city-logistics-simulation-system
```

### 2️⃣ Create initial simulation data

``` bash
python simulation/generate_initial.py
```

### 3️⃣ Start the API

``` bash
uvicorn simulation.api.main:app --reload
```

### 4️⃣ Start Streamlit UI

``` bash
streamlit run streamlit_app/app.py
```

Access:

API Docs → http://127.0.0.1:8000/docs
Streamlit UI → http://localhost:8501

------------------------------------------------------------------------

## 🧩 Tech Stack

| Category      | Tools                     |
| ------------- | ------------------------- |
| Language      | Python                    |
| Simulation    | Discrete-Event Simulation |
| Backend       | FastAPI                   |
| Frontend      | Streamlit                 |
| Database      | SQLite                    |
| Visualization | Matplotlib                |
| API Models    | Pydantic                  |
| Deployment    | Docker, Render            |
| Data Export   | CSV, Excel, JSON          |

------------------------------------------------------------------------

## 🚀 Deployment

-   Backend and frontend are Dockerized
-   Designed for deployment on Render / Railway / Azure
-   Cloud URLs will be added after deployment

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   PostgreSQL database
-   Authentication & user roles
-   Time-series analytics
-   Real-time simulation controls
-   ML-based delivery time prediction
-   Event streaming with Kafka

------------------------------------------------------------------------

## 👤 Author

**Talla Sowmya Goud**
Master's in Digital Engineering - OVGU Magdeburg

**Focus Areas:** 
- Simulation Engineering
- Backend & API Development
- Data Engineering
- Cloud Deployment