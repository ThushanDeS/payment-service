from fastapi import APIRouter

router = APIRouter(prefix="/api/fares", tags=["fares"])

@router.get("/")
async def get_fares():
    """Get all fares"""
    return {
        "fares": [
            {"flight_id": "FL001", "total": 150.00, "fare_class": "economy"},
            {"flight_id": "FL002", "total": 250.00, "fare_class": "business"},
            {"flight_id": "FL003", "total": 180.00, "fare_class": "economy"},
            {"flight_id": "FL004", "total": 350.00, "fare_class": "first"},
            {"flight_id": "FL005", "total": 200.00, "fare_class": "economy"},
        ]
    }

@router.get("/{fare_id}")
async def get_fare(fare_id: str, passengers: int = 1):
    """Get fare details for a specific flight"""
    return {
        "fare_id": fare_id,
        "passengers": passengers,
        "base_price": 100.0,
        "total_price": 100.0 * passengers,
        "currency": "USD"
    }

@router.post("/")
async def create_fare(fare: dict):
    """Create a new fare"""
    return {"status": "success", "fare": fare}
