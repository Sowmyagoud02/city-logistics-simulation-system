from engine import SimulationEngine
import os

engine = SimulationEngine()
engine.create_drivers()

for i in range(50):
    engine.assign_delivery()

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "data", "deliveries.db")

engine.export_to_sql(db_path)

print("Initial 50 deliveries created.")