from fastapi import APIRouter

router = APIRouter(prefix="/api/payments", tags=["payments"])

@router.get("/")
async def get_payments():
    """Get all payments"""
    return {"payments": []}

@router.post("/")
async def create_payment(payment: dict):
    """Create a new payment"""
    return {"status": "success", "payment": payment}
