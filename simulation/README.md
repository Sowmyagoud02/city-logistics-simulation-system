🚚 City Logistics Simulation Engine — Documentation

This document describes the design of the simulation engine used to model city-wide delivery operations. The simulation is based on Discrete-Event Simulation (DES) and generates realistic delivery data including delays, travel times, and driver behavior.

🧭 1. What is Simulation?

Simulation is the creation of a digital model of a real-world system so we can study its behavior without needing the real system to operate.

In this project, we simulate a city logistics network where deliveries are generated, delayed, and completed — similar to how DHL, Amazon, or FedEx operate.

⏱️ 2. Discrete-Event Simulation (DES)

This project uses Discrete-Event Simulation, meaning:

Time jumps from one event to the next

We do not simulate every second or minute

Only significant changes (events) are simulated

Example event flow:

09:00 — Delivery assigned  
09:12 — Delivery starts  
09:25 — Traffic delay  
09:40 — Delivery completed  


This method is efficient and is commonly used in logistics, manufacturing, and supply chain simulations.

📦 3. Entities (Objects in the Simulation)

Entities represent the “things” participating in the logistics network.

3.1 Delivery

A delivery represents the transportation of a package from pickup to drop location.

Attributes:

delivery_id

pickup_location

drop_location

assigned_driver

distance_km

route_id

status (created / in-progress / delayed / completed)

delay_reason (if any)

start_time

end_time

3.2 Driver

Drivers perform the actual delivery tasks.

Attributes:

driver_id

speed_factor (affects travel duration)

experience_level

break_frequency

region_assigned

3.3 Route

A route represents the path taken during delivery.

Attributes:

route_id

distance_km

traffic_level (low / medium / high)

zone (city_center / suburbs / industrial / rural)

🎯 4. Events

Events are significant moments that change the state of the system.
Our simulation includes four core events:

4.1 DeliveryAssigned

A new delivery is generated

A driver and route are selected

Simulation time advances to the creation moment

4.2 DeliveryStarted

Delivery officially begins

start_time is set

Estimated travel time computed

4.3 DelayEvent

A random delay can occur due to:

Traffic congestion

Weather

Roadblocks

Driver break

Rerouting

Each delay has:

A duration

A reason

A time when it occurs

4.4 DeliveryCompleted

Delivery reaches the drop location

Simulation time jumps to arrival

Total time and delay time calculated

Completed delivery added to output log

🎲 5. Randomness (Stochastic Behavior)

To make the logistics world realistic, randomness is added using probability distributions.

Random variables include:

Route distance

Driver speed

Delivery frequency

Delay occurrence

Delay duration

Possible distributions:

Uniform distribution → Driver speed, random conditions

Normal distribution → Variation in travel time

Exponential distribution → Time between deliveries

Bernoulli distribution → Whether a delay occurs (yes/no)

Randomness ensures the simulation output looks like real-world data.

🕒 6. Simulation Time (Virtual Clock)

The simulation uses a virtual clock:

It moves event-to-event, not continuously

Every event sets the new time

No real-time waiting is required

Example:

current_time = 10:00
delay_duration = 8 minutes
current_time = 10:08  (after delay event)


This makes the simulation fast and efficient.

📤 7. Output Format

All completed deliveries are logged and exported as:

CSV file:

delivery_logs.csv

Or SQL Table:

delivery_logs

Columns include:

delivery_id

driver_id

route_id

start_time

end_time

total_time_minutes

delay_minutes

delay_reason

distance_km

traffic_level

This output is later used for:

database insertion

analytics

dashboard visualization

API responses

🧩 8. Purpose of This Simulation

This simulation engine is the foundation for the entire project pipeline:

Simulation → Raw Data → Database → SQL Analytics → API → Dashboard


It supports:

Data Engineering

Distributed Systems

Analytics

API design

End-to-end portfolio development
