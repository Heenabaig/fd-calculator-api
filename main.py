from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FD(BaseModel):
    principal: float
    rate: float    # annual %, e.g. 7
    years: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/calculate")
def calculate(fd: FD):
    n = 4  # quarterly compounding
    maturity = fd.principal * (1 + fd.rate / (100 * n)) ** (n * fd.years)
    return {"maturity_amount": round(maturity, 2)}