from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from admin import crud, models
from app.db import get_db

app = FastAPI()

@app.post("/agencies/")
def register_agency(agency: Agency, db: Session = Depends(get_db)):
    return crud.create_agency(db=db, agency=agency)

@app.put("/agencies/{agency_id}/verify")
def verify_agency(agency_id: int, db: Session = Depends(get_db)):
    return crud.verify_agency(db=db, agency_id=agency_id)

@app.get("/reports/")
def list_reports(db: Session = Depends(get_db)):
    return crud.get_reports(db=db)