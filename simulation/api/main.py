from fastapi import FastAPI
from engine import ensure_initial_data
from fastapi.middleware.cors import CORSMiddleware
from api.routes.deliveries import router as deliveries_router
from api.routes.analytics import router as analytics_router
from api.routes.drivers import router as drivers_router
from api.routes.delivery_by_id import router as delivery_by_id_router
from api.routes.route_type import router as route_by_id_router
from api.routes.driver_id import router as driver_id_router
from api.routes.simulate import router as simulate_router
from api.routes.simulate_batch import router as simulate_batch_router

app = FastAPI()  # server = app

ensure_initial_data()

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

app.include_router(deliveries_router)
app.include_router(analytics_router)
app.include_router(drivers_router)
app.include_router(delivery_by_id_router)
app.include_router(route_by_id_router)
app.include_router(driver_id_router)
app.include_router(simulate_router)
app.include_router(simulate_batch_router)

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],   # allow ALL origins (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )