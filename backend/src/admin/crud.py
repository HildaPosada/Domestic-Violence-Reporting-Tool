from sqlalchemy.orm import Session
from agency.models import Agency, Report

def create_agency(db: Session, agency: Agency):
    db.add(agency)
    db.commit()
    db.refresh(agency)
    return agency

def verify_agency(db: Session, agency_id: int):
    agency = db.query(Agency).filter(Agency.id == agency_id).first()
    if agency:
        agency.verified = True
        db.commit()
        return agency
    return None

def get_reports(db: Session):
    return db.query(Report).all()