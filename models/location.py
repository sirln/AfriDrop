from .engine.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Location(Base):
    __tablename__ = 'locations'


    locationID = Column(Integer, primary_key=True)
    locationName = Column(String(255), nullable=False)
    timezone = Column(String(50), nullable=True)
    coordinates = Column(String(255), nullable=True)
