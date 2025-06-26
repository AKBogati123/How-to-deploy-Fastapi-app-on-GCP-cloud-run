from fastapi import APIRouter, HTTPException

router = APIRouter()
#for addition
@router.get("/add")
def add(a: float, b: float):
    return {"result": a + b}
#for subtraction
@router.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}
#for multiplication
@router.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@router.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}
