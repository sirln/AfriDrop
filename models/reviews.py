from .engine.database import Base
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Review(Base):
    __tablename__ = 'reviews'

    reviewID = Column(Integer, primary_key=True)
    ratings = Column(Integer, nullable=False)
    dateposted = Column(DateTime, default=datetime.utcnow)
    comments = Column(Text, nullable=True)
    customerID = Column(Integer, ForeignKey('customers.customerID'), nullable=False)
    productID = Column(Integer, ForeignKey('product_listings.productID'), nullable=False)

    # Define relationships
    customer = relationship('Customer', back_populates='reviews')
    product = relationship('ProductListing', back_populates='reviews')
