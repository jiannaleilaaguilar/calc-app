from typing import List, Optional
from sqlalchemy.orm import Session
from models.calculation import Calculation

def get_user_calculations(db: Session, user_id: int = 1) -> List[Calculation]:
    return db.query(Calculation).filter(Calculation.user_id == user_id).all()

def get_calculation_by_id(db: Session, calc_id: int, user_id: int = 1) -> Optional[Calculation]:
    return db.query(Calculation).filter(Calculation.id == calc_id, Calculation.user_id == user_id).first()

def create_calculation(db: Session, user_id: int, operation: str, operand1: float, operand2: float, result: float) -> Calculation:
    calc = Calculation(user_id=user_id, operation=operation, operand1=operand1, operand2=operand2, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc

def update_calculation(db: Session, calc: Calculation, operation: str, operand1: float, operand2: float, result: float) -> Calculation:
    calc.operation = operation
    calc.operand1 = operand1
    calc.operand2 = operand2
    calc.result = result
    db.commit()
    db.refresh(calc)
    return calc

def delete_calculation(db: Session, calc: Calculation) -> None:
    db.delete(calc)
    db.commit()
