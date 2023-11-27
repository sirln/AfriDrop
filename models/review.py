#!/usr/bin/python3
"""The review model for AfriDrop"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    """Definition of Review"""
    __tablename__ = 'reviews'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(1024), nullable=False)

    def __init__(self, user_id, product_id, rating, comment, *args, **kwargs):
        """Initialises Review"""
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment
