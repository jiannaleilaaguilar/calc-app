from pydantic import BaseModel, Field
from datetime import datetime

class CalculationBase(BaseModel):
    operation: str = Field(..., description="Operation: add, subtract, multiply, divide")
    operand1: float
    operand2: float

class CalculationCreate(CalculationBase):
    pass

class CalculationUpdate(CalculationBase):
    pass

class CalculationResponse(CalculationBase):
    id: int
    user_id: int
    result: float
    created_at: datetime

    class Config:
        from_attributes = True
