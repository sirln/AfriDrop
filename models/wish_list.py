from .engine.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class WishList(Base):
    __tablename__ = 'wishlists'

    wishListId = Column(Integer, primary_key=True)
    addedDate = Column(DateTime, default=datetime.utcnow)
    priority = Column(Integer, nullable=True)
    quantityDesired = Column(Integer, nullable=False)
    customerID = Column(Integer, ForeignKey('customers.customerID'), nullable=False)
    productID = Column(Integer, ForeignKey('product_listings.productID'), nullable=False)


    customer = relationship('Customer', back_populates='wishlists')
    product = relationship('ProductListing', back_populates='wishlists')
