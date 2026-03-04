from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    amount: float
    currency: str = "USD"
    description: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    status: str

    class Config:
        from_attributes = True
