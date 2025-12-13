from fastapi import APIRouter
from engine import generate_single_delivery
from api.models.create_simulate import SimulateResponse
from api.models.delivery import DeliveryModel

router = APIRouter()

@router.post("/simulate", response_model = SimulateResponse)
def add_delivery():
    data = generate_single_delivery()

    return {
        "message": "New delivery generated successfully",
        "delivery": DeliveryModel(**data)
    }
    # to check the endpoint http://127.0.0.1:8000/docs

