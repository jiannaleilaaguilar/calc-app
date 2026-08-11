from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas.calculation import CalculationCreate, CalculationUpdate, CalculationResponse
import crud.calculation as crud

router = APIRouter(prefix="/calculations", tags=["Calculations"])

def compute(op: str, x: float, y: float) -> float:
    if op == "add": return x + y
    if op == "subtract": return x - y
    if op == "multiply": return x * y
    if op == "divide":
        if y == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero.")
        return x / y
    raise HTTPException(status_code=400, detail="Invalid operation type.")

@router.get("", response_model=List[CalculationResponse])
def browse_calculations(db: Session = Depends(get_db)):
    return crud.get_user_calculations(db, user_id=1)

@router.get("/{calc_id}", response_model=CalculationResponse)
def read_calculation(calc_id: int, db: Session = Depends(get_db)):
    calc = crud.get_calculation_by_id(db, calc_id=calc_id, user_id=1)
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found.")
    return calc

@router.post("", response_model=CalculationResponse, status_code=status.HTTP_201_CREATED)
def add_calculation(data: CalculationCreate, db: Session = Depends(get_db)):
    res = compute(data.operation, data.operand1, data.operand2)
    return crud.create_calculation(db, user_id=1, operation=data.operation, operand1=data.operand1, operand2=data.operand2, result=res)

@router.put("/{calc_id}", response_model=CalculationResponse)
def edit_calculation(calc_id: int, data: CalculationUpdate, db: Session = Depends(get_db)):
    calc = crud.get_calculation_by_id(db, calc_id=calc_id, user_id=1)
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found.")
    res = compute(data.operation, data.operand1, data.operand2)
    return crud.update_calculation(db, calc=calc, operation=data.operation, operand1=data.operand1, operand2=data.operand2, result=res)

@router.delete("/{calc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_calculation(calc_id: int, db: Session = Depends(get_db)):
    calc = crud.get_calculation_by_id(db, calc_id=calc_id, user_id=1)
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found.")
    crud.delete_calculation(db, calc)
    return None
