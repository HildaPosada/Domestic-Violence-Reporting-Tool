from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Agency(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    verified = Column(Boolean, default=False)

class Report(Base):
    id = Column(Integer, primary_key=True, index=True)
    agency_id = Column(Integer, ForeignKey("agency.id"))
    status = Column(String, index=True)
    agency = relationship("Agency", back_populates="reports")