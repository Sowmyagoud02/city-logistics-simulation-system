from fastapi import APIRouter
from engine import generate_batch_deliveries
from api.models.delivery import DeliveryModel

router = APIRouter()

@router.post("/simulate/batch")
def simulate_batch(count: int = 50):
    deliveries = generate_batch_deliveries(count)
    return {
        "message": f"{count} deliveries generated successfully",
        "total": len(deliveries),
        "deliveries": [DeliveryModel(**d) for d in deliveries]
    }