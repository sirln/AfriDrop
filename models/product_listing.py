from .engine.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class ProductListing(Base):
    __tablename__ = 'product_listings'

    productID = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    pricing = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    availability = Column(String(50), nullable=True)
    vendorID = Column(Integer, ForeignKey('vendors.vendorID'), nullable=False)

    # Relationship to vendor table
    vendor = relationship('Vendor', back_populates='product_listings')

